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

artists = ["4NOFcRCgjvnRy8nKVGUM0L", # steveruu
                "1NspLfgAsucc39MeTipXNy", # car
                "3GuGHOzPZ0AhH9hK8LqCsK", # pepap
                "2aZD8xH5DKRUwAR6mXAifV", # hakaslakas
                "3xVvsXvpURgj3zeTYiBtCv", # valian
                "2b5QC4KWCMRKdD7LiqvfMQ", # faon
                "50ENuvgRkFZ5hMA0BFEeAM", # helena
                "2qSLwqeQFUHWEzC86u3vRM", # awoken
                "6kEMNp6TPPl70gOicGT0uN", # děcko acid
                "3D57Cu0cu9caAvtl41xUx6", # samzel
                "5QvicxsGxXNicXu1f9guia", # yui paly
                "70Cg3NKGzk0G16trbrfYE5", # maria
                "1HbkAuG6cZndTXlORaQgOq", # ubránek
                "3tjBt96Yk1zS14xc8wldlT", # fembo ypl a
                "5NTcWbyHYQjA20voWilXeG", # kila asky
                "7h22ZneYwwRyOwlgnMd8So", # akarlos
                "5PNDGjJ1e6Tdr8LWmZDqPO", # ne duch
                "0IM0lwjzI0BYaayMweraKT", # matmej
                "34YDbjVGCySBRPAS19xl1L", # paply adomi
                "2IIf5hkbIzh1dqhG1T132E", # krobra08
                "3TTWuZxamiQERzR42VNMS5", # sopka
                "6UIdgISBaIHMOvWwz4nfP1", # prasak
                "569eihmWcdg4HvSPDnjlPn" # ondredaj
                ]

# seed the program with the artists 
seed0 = "/artist/" + artists[0]
seed1 = "/artist/" + artists[1]
seed2 = "/artist/" + artists[2]
seed3 = "/artist/" + artists[3]
seed4 = "/artist/" + artists[4]
seed5 = "/artist/" + artists[5]
seed6 = "/artist/" + artists[6]
seed7 = "/artist/" + artists[7]
seed8 = "/artist/" + artists[8]
seed9 = "/artist/" + artists[9]
seed10 = "/artist/" + artists[10]
seed11 = "/artist/" + artists[11]
seed12 = "/artist/" + artists[12]
seed13 = "/artist/" + artists[13]
seed14 = "/artist/" + artists[14]
seed15 = "/artist/" + artists[15]
seed16 = "/artist/" + artists[16]
seed17 = "/artist/" + artists[17]
seed18 = "/artist/" + artists[18]
seed19 = "/artist/" + artists[19]
seed20 = "/artist/" + artists[20]
seed21 = "/artist/" + artists[21]
seed22 = "/artist/" + artists[22]

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

    # Save response to file
    with open("response.txt", "a") as file:
        file.writelines(html_soup.prettify().encode('utf-8'))
    

    # Append the artistlink to the array for future iterations
    nextLinksToCrawl.append(artistLink)
    return nextLinksToCrawl


# run the main loop
main(seed0)
main(seed1)
main(seed2)
main(seed3)
main(seed4)
main(seed5)
main(seed6)
main(seed7)
main(seed8)
main(seed9)
main(seed10)
main(seed11)
main(seed12)
main(seed13)
main(seed14)
main(seed15)
main(seed16)
main(seed17)
main(seed18)
main(seed19)
main(seed20)
main(seed21)
main(seed22)
driver.quit()