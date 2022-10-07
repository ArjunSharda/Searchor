Searchor
========
![PyPI](https://img.shields.io/pypi/v/searchor?color=green&logo=python&logoColor=green)
[![Discord](https://img.shields.io/discord/1026470859868741662)](https://discord.gg/fPXNMW7swn)
<div style="text-align: center; display: grid; justify-content: center;"><img style="margin: auto; margin-bottom: 1rem; border-radius: 30%;" height="150" width="150" src="https://raw.githubusercontent.com/ArjunSharda/Searchor/main/ext/searchor.png"/></div>

⚡️ Quick and easy search engine queries.

Installation
------------
**[Python 3.7+](https://www.python.org/downloads/) is required**
```bash
# MacOS / Linux (via Terminal)
python3 -m pip install -U searchor

# Windows (via CMD Prompt)
py -3 -m pip install -U searchor
```

Quick Start
-----------
```python
>>> from searchor import Engine
>>> Engine.Google.search("Hello, World!")
'https://www.google.com/search?q=Hello%2C%20World%21'
```

Take a look at more examples in the [examples](https://github.com/ArjunSharda/Searchor/tree/main/examples) folder!

*Note*:&nbsp; Engine names follow the **UpperCamelCase** convention.(eg: ChromeWebStore).

v2.2.1 Changes
--------------
- **[ADDED]** Added Instagram, Brave, AlternativeTo, Docker Hub, Unsplash, BBC, Indeed, CountryCode, OpenLibrary, Dell, Wired, Google Maps, Google Images, Audible, Behance, Bugzilla, Dribble, Flipkart, Google Fonts,  Imgur, Imgur, MDN, NPM and Steam search engines.
- **[FIXED]** Fixed a broken image in the PyPi of Searchor.
- **[REMOVED]** Removed an unneeded library in the codebase.


Migration
---------
Instead of different functions for each engine, Searchor `v2.2.0` uses a single function with an `Engine` enum. This makes it easier to use and maintain. If you're migrating from `v2.0.0`, compare the differences between the following snippets:
```python
# Searchor 2.0.0
from searchor import search, Engine
search("Hello, World!", Engine.Google)
```
```python
# Searchor v2.2.0
from searchor import Engine
Engine.Google.search("Hello, World!")
```

