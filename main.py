from scrapyscript import Job, Processor
import logging
from spider.spiders.sreality_spider import SrealitySpider
from src.database_estates import DatabaseEstates
from http.server import HTTPServer
from src.web_server import MyServer


def main():
    # start web scraping job of sreality and get yielded data
    logging.info('Starting web scraping job.')
    srealityJob = Job(SrealitySpider)

    processor = Processor(settings=None)
    data = processor.run([srealityJob])
    #print(json.dumps(data, indent=4))

    # initialize and add data to the database
    logging.info('Establishing connection to database.')
    db_estates = DatabaseEstates()
    db_estates.insert(data)
    #db_estates.view_all()

    # run web server that displays results on http://127.0.0.1:8080/show
    logging.info('Creating python web server.')
    hostName = "0.0.0.0"
    serverPort = 8080
    myserver = MyServer
    myserver.data = db_estates.get_all()
    webServer = HTTPServer((hostName, serverPort), myserver)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")


if __name__ == '__main__':
    main()
