<img src="assets\spotify_logo.png" alt="Spotify Logo" width="25" height="25"> Spotify Web Scraper
=======================

Spotify Web Scraper crawls through the Spotify web interface and extracts artist monthly listener information.

## Technology Stack
 - [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - Parse HTML code
 - [Selenium](https://pypi.org/project/selenium/) - Browser Automation Tool

## Dependencies
Install Dependencies with [pip](https://pypi.org/project/pip/)

```
pip install beautifulsoup4
pip install selenium
```

Alternatively you can install the requirement.txt
```
pip install -r requirement.txt
```

## Selenium Chrome Webdriver
Since Spotify webpages are generated dynamically, we need a headless browser to generate the webpages dynamically from the source. I have chosen the Chrome WebDriver which works great in this instance.

Download and save the <a href="http://chromedriver.chromium.org/downloads">Chrome WebDriver</a> at the root level.

## Authors
  Author of original repo - [Chris Yang](https://chrisyang.io) (ServiceNow Architect, GlideFast)
  Fork Author - [Steveruu](https://steveruu.github.io) (idiot)
