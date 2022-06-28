from flask import Flask


def run_web_server(data):
    app = Flask(__name__)

    @app.route("/show")
    def show_estates():
        html_string = "<!DOCTYPE html><html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" \
                      "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\">" \
                      "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js\"></script>" \
                      "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js\"></script>" \
                      "</head><body><div class=\"container\"><h2>Table of 50 estates scraped from sreality</h2>" \
                      "<table class=\"table\"><thead><tr><th>#</th><th>Name</th><th>Location</th><th>Photo urls</th></tr></thead>" \
                      "<tbody>"
        for est in data:
            html_string += "<tr><td>" + str(est.id) + "</td><td>" + est.name + "</td><td>" + est.location + "</td><td>"
            for i in range(len(est.urls)):
                html_string += "<a href=" + est.urls[i] + ">Photo_" + str(i) + " </a>"
            html_string += "</td></tr>"
        html_string += "</tbody></table></div></body></html>"

        return html_string

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run(host='0.0.0.0', port=8001)
