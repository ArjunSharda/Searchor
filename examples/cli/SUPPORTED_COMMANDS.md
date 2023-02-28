# Supported Commands

This is a list of all the official supported CLI options of Searchor, with an example of them being used.

# search ✅
```shell
$ searchor search Yahoo "Hello World!"

```
Returns the search query URL for a designated search engine.

# search:copy_url ✅
```shell
$ searchor search Google "Hello World!" --copy
```
A option to copy the URL to your browser, as a addon option to the search command.
# search:open_web ✅ 

```shell
$ searchor search Target "Hello World!" --open
```
Opens the search query URL in your browser, as a addon option to the search command.

# history ✅
```shell
$ searchor history
```
Gets your history of the CLI commands that you have used with the `search` command. Only applies to the `search` command.

# history:clear ✅
```shell
$ searchor history --clear
```
Clears your history of the CLI commands that you have used with the `search` command. Only applies to the `search` command.


# getinfo ✅
```shell
$ searchor getinfo Football
```
Gets the information about a topic.


# webscrape ✅

```shell
$ searchor webscrape https://google.com/
```

Web scrapes the given URL.
