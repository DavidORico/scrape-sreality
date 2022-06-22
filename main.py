from scrapyscript import Job, Processor
import json
from spider.spiders.sreality_spider import SrealitySpider


def main():
    srealityJob = Job(SrealitySpider)

    processor = Processor(settings=None)
    data = processor.run([srealityJob])

    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    main()
