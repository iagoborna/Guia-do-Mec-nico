import http.server
import socketserver
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("Servidor rodando em http://127.0.0.1:8000")
    
    webbrowser.open("http://127.0.0.1:8000")
    
    httpd.serve_forever()