from textblob import TextBlob
import textblob
import newspaper
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def parse_article_text(url):
    first_article = newspaper.Article(url, language='en')
    first_article.download()
    first_article.parse()
    return first_article

def sentiment_analaysis_sentence(sentence):
    analyzer = SentimentIntensityAnalyzer()
    results = analyzer.polarity_scores(sentence)
    return results 

def main():
    #example_url = 'https://arstechnica.com/information-technology/2018/01/intel-ceos-sale-of-stock-just-before-security-bug-reveal-raises-questions/'
    #example_url =  "https://www.denverpost.com/2018/01/06/amazon-maintains-holiday-dominance-despite-stepped-up-pressure/"
    #example_url = 'http://www.latimes.com/local/california/la-me-ln-flu-surge-20180106-htmlstory.html'
    example_url = 'https://www.theregister.co.uk/2018/01/04/intel_amd_arm_cpu_vulnerability/'

    data = parse_article_text(example_url)
    sentences = data.text.split('.')
    for sentence in sentences:
        print( sentence)
        print(sentiment_analaysis_sentence(sentence))
    print(data.title)
    print (sentiment_analaysis_sentence(data.title), 'TITLE')
    print(sentiment_analaysis_sentence(data.text), 'OVERALL')


if __name__ == "__main__":
    main()
    print ('finished')


