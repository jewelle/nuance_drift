# COPY PASTE
# - go to a news URL, copy text, and then go to google translate and paste

# TO DO
# - if miami herald and not logged in, log in
# - cycle appropriately through languages on google translate
# - save resulting text
# - figure out how to best display changing text
# - get text from sites other than Local 10
# - call the url_scraper script occassionally (perhaps from within this one)
# - how many times per day should this be updated?
# - check robustness of xpath / css stuff

import time
from datetime import date
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv


driver = webdriver.Chrome("/Users/ericajewell/Downloads/chromedriver")

sources = ["LOCAL_10","MIAMI_HERALD","MIAMI_NEW_TIMES","SFL_TIMES","WLRN"]
current_source = 0
today = str(date.today())

# --- GET URL FROM LIST ---

# check whether YES has already been selected
# get a new url to use
with open("urls.csv", "r+") as csvfile:
	reader = csv.reader(csvfile)
	date = next(reader) # skip first row which contains the date
	headings = next(reader) # skip second row with column headings
	for row in reader:
		used = row[1]
		source = row[2]
		current_url = row[3]
		if sources[current_source] in source and used == "NO": # match source and not yet used
			print(current_url)
			break
# overwrite the list of urls to change the current url used column from NO to YES
"""
csv_overwrite = list() # list to store data for the overwritten CSV file
with open("urls.csv", "r") as csvfile:
	csv_overwrite.append([today])
	reader = csv.reader(csvfile)
	date = next(reader) # skip first row which contains the date
	for row in reader:
		num = row[0]
		used = row[1]
		source = row[2]
		url = row[3]
		if url == current_url:
			# change used to yes and append
			csv_overwrite.append([num, "YES", source, url])
		else:
			csv_overwrite.append(row)
with open("urls.csv", "w") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(csv_overwrite)
"""
# need to ensure somehow that the file isn't being overwritten at the same time that this is running
# maybe this will get and store all the translations for one article
# and then while they are being displayed it can make it ok to update the URL file



# --- GET TEXT FROM ARTICLE ---

driver.get(current_url)

# FOR LOCAL 10 ONLY
list_of_lines = []
title = driver.find_element_by_tag_name("h1")
list_of_lines.append(title.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
print(title.text.encode("utf-8")) # print in utf for reading in the console
article_body = driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/section")
for element in article_body:
	list_of_lines.append(element.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
	print(element.text.encode("utf-8")) # print in utf for reading in the console
	#encoded_line = element.text.encode("utf8")
	#list_of_lines.append(encoded_line)
# count characters, if over 5000, it won't work
translated_text = "\n" # new line character that will go between each line/element
translated_text = translated_text.join(list_of_lines) 

"""
article_text = driver.find_elements_by_tag_name("p")
print(article_body.text.encode("utf8"))
for line in article_text:
	encoded_line = line.text.encode("utf8")
	if encoded_line == " ":
		break
	list_of_lines.append(encoded_line)
	print(encoded_line)
"""
time.sleep(2)


# --- GET TRANSLATIONS ---

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
with open(source + now + ".csv", "w") as csvfile:
	# need to fix this, maybe have to do .text
#with open(source + "-" + date + "-" + current_time + ".csv", "w") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["ENG - ENG", translated_text, translated_text]) # write first english version in column 1, first english version in column 2
	driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=eo")
	source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
	source_text.send_keys(translated_text)
	#for line in list_of_lines:
	#	source_text.send_keys(line)
	time.sleep(2)
	copy_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[4]/div")
	copy_button.click()
	time.sleep(2)
	driver.get("https://translate.google.com/#view=home&op=translate&sl=eo&tl=et")
	source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
	time.sleep(2)
	source_text.send_keys(Keys.SHIFT, Keys.INSERT) #paste, might need to be changed for Linux (CTRL)

# ensure that the next article will be from a different source
if current_source != 4:
	current_source += 1
else:
	current_source = 0
