from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import re

driver = webdriver.Chrome('./chromedriver')
driver.get("https://play.esea.net/index.php?s=league&d=bracket&id=7572")
	
driver.implicitly_wait(10)
elements = driver.find_elements_by_class_name('match-games')

score_tuples = []
for element in elements:
    if element.text and element.text != '':
        text = element.text
        regex = r"\D*(\d{1,2})\s*-\s*(\d{1,2})\D*"
        scores = re.findall(regex, text)
        for score in scores:
            score1 = int(score[0])
            score2 = int(score[1])
            score_tuples.append((score1, score2))
            



