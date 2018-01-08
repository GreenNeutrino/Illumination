from sentiment_analysis import ArticleSentiment 
from news_query import return_articles

article_obj = ArticleSentiment('http://www.cnn.com/2018/01/07/politics/jake-tapper-stephen-miller/index.html')
list_articles = return_articles('WEINSTEIN', '2018-01-08')

for each in list_articles:
    try:
        obj = ArticleSentiment(each['url'])
        print('TITLE',obj.title_sentiment)
        print('TOTAL' , obj.overall_sentiment)

    except:
        print('failed for' , each['url'])


