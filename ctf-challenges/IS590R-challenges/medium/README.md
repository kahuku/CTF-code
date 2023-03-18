Challenge name: World Wide Web
Challenge category: Web
Challenge description: The internet is just a network of interconnected pages! [link to www.html]
Challenge flag: byu22ind{flaggy_flag_flag}
Hint: Web scrapers can find all of the links on a page very quickly
Setup instructions: Unzip and place www.html and the challenge folder on a public facing web server
Walk through of how to solve: Each page is linked to the next page through one of the random <a> tags on the previous page. On the final page in the chain is the flag. Since there are so many pages, use Python's BeautifulSoup and requests libraries to follow the links (only one href on each page) until the end of the chain.