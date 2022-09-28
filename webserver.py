# user sbi_sicherheit added
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Exfiltration Environment')
 
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        decoded = body.decode('utf-8')
        print('[+] Received: ')
        print(decoded)
        f = open('/tmp/exfil.txt', 'w')
        f.write(decoded)
 
httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()
