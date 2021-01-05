# Introduction #
`TweetScraper` can get tweets from [Twitter Search](https://twitter.com/explore). 
It is built on [Scrapy](http://scrapy.org/) without using [Twitter's APIs](https://dev.twitter.com/rest/public).
The crawled data is not as *clean* as the one obtained by the APIs, but the benefits are you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.

**WARNING:** please be polite and follow the [crawler's politeness policy](https://en.wikipedia.org/wiki/Web_crawler#Politeness_policy).
 

# Installation #
1. Install selenium python bindings: https://selenium-python.readthedocs.io/installation.html. (Note: the `KeyError: 'driver'` is caused by wrong setup)

2. Run:
    
    ```
    $ pip3 install -r requirements.txt
    ```

# Usage #
1. Change the `USER_AGENT` in `TweetScraper/settings.py` to identify who you are
	
		USER_AGENT = 'your website/e-mail'

2. In the root folder of this project, you can run the following commands: 

		scrapy crawl TweetScraper -a query="foo,#bar"

	where `query` is a list of keywords seperated by comma and quoted by `"`. The query can be any thing (keyword, hashtag, etc.) you want to search in [Twitter Search](https://twitter.com/search-home). `TweetScraper` will crawl the search results of the query and save the tweet content and user information.

    	scrapy crawl TwitterConversationScraper -a query="conversation"

	where `query` is a id of a tweet or a Twitter conversation, quoted by `"`. `TwitterConversationScraper` will crawl the results of the query and save the tweets and users in the conversation of the tweet, as well as references to all of them. 
	### Options for TwitterConversationScraper
	- `-a save_to_single_file="True"`: save all tweets, users and references found for a conversation to a single file instead of saving them separately.

	- `-a subfolder="foldername"`: save to a newly created subfolder in your specified `SAVE_CONVERSATION_PATH`.

3. The tweets will be saved to disk in `../Data/tweet/` in default settings and `../Data/user/` is for user data. References to conversations will be saved in `../Data/conversation` The file format is JSON. Change the `SAVE_TWEET_PATH`, `SAVE_USER_PATH` and `SAVE_CONVERSATION_PATH` in `TweetScraper/settings.py` if you want another location.


# Acknowledgement #
This repository is a fork of the [original TweetScraper](https://github.com/jonbakerfish/TweetScraper)


# License #
TweetScraper is released under the [GNU GENERAL PUBLIC LICENSE, Version 2](https://github.com/JonasPuchinger/TweetScraper/blob/master/LICENSE)
