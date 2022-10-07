from urllib.parse import quote
from webbrowser import open_new_tab
from enum import Enum, unique


@unique 
class Engine(Enum):
    AlternativeTo = "https://alternativeto.net/browse/search/?q={query}"
    Apple = "https://www.apple.com/search/{query}"
    Ask = "https://www.ask.com/web?q={query}"
    AOL = "https://search.aol.com/aol/search?q={query}"
    Amazon = "https://www.amazon.com/s?k={query}"
    Atlassian = "https://www.atlassian.com/search?q={query}"
    AmazonWebServices = "https://aws.amazon.com/search/?searchQuery={query}"
    Audible = "https://www.audible.in/search?keywords={query}"
    Behance = "https://www.behance.net/search?search={query}"
    Bing = "https://www.bing.com/search?q={query}"
    BlogSpot = "https://www.searchblogspot.com/search?q={query}"
    Brave = "https://search.brave.com/search?q={query}"
    Bugzilla = "https://bugzilla.mozilla.org/buglist.cgi?quicksearch={query}"
    BBC = "https://www.bbc.co.uk/search?q={query}"
    ChromeWebStore = "https://chrome.google.com/webstore/search/{query}"
    CountryCode = "https://countrycode.org/{query}"
    Crunchyroll = "https://www.crunchyroll.com/search?q={query}"
    CrunchyrollBeta = "https://beta.crunchyroll.com/search?q={query}"
    Dell = "https://www.dell.com/en-us/search/{query}"
    DuckDuckGo = "https://www.duckduckgo.com/?q={query}"
    Dictionary = "https://www.dictionary.com/browse/{query}"
    DockerHub = "https://hub.docker.com/search?q={query}"
    Dribbble = "https://dribbble.com/search/{query}"
    Excite = "https://results.excite.com/serp?q={query}"
    eBay = "https://www.ebay.com/sch/{query}"
    Facebook = "https://www.facebook.com/search/top/?q={query}"
    Fandom = "https://www.fandom.com/?s={query}"
    FedEx = "https://www.fedex.com/en-us/search.html?q={query}"
    Flipkart = "https://www.flipkart.com/search?q={query}"
    G2 = "https://www.g2.com/search?query={query}"
    GoogleFonts = "https://fonts.google.com/?query={query}"
    GitHub = "https://www.github.com/search?q={query}"
    GitLab = "https://www.gitlab.com/search?search={query}"
    Google = "https://www.google.com/search?q={query}"
    GoogleImages = "https://www.google.com/search?tbm=isch&q={query}"
    GoogleMaps = "https://www.google.com/maps/search/{query}"
    Genius = "https://www.genius.com/search?q={query}"
    Imgur = "https://imgur.com/search?q={query}"
    Indeed = "https://www.indeed.com/jobs?q={query}"
    InstantGaming = "https://www.instant-gaming.com/en/search/?q={query}"
    Instagram = "https://www.instagram.com/{query}"
    JetBrains = "https://www.jetbrains.com/search/?q={query}"
    Lycos = "https://search20.lycos.com/web/?q={query}"
    LinkedIn = "https://www.linkedin.com/search/results/all/?keywords={query}"
    Lenovo = "https://www.lenovo.com/us/en/search?fq=&text={query}"
    MDN = "https://developer.mozilla.org/en-US/search?q={query}"
    Medium = "https://medium.com/search?q={query}"
    Microsoft = "https://www.microsoft.com/en-us/search/explore?q={query}"
    Mmoga = "https://www.mmoga.com/advanced_search.php?keywords={query}"
    NPM = "https://www.npmjs.com/search?q={query}"
    OpenLibrary = "https://openlibrary.org/search?q={query}"
    OperaAddons = "https://addons.opera.com/en/search/?query={query}"
    PyPi = "https://pypi.org/search/?q={query}"
    Quora = "https://www.quora.com/search?q={query}"
    Replit = "https://replit.com/search?q={query}"
    Reddit = "https://www.reddit.com/search/?q={query}"
    Spotify = "https://open.spotify.com/search/{query}"
    StackOverflow = "https://www.stackoverflow.com/search?q={query}"
    Steam = "https://store.steampowered.com/search/?term={query}"
    TikTok = "https://www.tiktok.com/search?q={query}"
    Twitter = "https://twitter.com/search?q={query}"
    Twitch = "https://www.twitch.tv/search?term={query}"
    Target = "https://www.target.com/s?searchTerm={query}"
    Textures = "https://www.textures.com/search?q={query}"
    Thesaurus = "https://www.thesaurus.com/browse/{query}"
    Unsplash = "https://unsplash.com/s/photos/{query}"
    UPS = "https://www.ups.com/us/en/SearchResults.page?q={query}"
    UrbanDictionary = "https://www.urbandictionary.com/define.php?term={query}"
    USPS = "https://www.usps.com/search/results.htm?keyword={query}"
    Wikipedia = "https://en.wikipedia.org/w/index.php?search={query}"
    Wikihow = "https://www.wikihow.com/wikiHowTo?search={query}"
    Wired = "https://www.wired.com/search/?q={query}"
    Wolframalpha = "https://www.wolframalpha.com/input?i={query}"
    Walmart = "https://www.walmart.com/search?q={query}"
    Youtube = "https://www.youtube.com/results?search_query={query}"
    Yahoo = "https://search.yahoo.com/search?p={query}"
    Yandex = "https://yandex.com/search/?text={query}"

    def search(self, query, open_web=False, additional_queries: dict = None):
        url = self.value.format(query=quote(query, safe=""))
        if additional_queries:
            url += ("?" if "?" not in self.value.split("/")[-1] else "&") + "&".join(
                query + "=" + quote(query_val)
                for query, query_val in additional_queries.items()
            )
        if open_web is True:
            open_new_tab(url)
        return url
    
