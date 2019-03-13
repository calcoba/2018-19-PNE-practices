import socketserver
import http.server
import termcolor
from P6.Seq import Seq

PORT = 8000


def seq_analysis(msg):
    # Empty dic initiated
    actions = {}

    # The function makes the computations
    msg = msg.split("&")
    seq = Seq(msg.pop(0).split("=")[-1].upper())
    bases = "ACTG"

    # Check if the characters of the DNA sequence are all allowed
    if not all(c in bases for c in seq.strbases):
        actions = "ERROR"
        return actions

    actions.update({"Seq": seq.strbases})
    # Possible functions the program could perform
    base = ""
    for request in msg:
        if "base" in request:
            base += request[-1]
        elif "count" in request or "perc" in request:
            operation = request.split("=")[-1]
            action = seq.call_function(operation, base)
            actions.update({"Result for " + base +" " + operation: action})

        elif request == "chk=on":
            action = seq.len()
            actions.update({"Len": action})
            # If the request action is not allowed then send back an empty variable

    return actions

    # Sending the message back to the client pending


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Printing the request line
        termcolor.cprint(self.requestline, 'blue')

        request = self.requestline.split()[1]
        print(request)
        actions = request.split("?")[-1]
        print(actions)

        if self.path.startswith("/seq"):
            analysis = seq_analysis(actions)
            if analysis == "ERROR":
                f = open("error.html", 'r')
                contents = f.read()
                f.close()
            else:
                results = ""
                for key, value in analysis.items():
                    results += "<p>"+key+" : "+str(value)+"</p>"

                contents = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>SeqAnalysis</title>
                    </head>
                    <body>
                     <h1>Result of Sequence Analysis</h1>
                      {}
                      <a href="/">Main page</a>
                    </body>
                    </html>""".format(results)

        elif self.path == "/":
            f = open("form.html", 'r')
            contents = f.read()
            f.close()

        else:
            f = open("error.html", 'r')
            contents = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("")
print("Server Stopped")
