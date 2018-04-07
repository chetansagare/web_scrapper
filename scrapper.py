
#import libraries 
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


#specify the url 
tnp_notifications = 'https://tnp.iitd.ac.in/notices/training/notify.php'
page = urllib2.urlopen(tnp_notifications)

# parse the html using beautiful soup and store in variable `soup`

soup=BeautifulSoup(page,'html.parser')

central_notifications = soup.find('div', attrs={'id': 1})
new_data = central_notifications.text.strip() # strip() is used to remove starting and trailing

placement_schedule = soup.find('div', attrs={'id':2})
new_data = new_data+placement_schedule.text

company_visit = soup.find('div',attrs={'id':3})
new_data = new_data+company_visit.text

shortlist_list = soup.find('div',attrs={'id':4})
new_data = new_data+shortlist_list.text

downloads_data = soup.find('div',attrs={'id':5})
new_data = new_data+downloads_data.text

deadlines_data = soup.find('div',attrs={'id':6})
new_data = new_data+deadlines_data.text

with open('tnp_notifications.txt','r') as file : 
    old_data = file.read()
    
if new_data == old_data :
    print "No Change In Page"
else:
    print "Change In Page"
    print len(new_data)
    print len(old_data)
    #print [i for i in xrange(len(new_data)) if new_data[i] != old_data[i]]
    with open('tnp_notifications.txt','w+') as file :
        file.write(new_data)

# open a csv file with append, so old data will not be erased
#with open('index.csv', 'a') as csv_file:
# writer = csv.writer(csv_file)
#writer.writerow([name, price, datetime.now()])