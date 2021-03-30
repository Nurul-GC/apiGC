from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        template_html = open(self.path).read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(template_html, 'utf-8'))


if __name__ == '__main__':
    print("[i] Servidor operando..\n[i] Abra o navegador e digite o endereço: https://localhost:8000")
    run_server = HTTPServer(('localhost', 8000), Server)
    run_server.serve_forever()
