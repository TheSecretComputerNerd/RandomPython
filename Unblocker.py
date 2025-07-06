import http.server
import socketserver
import urllib.request

class UnblockerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  # Remove the leading '/'
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        try:
            response = urllib.request.urlopen(url)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.read())
        except Exception as e:
            self.send_error(404, str(e))

def run_unblocker(port=8000):
    with socketserver.TCPServer(("", port), UnblockerHandler) as httpd:
        print(f"Unblocker running on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_unblocker()