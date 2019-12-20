# COPY PASTE
# - go to a news URL, copy headline and article text
# - paste in google translate and cycle through each language then back to english
# - store each full translation in a new csv file

# TO DO
# - figure out how to best display changing text
# - create system for saving CSV filenames
# - deal with other scripts and missing apostrophes, if necessary
# - get text from sites other than Local 10
# - if miami herald and not logged in, log in
# - call the url_scraper script occassionally (perhaps from within this one) - how many times per day?
# - check robustness of xpath / css stuff


import pyperclip
import time
from datetime import date
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from textwrap import wrap
import csv


driver = webdriver.Chrome("/Users/ericajewell/Downloads/chromedriver")

sources = ["LOCAL_10","MIAMI_HERALD","MIAMI_NEW_TIMES","SFL_TIMES","WLRN"]
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

while True:

# --- GET URL FROM LIST ---

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
				#print(current_url)
				break
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

	# FOR LOCAL 10 ONLY
	list_of_lines = []
	title = driver.find_element_by_tag_name("h1")
	list_of_lines.append(title.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
	#print(title.text.encode("utf-8")) # print in utf for reading in the console
	article_body = driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/section")
	for element in article_body:
		list_of_lines.append(element.text.encode('ascii', 'ignore')) # store text in ascii since it's going back into the browser
		#print(element.text.encode("utf-8")) # print in utf for reading in the console
	original_english_text = "\n" # new line character that will go between each line/element
	original_english_text = original_english_text.join(list_of_lines) 
	# ensure that the text is under 5000 characters. if over 5000, google translate won't accept it
	# problem - this seems to remove line breaks
	if (len(original_english_text)) > 5000:
		correct_word_count = [(original_english_text[i:i+5000]) for i in range(0, len(original_english_text), 5000)] 
		#correct_word_count = wrap(original_english_text, 5000)
		english_text = correct_word_count[0]
	else:
		english_text = original_english_text
	pyperclip.copy(english_text) # copy the text to the clipboard to paste it in GT later
	time.sleep(2)


	# --- GET TRANSLATIONS ---

	current_time = str(datetime.now())
	# create a system to determine which files are created & displayed each day: 
	# write the filename to another table with a column for USED YES/NO that has file names sorted by day.
	# maybe the filename should be the article title
	with open(current_time + ".csv", "w") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Language", "Native Language", "Translated Back to English"]) # column titles
		writer.writerow(["English", english_text, english_text]) # write first english version in columns 1 and 2
		# going to run into problems once other scripts start coming in...
		for key, name in  zip(language_keys, language_names):
			# from english version to new language
			driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=" + key)
			source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
			source_text.send_keys(Keys.SHIFT, Keys.INSERT) # paste, might need to be changed for Linux (CTRL)
			time.sleep(6)
			copy_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[4]/div")
			copy_button.click()
			native_text = pyperclip.paste().encode('ascii', 'ignore')
			if (len(native_text)) > 5000:
				correct_word_count = [(native_text[i:i+5000]) for i in range(0, len(native_text), 5000)] 
				native_text = correct_word_count[0]
				pyperclip.copy(native_text)
			time.sleep(1)
			# from new language back to english
			driver.get("https://translate.google.com/#view=home&op=translate&sl=" + key + "&tl=en")
			source_text = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
			source_text.send_keys(Keys.SHIFT, Keys.INSERT)
			time.sleep(6)
			copy_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[4]/div[4]/div")
			copy_button.click()
			english_text = pyperclip.paste().encode('ascii', 'ignore')
			time.sleep(1)
			writer.writerow([name, native_text, english_text]) # write new row with the language, original text, version translated back into english

	# ensure that the next article will be from a different source
	if current_source != 4:
		current_source += 1
	else:
		current_source = 0
