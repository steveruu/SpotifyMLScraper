#stepane nainstaluj pres pip selenium a hod chromedriver do root slozky
from selenium import webdriver

# Python Dependencies
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import date

# Setup Selenium Chrome Driver
browser_locale = 'en-US'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--lang={}".format(browser_locale))

driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)

# Set up artists and their IDs
artists = [
                "3GuGHOzPZ0AhH9hK8LqCsK", # pepap
                "1NspLfgAsucc39MeTipXNy", # car
                "5VW7PyWYrxkuWlzSxic7N2", # hakaslakas
                "4NOFcRCgjvnRy8nKVGUM0L", # steveruu
                "3xVvsXvpURgj3zeTYiBtCv", # valian
                "6kEMNp6TPPl70gOicGT0uN", # děcko acid
                "50ENuvgRkFZ5hMA0BFEeAM", # helena
                "2qSLwqeQFUHWEzC86u3vRM", # awoken
                "2HJYEBrWgHX2MtQng48uSw", # gmane
                "2b5QC4KWCMRKdD7LiqvfMQ", # faon
                
                
                
                "3D57Cu0cu9caAvtl41xUx6", # samzel
                "5NTcWbyHYQjA20voWilXeG", # kila asky
                "0cpiDjS2bR8rWA8JLhU2uM", # givert
                "7h22ZneYwwRyOwlgnMd8So", # akarlos
                
                "1HbkAuG6cZndTXlORaQgOq", # ubránek
                "5QvicxsGxXNicXu1f9guia", # yui paly
                
                
                "3tjBt96Yk1zS14xc8wldlT", # fembo ypl a
                "02pls7VjPaXvSbarvDUW7p", # maros2
                "34YDbjVGCySBRPAS19xl1L", # paypal adomi
                "1tqkzvbam2vnrUdredtErd", # shitlord
                
                
                "5PNDGjJ1e6Tdr8LWmZDqPO", # ne duch
                "2GaadbJKN8S8PbST0XwwQD", # xfgin
                "0IM0lwjzI0BYaayMweraKT", # matmej                                                
                "2IIf5hkbIzh1dqhG1T132E", # krobra08
                "3TTWuZxamiQERzR42VNMS5", # sopka
                "6JHPfVpbSjecbv3oAOJSov", # filip benes                           
                "1hRLNOS6wPhSMLfXVaJk5t", # akuda
                "6UIdgISBaIHMOvWwz4nfP1", # prasak
                "569eihmWcdg4HvSPDnjlPn", # ondredaj
                "30ZlxBZfVVt67x1giU0xa4", # hakalas

                ]

# Set the artist seeds
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
seed23 = "/artist/" + artists[23]
seed24 = "/artist/" +  artists[24]
seed25 = "/artist/" + artists[25]
seed26 = "/artist/" + artists[26]
seed27 = "/artist/" + artists[27]
seed28 = "/artist/" + artists[28]
seed29 = "/artist/" + artists[29]

# main() will handle the loop and crawling logic
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

# scrapArtist() will handle logic to parse html and collect data for a particular artist
def scrapArtist(artistLink):
    driver.get("https://open.spotify.com" + artistLink)

    # scroll the page to generate all content
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
    response2 = driver.find_element_by_class_name('rEN7ncpaUeSGL9z0NGQR').get_attribute('innerHTML').replace('</h1>','')[146:200].replace('">','').replace('0%; font-size:','').replace('6rem','').replace('4.5rem','').replace('3rem','').replace('2rem','').replace(';','')
    if response2 == "COBRA 808":
        response2 = "COBRA_808"
    if response2 == "sađz":
        response2 = "sadz"

    # initialize the returning array to store artist links on the current page
    nextLinksToCrawl = []

    # parse the page source to extract information
    html_soup = BeautifulSoup(response, 'html.parser')
    fullres = html_soup.prettify().replace(',',' ').replace('monthly listeners','')
    print(fullres)
    
    # czech grammar
    if (int(fullres.strip('\r\n').replace(' ','')) == 1):
        ml = "posluchač měsíčně"
    elif (int(fullres.strip('\r\n').replace(' ','')) <= 4):
        ml = "posluchači měsíčně"
    else:
        ml = "posluchačů měsíčně"

    # send data to webhook
    webhookContent = (response2 + " – " + "**" + fullres.strip('\r\n') + "**" + ml)

    # Save response to file
    with open("response.txt", "a") as file:
        file.write(webhookContent)

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1046402781696753715/DuBZxciO1pTDRHq3FnEa2EYsMjI1flapP5wsw_VTDNxUh05TPOPZA2TxJnkZJak8taQy', username="cyrex real", content=webhookContent)
    response = webhook.execute() 
    
    # Append the artistlink to the array for future iterations
    nextLinksToCrawl.append(artistLink)
    return nextLinksToCrawl
   
# run the main loop for each artist
webhook2 = DiscordWebhook(url='https://discord.com/api/webhooks/1046402781696753715/DuBZxciO1pTDRHq3FnEa2EYsMjI1flapP5wsw_VTDNxUh05TPOPZA2TxJnkZJak8taQy', username="cyrex real", content=date.today().strftime("<:carex:1042562384688066600>"))
response = webhook2.execute() 

webhook2 = DiscordWebhook(url='https://discord.com/api/webhooks/1046402781696753715/DuBZxciO1pTDRHq3FnEa2EYsMjI1flapP5wsw_VTDNxUh05TPOPZA2TxJnkZJak8taQy', username="cyrex real", content=date.today().strftime("update **%d/%m/%y:** "))
response = webhook2.execute() 

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
main(seed23)
main(seed24)
main(seed25)
main(seed26)
main(seed27)
main(seed28)
main(seed29)
driver.quit()

