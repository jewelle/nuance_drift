# COPY PASTE
# - get URLs for news articles
# - go to a news URL, copy headline and article text
# - paste in google translate and cycle through each language then back to english
# - store each full translation in a new csv file

import pyperclip
import time
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
import csv


driver = webdriver.Chrome("/Users/ericajewell/Downloads/chromedriver")
sources = ["WLRN", "LOCAL_10", "SFL_TIMES", "MIAMI_HERALD"]
language_keys = [
	"eo","et","tl","fi","fr","fy",
	"gl","ka","de","el","gu","ht","ha",
	"haw","iw","hi","hmn","hu","is","ig",
	"id","ga","it","ja","jw","kn","kk",
	"km","ko","ku","ky","lo","la","lv",
	"lt","lb","mk","mg","ms","ml","mt",
	"mi","mr","mn","my","ne","no","ps",
	"fa","pl","pt","pa","ro","ru","sm",
	"gd","sr","st","sn","sd","si","sk",
	"sl","so","es","su","sw","sv","tg",
	"ta","te","th","tr","uk","ur","uz",
	"vi","cy","xh","yi","yo","zu","af",
	"sq","am","ar","hy","az","eu","be",
	"bn","bs","bg","ca","ceb","ny","zh-CN",
	"co","hr","cs","da","nl"
	]
language_names = [
	"Esperanto","Estonian","Filipino","Finnish","French","Frisian",
	"Galician","Georgian","German","Greek","Gujarati","Haitian Creole","Hausa",
	"Hawaiian","Hebrew","Hindi","Hmong","Hungarian","Icelandic","Igbo",
	"Indonesian","Irish","Italian","Japanese","Javanese","Kannada","Kazakh",
	"Khmer","Korean","Kurdish","Kyrgyz","Lao","Latin","Latvian",
	"Lithuanian","Luxembourgish","Macedonian","Malagasy","Malay","Malayalam","Maltese",
	"Maori","Marathi","Mongolian","Myanmar","Nepali","Norwegian","Pashto",
	"Persian","Polish","Portuguese","Punjabi","Romanian","Russian","Samoan",
	"Scots Gaelic","Serbian","Sesotho","Shona","Sindhi","Sinhala","Slovak",
	"Slovenian","Somali","Spanish","Sudanese","Swahili","Swedish","Tajik",
	"Tamil","Telugu","Thai","Turkish","Ukranian","Urdu","Uzbek",
	"Vietnamese","Welsh","Xhosa","Yiddish","Yoruba","Zulu","Afrikaans",
	"Albanian","Amharic","Arabic","Armenian","Azerbaijani","Basque","Belarusian",
	"Bengali","Bosnian","Bulgarian","Catalan","Cebuano","Chichewa","Chinese",
	"Corsican","Croatian","Czech","Danish","Dutch"
	]

current_source = 0
today = str(date.today())

# check whether the master CSV file of the day exists
# for this version, just using a single file rather than 
# rewriting every day since it's only up for 2 days
try:
    with open("article_titles.csv", "r") as csvfile:
    #with open(today + ".csv", "r") as csvfile:
		print("file exists")
except IOError: # if there"s no file, create one
    with open("article_titles.csv", "w") as csvfile:
    #with open(today + ".csv", "w") as csvfile:
    	writer = csv.writer(csvfile)
    	writer.writerow(["USED", "FILENAME"])
    	print("creating new file")

def scrape_urls():
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
	"""
	if today not in date: # if this is a new day, erase old data
			print("not in date")
			with open("urls.csv", "w") as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow([today])
				writer.writerow(["NUM", "USED", "SOURCE", "URL"])
	"""
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
		if "watch-local-10-news-live" not in url and "https://www.local10.com/news/local/" in url: 
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

#scrape_urls()

while True:

# --- GET URL FROM LIST ---

	# get a new url to use
	with open("urls.csv", "r+") as csvfile:
		source_available = False
		reader = csv.reader(csvfile)
		date = next(reader) # skip first row which contains the date
		headings = next(reader) # skip second row with column headings
		for row in reader:
			used = row[1]
			source = row[2]
			current_url = row[3]
			if sources[current_source] in source and used == "NO": # match source and not yet used
				source_available = True
				break
		if source_available == False:
			scrape_urls()
			# if no more urls available... do URL scraper again
			# might be a problem because then we use the same current_url as previous?

	# overwrite the list of urls to change the current url used column from NO to YES
	csv_overwrite = list() # list to store data for the overwritten CSV file
	with open("urls.csv", "r") as csvfile:
		csv_overwrite.append([today])
		reader = csv.reader(csvfile)
		date = next(reader) # skip first row which contains the date because it only has 1 column
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
	# need to ensure that the file isn't being overwritten at the same time that this is running


