import pymysql
import urllib.request
# import selenium.webdriver as webdriver
# import requests
import re
import random
# from robobrowser import RoboBrowser
import datetime
import csv

############### CONFIGURE THIS ###################
# Open database connection
db = pymysql.connect("localhost","root","","seo-tracking-tool")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# -----------------------------------------------------------

# agent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0',
#          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#          'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
#          'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0']
#
# parser = 'html.parser'
#
# browser = RoboBrowser(history=False,
#                       user_agent=random.choice(agent),
#                       parser=parser)


#############################################################################################################################




            # linenum += 1
            # if pattern.search(line) != None:
            #     urlss.append((linenum, line.rstrip('\n')))
    # for err in urlss:
    #     print("Line " + str(err[0]) + ": " + err[1])
    #
    # # Returns all instances of urls between the start and end paramaters in data.txt



#############################################################################################################################

def find(start, end):
   # Needs to append the every instance of all urls between the start and end inputs in data.txt

   # linenum = 0
   # pattern = re.compile("www.random.org", re.IGNORECASE)
   urlss = []
   mylines = []

   with open('data.txt', 'rt') as myfile:
       for line in myfile:
           mylines.append(line.rstrip('\n'))
           regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
           for ln in mylines:
               matches = re.findall(regex, ln)
               urlss.append(matches)

   # d = []
   # counter = 0
   # for i in collected_data:
   #     counter += 1
   #     if urls in str(i):
   #         url = i.find_all('a', href=True)
   #         position = "%d" % (counter)
   #         rank = "%s" % (url[0]['href'])
   #         now = datetime.date.today().strftime("%d-%m-%Y")
   #         terms = 'terms'
   #         d.append(terms)
   #         d.append(position)
   #         d.append(rank)
   #         d.append(now)
   #         print(terms, position, rank, now)

   return urlss[0]

# def get_index(strings, substr):
#     for idx, string in enumerate(strings):
#         if substr in string:
#             break
#     return idx




# Prepare SQL query to READ a record into the database.
sql = "SELECT `url`, `terms` FROM `site` LEFT JOIN `keywords` ON `site`.`url-ID` = `keywords`.`terms-ID`"

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows
results = cursor.fetchall()
for rowU in results:
   urls = rowU[0]
   terms = rowU[1]
   # Now print fetched result
   # print ("URLs = {0} | Keywords = {1}".format(terms,urls))
   # print('-------------------------------------')
   # Prepare SQL query to READ a record into the database.
   # sql = "SELECT terms FROM keywords"
   #
   # # Execute the SQL command
   # cursor.execute(sql)
   #
   # # Fetch all the rows
   # results = cursor.fetchall()
   # for row in results:
   #     terms = row[0]
   #     # Now print fetched result
   #     # print ("URLs = {0} | Keywords = {1}".format(terms,urls))
   #     # import webbrowser
   #
   #     # new = 2
   #     # tabUrl = "https://www.google.com/search?q="
   #     # webbrowser.open(tabUrl + terms)
   #     # Creates the url with the query
   query = terms
   query = query.replace(", ", "&")
   url = 'https://www.google.com/search?q=' + query

   # Gets past googles attempt to block parsing

   headers = {}
   headers[
       'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

   # Fetches data

   req = urllib.request.Request(url, headers=headers)
   resp = urllib.request.urlopen(req)
   respData = resp.read()

   # Saves the source code in a txt file

   saveFile = open('data.txt', 'w')
   saveFile.write(str(respData))
   saveFile.close()

   # Finds the urls and returns them


   urlsFinded = find('<h3 class="r"><a href="', '"')
   print(urlsFinded)

   collected_data = []
   try:
       print('\n')
       print('  ::  Index of the URL: ', urls, ' in this search query : ', urlsFinded.index(urls))
       print('\n')
       collected_data.append(urls)
       collected_data.append(urlsFinded.index(urls))
       now = datetime.date.today().strftime("%d-%m-%Y")
       print('  :: Date:  ' + now)

       collected_data.append(now)
       print('\n')
       print(collected_data)
   except ValueError as e:
       print('  ::  Error msg : ', urls+' is not found in this search query ! ')


   file = datetime.date.today().strftime("%d-%m-%Y") + '-' + '.csv'
   with open(file, 'w') as f:
       writer = csv.writer(f)
       writer.writerow(['URL', 'Rank', 'Date', 'Keyword'])
       writer.writerows(zip(collected_data[0::3], collected_data[1::3], collected_data[2::3], collected_data[3::3]))


   # browser.open('https://www.google.com/search?num=100&q=' + terms)
   # page = requests.get("http://www.google.com/search?q=" + terms).text
   # url = "https://www.startpage.com"
   # # PhantomJS(executable_path='C:/PhantomJs/bin/phantomjs/phantomjs.exe')
   # browser = webdriver.PhantomJS(executable_path='C:/PhantomJs/bin/phantomjs/phantomjs.exe')
   # browser.get(url)
   # search_box = browser.find_element_by_id("query")
   # search_box.send_keys(terms)
   # search_box.submit()
   # try:
   #     links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
   # except:
   #     links = browser.find_elements_by_xpath("//h3//a")
   # results = []
   # for link in links:
   #     href = link.get_attribute("href")
   #     print(href)
   #     results.append(href)
   # browser.close()
   # print("URLs = {0}".format(urls))
   print("Keywords = {0}".format(terms))
   print('\n-----------------------------------------------------------------------------------------------------------\n')




# import webbrowser, requests, sys, bs4
# res = requests.get('https://google.com/search?q='+''.join(terms))
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# linkElements = soup.select('.r a')
# if linkElements == urls:
#    linkToOpen = min(5, len(linkElements))
# else:
#    print('**** URLs is not Found. ****')
#    exit()
# for i in range(linkToOpen):
#    webbrowser.open('https://google.com'+linkElements[i].get('href'))


# ############# DISCONNECT FROM SERVER.
db.close()