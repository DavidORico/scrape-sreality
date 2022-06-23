from scrapyscript import Job, Processor
import json
from spider.spiders.sreality_spider import SrealitySpider
from src.database_estates import DatabaseEstates


def main():
    srealityJob = Job(SrealitySpider)

    processor = Processor(settings=None)
    data = processor.run([srealityJob])

    #print(json.dumps(data, indent=4))
    db_estates = DatabaseEstates()
    db_estates.insert(data)
    #db_estates.view_all()


if __name__ == '__main__':
    main()
