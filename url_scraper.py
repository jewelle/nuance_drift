# URL SCRAPER
# - checks whether the current file is from yesterday
# - if so, make a new file and gather URLs from news sources
# - if not, search news sources and append any new URLS to file

# TO DO
# - refresh every hour to gather new articles
# - add test for when a page doesn"t load within a certain time?

import time
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv

today = str(date.today()) # get the date to check whether a new file should be createdtoday = str(date.today()) # get the date to check whether a new file should be created
date = today
try: # check whether the file exists
    with open("urls.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		date = next(reader) # the date is stored in the first line of the file
		if today in date:
			print("same date")
except IOError: # if there"s no file, create one
    with open("urls.csv", "w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([today]) # add time
		writer.writerow(["NUM", "USED", "SOURCE", "URL"])
		print("creating new file")
if today not in date: # if this is a new day, erase old data
		print("not in date")
		with open("urls.csv", "w") as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([today])
			writer.writerow(["NUM", "USED", "SOURCE", "URL"])

driver = webdriver.Chrome("/Users/ericajewell/Downloads/chromedriver")

num_of_rows = 0
with open("urls.csv", "r") as csvfile:
   	for line in csvfile: num_of_rows+=1
num_of_urls = num_of_rows-2

# - Local 10
driver.get("https://www.local10.com/")
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
	url = elem.get_attribute("href")
	if "watch-local-10-news-live" not in url:
		if "https://www.local10.com/news/2" in url or "https://www.local10.com/news/politics/2" in url or "https://www.local10.com/entertainment/2" in url or "https://www.local10.com/health/2" in url: 
			# open csv file to read and check whether the url is already there
			in_file_already = False
			with open("urls.csv", "r") as csvfile:
	   			for line in csvfile:
	   				# if the url matches the line
	   				if url in line:
	   					in_file_already = True
			if in_file_already == False:
				num_of_urls+=1	
				with open("urls.csv", "a") as csvfile:
	   				writer = csv.writer(csvfile)
					writer.writerow([num_of_urls, "NO", "LOCAL_10", url])

# - Miami Herald
driver.get("https://www.miamiherald.com/")
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
	full_url = elem.get_attribute("href")
	if "article" in full_url and "https://www.miamiherald.com/" in full_url:
		# remove everything after hashtag
		url, sep, junk = full_url.rpartition("#")
		# open csv file to read and check whether the url is already there
		in_file_already = False
		with open("urls.csv", "r") as csvfile:
   			for line in csvfile:
   				# if the url matches the line
   				if url in line: 
   					in_file_already = True
		if in_file_already == False:	
			num_of_urls+=1
			with open("urls.csv", "a") as csvfile:
   				writer = csv.writer(csvfile)
				writer.writerow([num_of_urls, "NO", "MIAMI_HERALD", url])

# - Miami New Times
driver.get("https://www.miaminewtimes.com/")
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
	url = elem.get_attribute("href")
	if "https://www.miaminewtimes.com/news/" in url:
		in_file_already = False
		with open("urls.csv", "r") as csvfile:
   			for line in csvfile:
   				# if the url matches the line
   				if url in line: 
   					in_file_already = True
		if in_file_already == False:
			num_of_urls+=1	
			with open("urls.csv", "a") as csvfile:
   				writer = csv.writer(csvfile)
				writer.writerow([num_of_urls, "NO", "MIAMI_NEW_TIMES", url])

# - South Florida Times
driver.get("http://www.sfltimes.com/")
time.sleep(2)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
	url = elem.get_attribute("href")
	if "http://www.sfltimes.com/news/" in url or "http://www.sfltimes.com/finance/" in url or "http://www.sfltimes.com/education/" in url or "http://www.sfltimes.com/sports/" in url:
		in_file_already = False
		with open("urls.csv", "r") as csvfile:
   			for line in csvfile:
   				# if the url matches the line
   				if url in line: 
   					in_file_already = True
		if in_file_already == False:	
			num_of_urls+=1
			with open("urls.csv", "a") as csvfile:
   				writer = csv.writer(csvfile)
				writer.writerow([num_of_urls, "NO", "SFL_TIMES", url])
	
# - WLRN
driver.get("https://www.wlrn.org/term/local-news/")
time.sleep(5)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
	url = elem.get_attribute("href")
	if "https://www.wlrn.org/post/" in url:
		in_file_already = False
		with open("urls.csv", "r") as csvfile:
   			for line in csvfile:
   				# if the url matches the line
   				if url in line: 
   					in_file_already = True
		if in_file_already == False:	
			num_of_urls+=1
			with open("urls.csv", "a") as csvfile:
   				writer = csv.writer(csvfile)
				writer.writerow([num_of_urls, "NO", "WLRN", url])

print(num_of_urls)