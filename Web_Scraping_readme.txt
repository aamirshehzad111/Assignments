Author: Aamir Shehzad
Description: This a web Scrapping project. 

Language: python
Libraries: Beautifulsoup, pandas, Urllib.

=> Beautifulsoup:
pip install beautifulsoup4.

Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). 
It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
Due to its tree structure scrapping becomes easy.

=> Urllib:
Package is already installed in python you just need to import it. we used it to read html page.

It is a Python module for fetching URLs (Uniform Resource Locators). 
It offers a very simple interface, in the form of the urlopen function.
This is capable of fetching URLs using a variety of different protocols. 
It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on.
These are provided by objects called handlers and openers.

=> Pandas:
pip install pandas. we used it's Dataframe() to create table and then created csv file with the help of pandas.

In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. 
In particular, it offers data structures and operations for manipulating numerical tables and time series. 
It is free software released under the three-clause BSD license


=>Step we follow to create our program for scrapping a web:
1- Go to target url by ob=urlopen(url)
2- Read html page by ob.raad() and then close connection, ob.close(), with help of library urllib
3- Parse html by Beautifulsoup(page, 'html.parser')
4- Remove css if any there, using bs4 extract()
5- Go to bs4, bs4_obj.findAll("body") 
6- Use loop find all the text from container 
7- Put data into list
8- Put above created list into file and done.


--END--