from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Backend deployed through Jenkins!")

server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Backend running on port 5000")

server.serve_forever()