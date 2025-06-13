import http.server
import socketserver
import webbrowser
import os

PORT = 8000
FILENAME = "data/data.csv"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/save":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")

            with open(FILENAME, "w", encoding="utf-8") as f:
                f.write(post_data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Saved successfully.")
        else:
            self.send_error(404)

os.chdir(os.path.dirname(__file__))

with socketserver.TCPServer(("localhost", PORT), MyHandler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"Serving at {url}")
    webbrowser.open(url)
    httpd.serve_forever()
