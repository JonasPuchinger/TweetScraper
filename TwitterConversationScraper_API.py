import os
from timeit import default_timer as timer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

def start_twitter_conversation_scraper(requests):
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
        if hasattr(r, 'save_to_single_file') and hasattr(r, 'subfolder'):
            yield crawler_runner.crawl('TwitterConversationScraper', query=r['query'], save_to_single_file=r['save_to_single_file'], subfolder=r['subfolder'])
        if hasattr(r, 'save_to_single_file') and not hasattr(r, 'subfolder'):
            yield crawler_runner.crawl('TwitterConversationScraper', query=r, save_to_single_file=r['save_to_single_file'])
        if not hasattr(r, 'save_to_single_file') and hasattr(r, 'subfolder'):
            yield crawler_runner.crawl('TwitterConversationScraper', query=r, subfolder=r['subfolder'])
        else:
            yield crawler_runner.crawl('TwitterConversationScraper', query=r)
    reactor.stop()