import os
from timeit import default_timer as timer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

def start_tweet_scraper(requests):
    # Change working directory to TweetScraper to find the correct settings
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Init CrawlerRunner
    runner = CrawlerRunner(get_project_settings())

    start_time = timer()

    # Scrape
    crawl(runner, requests)
    reactor.run()

    end_time = timer()
    print(f'Elapsed time: {(end_time - start_time)} seconds')

# Init all requests
@defer.inlineCallbacks
def crawl(crawler_runner, queries):
    for r in queries:
        print(r)
        yield crawler_runner.crawl('TweetScraper', query=r)
    reactor.stop()