# --- GET TEXT FROM ARTICLE ---

	driver.get(current_url)
	time.sleep(2)
	list_of_lines = []
	# WLRN
	if (current_source == 0): 
		title = driver.find_element_by_tag_name("h1").text.encode('ascii', 'ignore')
		list_of_lines.append(title)#.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
		article_body = driver.find_elements_by_tag_name("p")
		for element in article_body:
			list_of_lines.append(element.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
	
	# LOCAL 10
	if (current_source == 1): 
		title = driver.find_element_by_tag_name("h1").text.encode('ascii', 'ignore')
		list_of_lines.append(title)#.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
		article_body = driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/section")
		for element in article_body:
			list_of_lines.append(element.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser

	# SFL TIMES
	if (current_source == 2): 
		title = driver.find_element_by_tag_name("h1").text.encode('ascii', 'ignore')
		list_of_lines.append(title)#.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
		article_body = driver.find_elements_by_tag_name("p")
		for element in article_body:
			if ("You must be logged in" in element.text):
				break
			if ("PHOTO COURTESY OF" not in element.text):
				list_of_lines.append(element.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser

	#if (current_source == 3): # MIAMI HERALD
		# check if logged in
	
	original_english_text = "\n" # new line character that will go between each line/element
	original_english_text = original_english_text.join(list_of_lines) 
	# ensure that the text is well under 5000 characters. if over 5000, google translate won't accept it
	if (len(original_english_text)) > 4900:
		correct_word_count = [(original_english_text[i:i+4900]) for i in range(0, len(original_english_text), 4900)] 
		english_text = correct_word_count[0]
	else:
		english_text = original_english_text
		if ('\"' in english_text):
			english_text = english_text.replace ('\"', '')
	pyperclip.copy(english_text) # copy the text to the clipboard to paste it in GT later
	time.sleep(2)

# --- GET TRANSLATIONS ---

	with open("/Users/ericajewell/Downloads/NUANCE-DRIFT/articles/" + title + ".csv", "w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Language", "Native Language", "Translated Back to English"]) # column titles
		writer.writerow(["English", english_text, english_text]) # write first english version in columns 1 and 2
		# going to run into problems once other scripts start coming in...
		for key, name in  zip(language_keys, language_names):
			# from english version to new language
			driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=" + key)
			source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
			source_text.send_keys(Keys.SHIFT, Keys.INSERT) # paste, might need to be changed for Linux (CTRL)
			time.sleep(3)
			copy_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[4]/div")
			try:
				copy_button.click()
			except ElementClickInterceptedException:
				print("ElementClickInterceptedException")
				driver.execute_script("arguments[0].click();", copy_button)
			native_text_utf = pyperclip.paste().encode('utf-8')
			native_text_ascii = pyperclip.paste().encode('ascii', 'ignore')
			if (len(native_text_ascii)) > 4900:
				correct_word_count = [(native_text_ascii[i:i+4900]) for i in range(0, len(native_text_ascii), 4900)] 
				native_text_ascii = correct_word_count[0]
			if (len(native_text_utf)) > 4900:
				correct_word_count = [(native_text_utf[i:i+4900]) for i in range(0, len(native_text_utf), 4900)] 
				native_text_utf = correct_word_count[0]
			# remove quotes
			if ('\"' in native_text_ascii):
				native_text_ascii = native_text_ascii.replace ('\"', '')
				pyperclip.copy(native_text_ascii)
			if ('\"' in native_text_utf):
				native_text_utf = native_text_utf.replace ('\"', '')
				#pyperclip.copy(native_text_utf)
			time.sleep(1)
			# from new language back to english
			driver.get("https://translate.google.com/#view=home&op=translate&sl=" + key + "&tl=en")
			source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
			source_text.send_keys(Keys.SHIFT, Keys.INSERT)
			time.sleep(3)
			copy_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[4]/div")
			try:
				copy_button.click()
			except ElementClickInterceptedException:
				print("ElementClickInterceptedException")
				driver.execute_script("arguments[0].click();", copy_button)
			# might need to make this Ascii because weird things sometimes happen
			#english_text = pyperclip.paste().encode('ascii', 'ignore')
			english_text_ascii = pyperclip.paste().encode('ascii', 'ignore')
			english_text_utf = pyperclip.paste().encode('utf-8')
			if ('\"' in english_text_ascii):
				english_text_ascii = english_text_ascii.replace ('\"', '')
				pyperclip.copy(english_text_ascii)
			if ('\"' in english_text_utf):
				english_text_utf = english_text_utf.replace ('\"', '')
			time.sleep(1)
			# write new row with the language, original text, version translated back into english
			writer.writerow([name, native_text_utf, english_text_utf])

	# only add this file to the list of files only once it's done
	csv_overwrite = list() # list to store data for the overwritten CSV file
	# title should be day
	with open("article_titles.csv", "r") as csvfile:
	#with open(today + ".csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			csv_overwrite.append(row)
		csv_overwrite.append(["NO", title + ".csv"])
	with open("article_titles.csv", "w") as writeFile:
	#with open(today + ".csv", "w") as writeFile:
	    writer = csv.writer(writeFile)
	    writer.writerows(csv_overwrite)
	
	# ensure that the next article will be from a different source
	if current_source != 2: #if current_source != 4:
		current_source += 1
	else:
		current_source = 0
