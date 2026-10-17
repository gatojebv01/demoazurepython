import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Fetch injected secrets from environment variables
        secret_word_1 = os.environ.get("MY_SECRET_WORD_1", "DefaultWord1")
        secret_word_2 = os.environ.get("MY_SECRET_WORD_2", "DefaultWord2")
        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        response_text = f"Hello! The secret words are: {secret_word_1} and {secret_word_2}\n"
        self.wfile.write(response_text.encode("utf-8"))

def run():
    print("Starting server on port 8080...")
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
