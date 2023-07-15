'''

##  Web Scraping by using Regular Expressions :

-> the process of collecting information from web pages is called web scraping. 
-> in web scraping to match our required patterns like mail ids, mobile numbers 
	we can use regular expressions.

=> to open url first and send request, we require special module => urllib

'''

import re, urllib
import urllib.request

sites = ['http://google.com', 'http://rediff.com']
for s in sites :
	print('searching...', s)
	u = urllib.request.urlopen(s)
	text = u.read()
#	print(text)   =>> complete html page of site
	title = re.findall('<title>.*</title>', str(text), re.IGNORECASE)
	print(title[0])


'''  output =>

searching... http://google.com
<title>Google</title>
searching... http://rediff.com
<title>Rediff.com: News | Rediffmail | Stock Quotes | Shopping</title>

'''