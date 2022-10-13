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

Searchor CLI Quick Start
---------
`$ searchor Google "Hello World!" --copy`
<br>
</br>

Take a look at more examples in the [examples](https://github.com/ArjunSharda/Searchor/tree/main/examples) folder!

*Note*:&nbsp; Engine names follow the **UpperCamelCase** convention.(eg: ChromeWebStore).

v2.3.0 Changes
--------------
- **[ADDED]** Added CCMixture, Hoogle, and Naver
- **[ADDED]** Added a setup.py to support CLI
-- **[ADDED]** Added CLI, examples are available of the current supported options [here](https://github.com/ArjunSharda/Searchor/blob/main/examples/cli/SUPPORTED_OPTIONS.md)

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
<h6 align="center">© Arjun Sharda 2022 
<br>
All Rights Reserved</h6>
