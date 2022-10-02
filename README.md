Searchor
========
![PyPI](https://img.shields.io/pypi/v/searchor?color=green&logo=python&logoColor=green)
<div style="text-align: center; display: grid; justify-content: center;"><img style="margin: auto; margin-bottom: 1rem; border-radius: 30%;" height="150" width="150" src="./ext/searchor.png"/></div>

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
>>> from searchor import search, Engine
>>> search("Hello, World!", Engine.Google)
'https://www.google.com/search?q=Hello%2C%20World%21'
```

*Note*:&nbsp; Engine names follow the **UpperCamelCase** convention.(eg: ChromeWebStore).

Take a look at more examples in the [examples](https://github.com/ArjunSharda/Searchor/tree/main/examples) folder!

v2.1.5 Changes
--------------
- **[BREAKING]** Fixed typo in Atlassian and Lycos


Migration
---------
Instead of different functions for each engine, Searchor `v2.0.0` uses a single function with an `Engine` enum. This makes it easier to use and maintain. If you're migrating from `v1.0.0`, compare the differences between the following snippets:
```python
# Searchor v1.0.0
import Searchor
Searchor.SearchGoogle("Hello, World!")
```
```python
# Searchor v2.0.0
from searchor import search, Engine
search("Hello, World!", Engine.Google)
```

Custom Engine
-------------
Single Use 
```python
from searchor import search
search("Hello, World!", "https://example.com/search/{query}")
```
Multiple Use
```python
from searchor import search, Engine
Engine.MySite = "https://example.com/search/{query}"
search("Hello, World!", Engine.MySite)
search("Hello Again!", Engine.MySite)
```

View Engine list
-------------
```python
from searchor import engine_list
print(engine_list())
```
