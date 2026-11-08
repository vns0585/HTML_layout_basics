from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            with open("html/contacts.html", "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            self.send_error(404, "File not found")
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")