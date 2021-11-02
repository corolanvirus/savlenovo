import json
import random
import re
import time
from datetime import datetime
from threading import Timer

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
from getpass import getpass
from time import sleep
from selenium.webdriver.support.select import Select

# crée le driver chrome
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://pcsupport.lenovo.com/fr/fr/servicerequest")
sleep(3)
# toujours fidn par le xpath c'est plus precis
search_field = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/input")
search_field.click()
sleep(1)
snfield = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div[2]/div/div/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div/input")
# stocker le sn dans une variable l'appli sera en mode console
snfield.send_keys("PF1KSPCT")
snfield.submit()
sleep(1)
step1 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/button")
step1.click()
sleep(5)
# bug ici
fin_step1 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/button")
fin_step1.click()
# ----------------------------------------------------- STEP ONE DONE voir côté ref dossier indigo
sleep(3)
refdossier = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/input")
refdossier.send_keys("NOREFDOS")
refdossier.submit()
sleep(1)

diag_code = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/input")
diag_code.send_keys("PASDECODEERR")
diag_code.submit()
sleep(1)
description = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div/div/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div/textarea")
description.send_keys(
    "le port usb c ne fonctionne plus, il faut rempalcer la carte mère")
description.submit()
sleep(5)
fin_step2 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/button")
fin_step2.click()
# --------------------------------------------------------- STEP one done voir pour config console stocker infos dans variable user

sleep(3)

username = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/input")
username.send_keys("")

email = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/input")
email.send_keys("")

phone_number = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div/div/input")
phone_number.send_keys("")

sleep(2)

choix_rappel = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[5]/div/div/div/div/div[1]/label[1]/span[2]")
choix_rappel.click()
sleep(2)

langue_rappel1 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/div/div/div")
langue_rappel1.click()


langue_rappel2 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[1]")
langue_rappel2.click()

sleep(2)

geo = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[2]/div/input")
geo.send_keys("  ")
sleep(5)

fin_step3 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/button")
fin_step3.click()

adress = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/input")
adress.send_keys("")
sleep(2)


dept = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div[1]/input")
dept.send_keys("Hauts")
sleep(2)

dept2 = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[107]")
dept2.click()
sleep(2)

city = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/input")
city.send_keys("Puteaux")
sleep(2)

cp = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[3]/div/div[2]/div[4]/div/div/div/div/div/div/div[2]/input")
cp.send_keys("92800")

sleep(2)

contact_sur_site = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/div/input")
contact_sur_site.send_keys("")

sleep(2)
tel_sur_site = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/input")
tel_sur_site.send_keys("")
sleep(5)

fin = browser.find_element_by_xpath(
    "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div/form/button")
fin.click()
