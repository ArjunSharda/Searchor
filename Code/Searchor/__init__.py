def SearchGoogle(query):
    query = query.replace(" ", "+")
    query_URL = "https://www.google.com/search?q=" + query
    return query_URL

def SearchYoutube(query):
    query = query.replace(" ", "+")
    query_URL = "https://www.youtube.com/results?search_query=" + query
    return query_URL

def SearchTwitter(query):
    query = query.replace(" ", "+")
    query_URL = "https://twitter.com/search?q=" + query
    return query_URL

def SearchWikipedia(query):
    query = query.replace(" ", "_")
    query_URL = "https://en.wikipedia.org/wiki/" + query
    return query_URL

def SearchDictionary(query):
    query = query.replace(" ", "-")
    query_URL = "https://www.dictionary.com/browse/" + query
    return query_URL

def SearchYahoo(query):
    query = query.replace(" ", "+")
    query_URL = "https://search.yahoo.com/search?p=" + query
    return query_URL

def SearchAmazon(query):
    query = query.replace(" ", "+")
    query_URL = "https://www.amazon.com/s?k=" + query
    return query_URL

def SearchBing(query):
    query = query.replace(" ", "+")
    query_URL = "https://www.bing.com/search?q=" + query
    return query_URL

def SearchDuckDuckGo(query):
    query = query.replace(" ", "+")
    query_URL = "https://duckduckgo.com/?q=" + query
    return query_URL

def SearchWalmart(query):
  query = query.replace(" ", "+")
  query_URL = "https://www.walmart.com/search?q=" + query
  return query_URL


def ExploreMicrosoft(query):
  query = query.replace(" ", "+")
  query_URL = "https://www.microsoft.com/en-us/search/explore?q=" + query
  return query_URL

