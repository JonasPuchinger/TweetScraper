from timeit import default_timer as timer
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

queries = None
runner = None

def start_tweet_scraper(requests):
    global queries, runner
    queries = requests

    # Init CrawlerRunner
    runner = CrawlerRunner(get_project_settings())

    start_time = timer()

    # Scrape
    crawl()
    reactor.run()

    end_time = timer()
    print(f'Elapsed time: {(end_time - start_time)} seconds')

# Init all requests
@defer.inlineCallbacks
def crawl():
    for r in queries:
        print(r)
        yield runner.crawl('TweetScraper', query=r)
    reactor.stop()
