from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys, re
from getpass import getpass


# To implement the functionality that the domain matches only protonmail. 
emailRegex = re.compile(r'''
    (
        [a-zA-Z0-9._%+-]+     # username
    )
    (    
        @                     # symbol
        [a-zA-Z0-9,-]+        # domain name
        \.[a-zA-Z]{2,4}       # dot-something
    )
''', re.VERBOSE)

protonDomains = ['@proton.me', '@protonmail.com', '@pm.me']

if len(sys.argv) < 3 or sys.argv[1] == "--help" or sys.argv[1] == '-h':
    print("Syntax: commandLineEmailer.py <recipient_email> <login_email>. Login email MUST be protonmail!(@protonmail.com, @pm.me or @proton.me)")

recipientEmailAddress = sys.argv[1]

login = sys.argv[2]
# password = sys.argv[3]

moRecipient = emailRegex.search(recipientEmailAddress)
moLogin = emailRegex.search(login)

if moRecipient == None:
    print('Invalid recipient e-mail address!(1st parameter)')
    exit() 

if moLogin == None:
    print('Invalid login e-mail address!(2nd parameter)')
    exit()

if moLogin.group(2) not in protonDomains:
    print('Login e-mail address MUST be in Protonmail domain!')
    exit()    

# password = input("Enter e-mail password: ")
password = getpass("Enter your e-mail password: ")

browser = webdriver.Firefox()

browser.get('https://account.proton.me/mail')

sleep(2)

loginElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
loginElem.send_keys(login)

passwordElem = browser.find_element(by = By.ID, value = "password")
passwordElem.send_keys(password)



passwordElem.submit()

sleep(3)

newMessageButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button")))
newMessageButton.click()

sleep(1)

recipientEmailAddressField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='To']")))
recipientEmailAddressField.send_keys(recipientEmailAddress)

# subject = browser.find_element(by = By.XPATH, value="input[placeholder='Subject']")
subject = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Subject']")))
subject.send_keys('Future')

iframe = browser.find_elements(By.TAG_NAME, 'iframe')[0]
browser.switch_to.frame(iframe)


messageField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'rooster-editor')))


messageField.clear()


messageField.send_keys('Automating tasks with Python is the future!')

browser.switch_to.default_content() # Leave iframe

# sendButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Send'))) 
sendButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]'))) 



sendButton.click()
