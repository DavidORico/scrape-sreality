from scrapyscript import Job, Processor
import logging
from spider.spiders.sreality_spider import SrealitySpider
from src.database_estates import DatabaseEstates
from src.flask_web_server import run_web_server


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
    db_estates.insert_all(data)
    #db_estates.view_all()

    # run web server that displays results on http://127.0.0.1:8080/show
    logging.info('Creating python web server.')
    run_web_server(db_estates.get_all()[-50:])


if __name__ == '__main__':
    main()
