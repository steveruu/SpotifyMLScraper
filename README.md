<img src="assets\spotify_logo.png" alt="Spotify Logo" width="25" height="25"> Spotify Monthly Listener Scraper
=======================

Spotify Monthly Listener Scraper crawls through the Spotify web interface and extracts artist monthly listener information, then sends them via a Discord webhook

## Technology Stack
 - [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - For parsing HTML code
 - [Selenium](https://pypi.org/project/selenium/) - Browser automation tool
 - [Discord Webhook](https://pypi.org/project/discord-webhook/) - Webhook to send messages to a Discord server

## Dependencies
Install Dependencies with [pip](https://pypi.org/project/pip/)

```
pip install beautifulsoup4
pip install selenium
pip install discord-webhook
```

Alternatively you can install the requirement.txt
```
pip install -r requirement.txt
```

## Selenium Chrome Webdriver
Since Spotify webpages are generated dynamically, we need a headless browser to generate the webpages dynamically from the source. I have chosen the Chrome Webdriver which works great in this instance.

Download and save the <a href="http://chromedriver.chromium.org/downloads">Chrome Webdriver</a> at the root level.

## Authors
  * Author of [original repo](https://github.com/zaidongy/Spotify-Scraper) - [Chris Yang](https://chrisyang.io) (ServiceNow Architect, GlideFast)  
  * Fork Author - [Steveruu](https://steveruu.github.io) (idiot)
