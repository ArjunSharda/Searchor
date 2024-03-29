Searchor
========


<img align="left" src="http://estruyf-github.azurewebsites.net/api/VisitorHit?user=ArjunSharda&repo=Searchor&countColorcountColor&countColor=%237B1E7B"/>
<img align="right" src="https://img.shields.io/github/repo-size/ArjunSharda/Searchor?style=for-the-badge&logo=appveyor" alt="GitHub repo size"/>

<img align="right" alt="Json-Generator" src="https://socialify.git.ci/ArjunSharda/Searchor/image?description=1&font=Rokkitt&forks=1&issues=1&language=1&logo=https%3A%2F%2Fgithub.com%2FArjunSharda%2FSearchor%2Fblob%2Fmain%2Fext%2Fsearchor.png%3Fraw%3Dtrue&name=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light" />

<p align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" alt=" forks"/>
</p>

![PyPI](https://img.shields.io/pypi/v/searchor?color=green&logo=python&logoColor=green)
[![Discord](https://img.shields.io/discord/1026470859868741662)](https://discord.gg/fPXNMW7swn)
<div style="text-align: center; display: grid; justify-content: center;"><img style="margin: auto; margin-bottom: 1rem; border-radius: 30%;" height="150" width="150" src="https://raw.githubusercontent.com/ArjunSharda/Searchor/main/ext/searchor.png"/></div>

# Description

 Searchor is an all-in-one PyPi Python Library that simplifies web scraping, obtaining information on an topic, and generating search query URLs. Searchor is an a efficient tool for Python developers, with many web development needs in one, with support of over 100+ Engines and custom engines allowed, making it easy for developers to use for their web programming needs in Python without relying on many third-party dependencies. Furthermore, Searchor has a wide range of support, including command line interface and pip.

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
>>> Engine.Google.search("Hello, World!"))
'https://www.google.com/search?q=Hello%2C%20World%21'
```
Custom Engine
-------------
```python
>>> from searchor import Engine
>>> Engine.new("Colgate", "https://www.colgate.com/en-us/search/all?term=")
>>> Engine.Colgate.search("Hi world!")
'https://www.colgate.com/en-us/search/all?term=Hi%20world!"
```
Searchor CLI Quick Start
```bash
$ searchor Google "Hello World!" --copy
```
<br>
</br>

Web Scrape
----------
```python
>>> from searchor import Information
>>> Information.scrape("https://google.com")
>>> '{'title': 'Google', 'paragraphs': [<p style="font-size:8pt;color:#70757a">© 2023 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p>]}'
```


Get Information
---------------
```python
>>> from searchor import Information
>>> Information.getinfo("GitHub")
>>> 'GitHub, Inc. is an Internet hosting service for software development and version control using Git. It provides the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project. Headquartered in California, it has been a subsidiary of Microsoft since 2018.'
```
Take a look at more examples in the [examples](https://github.com/ArjunSharda/Searchor/tree/main/examples) folder!

*Note*:&nbsp; Engine names follow the **UpperCamelCase** convention.(eg: ChromeWebStore).

Docker
------

Building the docker image
```sh
$ docker build -t searchor .
```

Running searchor on the docker container
```sh
$ docker run --rm -it searchor sh
/usr/src/searchor/examples # python searchamazon.py
https://www.amazon.com/s?k=Hello%2C%20World%21
```

v2.5.2 Changes
--------------
v2.5.0
- **[ADDED]** Added a new Enum class `Information`.
- **[ADDED]** Added `getinfo` function in the `Information` Enum to gather information about a given topic, using Wikipedia.
- **[ADDED]** Add `web_scraper` function in the `Information` Enum, to web scrape a URL that is given.
- **[ADDED]** Added bs4 and requests as dependencies.
- **[MODIFIED]** The Searchor Package is now officially becoming a library, and is therefore no longer considered a package.

v2.5.2
- **[FIXED]** Fixed issue with web scraping, with attribute errors, and CLI issues

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

## Want to contribute?
Take a look at the [contributing guidelines](CONTRIBUTING.md)!

<hr>
<h6 align="center">© Arjun Sharda 2022-present
<br>
All Rights Reserved</h6>
