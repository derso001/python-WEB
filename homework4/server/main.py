import mimetypes
import pathlib
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote_plus


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)

        if url.path == "/":
            self.send_http_file("index.html")
    
        elif url.path == "/contact":
           self.send_http_file("contact.html")
        
        elif url.path == "/thanks":
           self.send_http_file("thanks.html")
        else:
            if pathlib.Path().joinpath(url.path[1:]).exists():
                self.send_static()
            else:
                self.send_http_file('error.html')



    def do_POST(self):

        raw_data = self.rfile.read()
        data = unquote_plus(raw_data.decode())
        data = self.parse_form_data(data)

        print(data)

        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()


    def parse_form_data(self, data):
        raw_params = data.split("&")
        data = {key.title(): value for key, value in [param.split("=") for param in raw_params]}
        return data

    def send_http_file(self, html_page, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open(html_page, "rb") as file:
            self.wfile.write(file.read())

    def send_static(self):

        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

if __name__ == "__main__":

    server = HTTPServer(("localhost", 5353), MyHandler)
    server.serve_forever()