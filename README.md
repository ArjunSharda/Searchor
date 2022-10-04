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
>>> from searchor import Engine
>>> Engine.Google.search("Hello, World!")
'https://www.google.com/search?q=Hello%2C%20World%21'
```

Take a look at more examples in the [examples](https://github.com/ArjunSharda/Searchor/tree/main/examples) folder!

*Note*:&nbsp; Engine names follow the **UpperCamelCase** convention.(eg: ChromeWebStore).

v2.2.0 Changes
--------------
- **[BREAKING]** Engine class is now subclassed as an enumerator
- **[BREAKING]** Removed engine_list
- **[BREAKING]** Changed search function to be inside the Engine class
- **[ADDED]** Added a additional_queries parameter in the search function
- **[ADDED]** Added a `open_web` parameter in the search function which is default set to `False` and can be made `True` to open a URL with Searchor in a new window with your default browser.


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

