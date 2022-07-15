import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        s.connect(("localhost", 6531))
    except socket.error:
        webbrowser.open("http://localhost:6531")
        server = HTTPServer(("0.0.0.0", 6531), SimpleHTTPRequestHandler)
        server.serve_forever()
    else:
        webbrowser.open("http://localhost:6531")
