import sys
import newspaper
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class ArticleSentiment():
    '''
    Class capture categorize various sentiment metrics for 
    articles
    '''
    def __init__(self, url):
        self.article = self._parse_article_text(url)
        self.title_sentiment = self.sentiment_analysis(self.article.title)
        self.overall_sentiment = self._sentiment_analysis_total(self.article.text)


    def sentiment_sentence_with_keyword(self, keyword):
        '''
        TODO
        '''
        pass


    def _parse_article_text(self, url):
        '''
        Returns article object with parsed and downloaded text
        '''
        first_article = newspaper.Article(url, language='en')
        first_article.download()
        first_article.parse()
        return first_article


    def sentiment_analysis(self, text):
        '''
        returns sentiment analysis metric
        with positive, negative, and compound
        '''
        analyzer = SentimentIntensityAnalyzer()
        results = analyzer.polarity_scores(text)
        return results 


    def _sentiment_analysis_total(self, article):
        '''
        sentiment analysis for all text in article
        '''
        return self.sentiment_analysis(article)


    def sentiment_analysis_all_sentences(self, article):
        '''
        sentiment analysis for all split sentences
        line at a time

        output: {'sentence': sentiment_metrics}
        '''

        sentences = article.text.split('.')
        data = {}

        for sentence in sentences:
            data[sentence] = sentiment_analysis(sentence)

        return data

'''
def main():
    example_url = sys.argv[1]
    data = parse_article_text(example_url)
    sentences = data.text.split('.')

    for sentence in sentences:
        print( sentence)
        print(sentiment_analysis_sentence(sentence))

    print(data.title)
    print (sentiment_analysis_sentence(data.title), 'TITLE')
    print(sentiment_analysis_sentence(data.text), 'OVERALL')


if __name__ == "__main__":
    main()
    print ('finished')
'''

