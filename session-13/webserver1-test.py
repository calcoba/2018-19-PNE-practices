import http.server
import socketserver

# Define the Server's port
PORT = 8009


class TestHandler (http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)
        if self.path == "/":
            f = open("index.html", 'r')
            content = f.read()
            f.close()

        else:
            print("ERROR")
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

# -- Use the http.server Handler


# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
