import os, logging, json, re
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User, Conversation, SingleFileConversation
from TweetScraper.utils import mkdirs


logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''

    @classmethod
    def from_crawler(cls, crawler):
        spider_name = getattr(crawler.spider, 'name')
        query_name = getattr(crawler.spider, 'query')
        save_to_single_file = getattr(crawler.spider, 'save_to_single_file', None)
        subfolder = getattr(crawler.spider, 'subfolder', None)
        if spider_name == 'TweetScraper':
            account_name = re.search(r'from:(\S*)\s?', query_name).group(1)
            query_name = account_name if account_name else query_name
        arguments = {
            'spider_name': spider_name,
            'query_name': query_name,
            'save_to_single_file': save_to_single_file,
            'subfolder': subfolder
        }
        return cls(arguments)


    def __init__(self, arguments):
        self.spider_name = arguments['spider_name']
        self.saveTweetPath = SETTINGS['SAVE_TWEET_PATH'] + arguments['query_name']
        self.saveUserPath = SETTINGS['SAVE_USER_PATH'] + arguments['query_name']
        self.saveConversationPath = SETTINGS['SAVE_CONVERSATION_PATH'] + arguments['subfolder']
        if arguments['save_to_single_file'] == None:
            mkdirs(self.saveTweetPath)
            mkdirs(self.saveUserPath)
        if self.spider_name == 'TwitterConversationScraper':
            mkdirs(self.saveConversationPath)


    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip tweet:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update tweet:%s"%item['id_'])
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add tweet:%s" %item['id_'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip user:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update user:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" %item['id_'])

        elif isinstance(item, Conversation):
            savePath = os.path.join(self.saveConversationPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip conversation:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update conversation:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add conversation:%s" %item['id_'])
        
        elif isinstance(item, SingleFileConversation):
            savePath = os.path.join(self.saveConversationPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip conversation:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update conversation:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add conversation:%s" %item['id_'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False)
