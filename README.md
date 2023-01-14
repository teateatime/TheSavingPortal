# TheSavingPortal

The Saving Portal is an automated cashback monitoring system that automatically scans the best cashback rates of many platforms and displays those values both numerically and statistically.

### Technologies Used:
* HTML
* CSS
* JavaScript
* BootStrap
* Python

How to set it up and use it:
---------------------------------------------------------------
First, check if you have git installed.

You can do this by entering `git --version` inside the terminal.

If you do not have git installed, there are plenty of sources online to help you get started.
Here is one of the sources to help you with getting git setup in your system.
                                                                            
https://git-scm.com/

Next to install the necessary packages for the imports used in python, you can use the following pip commands in the terminal:

`pip install flask`: This command installs the Flask package, which is necessary for creating and running a Flask web application.

`pip install selenium`: This command installs the Selenium package, which is necessary for interacting with a web browser using the Selenium library.

`pip install chromedriver-autoinstaller`: This command installs the chromedriver_autoinstaller package, which is necessary for automatically installing the ChromeDriver executable, which is needed for controlling the Chrome browser using Selenium.

Note that these commands assumes that you have python and pip installed in your system.

Also, to run the script with selenium, you need to have Chrome browser installed in your system.


Clone the Repository
---------------------------------------------------------------
Once you have git setup and the other neccessary packages, enter this git command to clone the repository so that you can use it for your own use.

`git clone https://github.com/teateatime/TheSavingPortal.git`

Once successfully cloned, type in `cd TheSavingPortal` and then type in `python scraper.py` inside the terminal/cmd to use the program.

Afterwards it will output several lines afterwards and you can run the app on 
"http://127.0.0.1:5000". From there you will be introduced to the main page and view the cashback rates
of multiple stores at your leisure.

Screenshots
---------------------------------------------------------------
### Main Page

![MainTSPPage](https://github.com/teateatime/TheSavingPortal/blob/main/static/screenshots/TSP_MainPage.png)

### Rates Page (Macy's)

![TSP_MacysRatePageImg](https://github.com/teateatime/TheSavingPortal/blob/main/static/screenshots/TSP_MacysRatePage.png)

### About Page

![AboutTSP](https://github.com/teateatime/TheSavingPortal/blob/main/static/screenshots/TSP_AboutPage.png)
