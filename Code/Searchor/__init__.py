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

def SearchGitHub(query):
  query = query.replace(" ", "+")
  query_URL = "https://github.com/search?q=" + query
  return query_URL

def Custom(query, queryurl, spacingsymbol):
  query = query.replace(" ", spacingsymbol)
  query_URL = queryurl + query
  return query_URL

def SearchApple(query):
  query = query.replace(" ", "-")
  query_URL = "https://apple.com/search/" + query
  return query_URL

def SearchTarget(query):
  query = query.replace(" ", "+")
  query_URL = "https://www.target.com/s?searchTerm=" + query
  return query_URL

def SearchGenius(query):
  query = query.replace(" ", "%20")
  query_URL = "https://genius.com/search?q=" + query
  return query_URL

def SearchTwitch(query):
  query = query.replace(" ", "%20")
  query_URL = "https://www.twitch.tv/search?term=" + query
  return query_URL

def SearchStackOverflow(query):
  query = query.replace(" ", "+")
  query_URL = "https://stackoverflow.com/search?q=" + query
  return query_URL

def SearchJetBrains(query):
  query = query.replace(" ", "+")
  jbs = "&s=full"
  query_URL = "jetbrains.com/?q=" + query + jbs
  return query_URL

def SearchQuora(query):
  query = query.replace(" ", "%20")
  query_URL = "https://www.quora.com/search?q=" + query
  return query_URL

def SearchUrbanDictionary(query):
  query = query.replace(" ", "%20")
  query_URL = "https://www.urbandictionary.com/define.php?term=" + query
  return query_URL
