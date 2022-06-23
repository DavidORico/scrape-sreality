from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    data = None

    def do_GET(self):
        if self.path != '/show':
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Python web server for visualizing "
                               "web scraping results</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Id Name Location Photo_urls</p>", "utf-8"))
        for i in range(50):
            self.wfile.write(bytes("<p>" + str(self.data[i].id) + " " + self.data[i].name + ", " + self.data[i].location
                                   + "</p>", "utf-8"))
            for j in range(len(self.data[i].urls)):
                self.wfile.write(bytes("<a href = " + self.data[i].urls[j] + " > Photo" + str(j) + "</a>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
