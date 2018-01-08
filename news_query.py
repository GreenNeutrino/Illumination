import requests

NEWSPAPER_QUERY = ('https://newsapi.org/v2/everything?'
                   'q={0}&'
                   'from={1}&'
                   'sortBy=popularity&'
                   'apiKey=476e1d6a6e954b96a85856c91df37eda')


def return_articles(keyword, date):
    response = requests.get(NEWSPAPER_QUERY.format(keyword, date))
    articles = response.json()
    print (articles)
    list_of_articles = articles['articles'] 

    return list_of_articles


