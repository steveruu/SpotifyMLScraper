#stepane nainstaluj pres pip selenium a hod chromedriver do root slozky
from selenium import webdriver

# Python Dependencies
from time import sleep
from random import randint
import re
from bs4 import BeautifulSoup

# Setup Selenium Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)

# Set an initial artist seed, I've used my favorite artist Giuseppe Ottaviani
seed = "/artist/4NOFcRCgjvnRy8nKVGUM0L"


# main will handling the loop and crawling logic
def main(startingArtist):
    artistLinks = [startingArtist]
    alreadySearched = [startingArtist]
    while(len(artistLinks) > 0):
        currentArtist = artistLinks.pop(0)
        additionalLinks = scrapArtist(currentArtist)
        alreadySearched.append(currentArtist)
        for link in additionalLinks:
            if link not in alreadySearched:
                artistLinks.append(link)
        
        #randomly sleep between 1-2 seconds to not abuse the server
        sleep(randint(1,2))

# ScrapArtist will handle logic to parse html and collect data for a particular artist
def scrapArtist(artistLink):
    driver.get("https://open.spotify.com" + artistLink)

    # Scroll the page to generate all content
    SCROLL_PAUSE_TIME = 0.5
    SCROLL_LENGTH = 200
    page_height = int(driver.execute_script("return document.body.scrollHeight"))
    scrollPosition = 0
    while scrollPosition < page_height:
        scrollPosition = scrollPosition + SCROLL_LENGTH
        driver.execute_script("window.scrollTo(0, " + str(scrollPosition) + ");")
        sleep(SCROLL_PAUSE_TIME)

    # Store the page response
    response = driver.find_element_by_class_name('Ydwa1P5GkCggtLlSvphs').get_attribute('innerHTML')
    
    # Initialize the returning array to store artist links on the current page
    nextLinksToCrawl = []

    # Parse the page source to extract information
    html_soup = BeautifulSoup(response, 'html.parser')
    print(html_soup)

    # Append the artistlink to the array for future iterations
    nextLinksToCrawl.append(artistLink)

    return nextLinksToCrawl


# run the main loop
main(seed)
driver.quit()