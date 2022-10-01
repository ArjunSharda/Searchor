from urllib.parse import quote

class Engine:
    Apple = "https://www.apple.com/search/{query}"
    Ask = "https://www.ask.com/web?q={query}"
    Amazon = "https://www.amazon.com/s?k={query}"   
    Bing = "https://www.bing.com/search?q={query}"
    ChromeWebStore = "https://chrome.google.com/webstore/search/{query}"
    Crunchyroll = "https://www.crunchyroll.com/search?q={query}"
    CrunchyrollBeta = "https://beta.crunchyroll.com/search?q={query}"
    DuckDuckGo = "https://www.duckduckgo.com/?q={query}"
    Dictionary = "https://www.dictionary.com/browse/{query}"
    Facebook = "https://www.facebook.com/search/top/?q={query}"
    Fandom = "https://www.fandom.com/?s={query}"
    Github = "https://www.github.com/search?q={query}"
    Google = "https://www.google.com/search?q={query}"
    Genius = "https://www.genius.com/search?q={query}"
    InstantGaming = "https://www.instant-gaming.com/en/search/?q={query}"
    JetBrains = "https://www.jetbrains.com/search/?q={query}"
    LinkedIn = "https://www.linkedin.com/search/results/all/?keywords={query}"
    Lenovo = "https://www.lenovo.com/us/en/search?fq=&text={query}"
    Microsoft = "https://www.microsoft.com/en-us/search/explore?q={query}"
    Mmoga = "https://www.mmoga.com/advanced_search.php?keywords={query}"
    OperaAddons = "https://addons.opera.com/en/search/?query={query}"
    Quora = "https://www.quora.com/search?q={query}"
    Replit = "https://replit.com/search?q={query}"
    StackOverflow = "https://www.stackoverflow.com/search?q={query}"
    TikTok = "https://www.tiktok.com/search?q={query}"
    Twitter = "https://twitter.com/search?q={query}"
    Twitch = "https://www.twitch.tv/search?term={query}"
    Target = "https://www.target.com/s?searchTerm={query}"
    Textures = "https://www.textures.com/search?q={query}"
    Thesaurus = "https://www.thesaurus.com/browse/{query}"
    UrbanDictionary = "https://www.urbandictionary.com/define.php?term={query}"
    Wikipedia = "https://en.wikipedia.org/w/index.php?search={query}"
    Wikihow = "https://www.wikihow.com/wikiHowTo?search={query}"
    Wolframalpha = "https://www.wolframalpha.com/input?i={query}"
    Walmart = "https://www.walmart.com/search?q={query}"
    Youtube = "https://www.youtube.com/results?search_query={query}"
    Yahoo = "https://search.yahoo.com/search?p={query}"
    FedEx = "https://www.fedex.com/en-in/search.html?q={query}"

#search function    
def search(query, engine=Engine.Google):
    return engine.format(query=quote(query, safe=""))

#returns all the engines available
def engine_list():  
    members = [attr for attr in dir(Engine) if not callable(getattr(Engine, attr)) and not attr.startswith("__")]
    return members
