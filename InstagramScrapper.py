import time
import myLibs
import re
from myLibs import findCommons
from selenium.webdriver import Firefox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def loginInstagram(loginUserName, loginPassword):
    driver = Firefox()

    driver.get("https://www.instagram.com/accounts/login/")

    # Wait element to load to load to find the elements
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//*[@class='_2hvTZ pexuQ zyHYP']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    # Get Username and Password Textboxes
    credentials = driver.find_elements_by_xpath("//*[@class='_2hvTZ pexuQ zyHYP']")

    credentials[0].send_keys(loginUserName)
    credentials[1].send_keys(loginPassword)

    loginButton = driver.find_element_by_xpath(
        "//*[@class='                   Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ']")
    loginButton.click()
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//*[@class='xlTJg']"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    return driver


# Mode --> Followers or Followings
def searchUserFollowersFollowings(searchedUser, mode, driver):
    driver.get("https://www.instagram.com/" + searchedUser)

    if mode.lower() == "followers":
        mode = 1
    elif mode.lower() == "followings":
        mode = 2
    # Get followers or followings, list
    targetList = driver.find_elements_by_xpath("//*[@class='-nal3 ']")[mode]

    # Get number of Followers/Followings
    targetList.click()
    time.sleep(2)
    scrollableFollowers = driver.find_element_by_xpath("//*[@class='isgrP']")
    scrollableFollowers.click()
    numberOfFollowers = int(re.findall(r'\d+', targetList.text.replace(',', '')).pop(0))
    print(numberOfFollowers)
    lst = []

    # Iterate through Follwers/Followings List
    while 1:
        lst = driver.find_elements_by_xpath("//*[@class='FPmhX notranslate  _0imsa ']")
        scrollableFollowers.send_keys(Keys.END)
        print(len(lst))
        if len(lst) >= numberOfFollowers:
            break
    return lst


# Connect to Instagram, Search Users defined in *argv, scrap their followers, Save Them in a File
def getFollowersFrom(loginName, password, *argv):
    browsers = []
    myList = []
    for arg in argv:
        browsers.append(loginInstagram(loginName, password))
    for i, browser in enumerate(browsers):
        myList.append(searchUserFollowersFollowings(argv[i], "followers", browser))
    for i, list in enumerate(myList):
        myLibs.writeListToFile(list, argv[i] + "_" + "followers")


#------------------------------------------------------------------------------------


