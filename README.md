# Youtube Crawler/Spider

In a youtube channel there is a tab called "Channels" where they link to other channels. I use this to find related creators, but I wanted to see how far it goes.
The program uses selenium to open all the channels, and then the channel channels, till infinity.

## WIP
- [DONE] get the channels on one page
- get all the channels channels till infinity
- visualise it with some graph code

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

_Selenium_
```
pip install selenium
```
[_chromewebdriver_](https://chromedriver.chromium.org/)

Make sure to pick the release for you according to your chrome version (chrome://version/). And decide on the correct version, chrome version, OS, cpu architecture. ie. Stable Chromedriver Windows x64 117.
### Installing
Download the files from the repository, and get the prerequisites.

To run the scraping program (ytspyder.py), you run it like any other python program. 
Open terminal or cmd and paste this in but replace YOUR_PATH with where ever you saved the files. You might also have to replace python with py or python3.
```
python YOUR_PATH/ytspyder.py
```

## Version and Enviroment Details
This is the first python project where I used a conda virtual enviroment. 

python 3.11 | Selenium 4.12 | Chrome 117 | Chromedriver 117

---
* **m&m** - *Initial work* - [m&m](https://github.com/MandMcoding)

## License

This project is licensed under the GPL-3 License - see the [LICENSE.md](LICENSE.md) file for details
