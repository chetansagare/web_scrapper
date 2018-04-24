
#import libraries 
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#specify the url 
quotes_page = 'http://wisdomquotes.com/short-quotes/'
page = urllib2.urlopen(quotes_page)
# parse the html using beautiful soup and store in variable `soup`
soup=BeautifulSoup(page,'html.parser')

quote=soup.find('div','center-block entry-content')

count=1

for child in quote.children:
    try:
        quote_text=child.text
        count=count+1
        if quote_text == "Go to table of contents" :
            quote_text="\n\n\n"
        with open("wisdomquotes.txt","a") as quotefile:
            quotefile.write(quote_text)
            quotefile.write("\n")
    except:
        print(count) 
    
print(count)


#print(quotes_text)

# open a csv file with append, so old data will not be erased
#with open('index.csv', 'a') as csv_file:
# writer = csv.writer(csv_file)
#writer.writerow([name, price, datetime.now()])

#with open("wisdomquotes.txt","a") as quotefile:
#       quotefile.write(quote_text)
#        quotefile.write("\n")