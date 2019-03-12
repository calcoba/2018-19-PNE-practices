import http.server
import socketserver
import termcolor

PORT = 8004


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Printing the request line
        termcolor.cprint("Request line: "+self.requestline, 'blue')
        termcolor.cprint("   CMD: "+self.command, 'red')
        termcolor.cprint("   Path: "+self.path, 'yellow')
        requests = self.path.split("?")[-1]
        if self.path.startswith("/echo"):
            for request in requests.split("&"):
                request = request.split("=")[-1]
                print(request)
                hi = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                    </head>
                    <body>
                     <h1>Echo from received message</h1>
                      <p>{}</p>
                      <a href="/">Main page</a>
                    </body>
                    </html>""".format(request)
                self.send_response(200)

                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(hi)))
                self.end_headers()

                # -- Sending the body of the response message
                self.wfile.write(str.encode(hi))
            return
        else:
            f = open("form1.html", 'r')
            contents = f.read()

            self.send_response(200)

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()

            # -- Sending the body of the response message
            self.wfile.write(str.encode(contents))
            return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("")
print("Server Stopped")
