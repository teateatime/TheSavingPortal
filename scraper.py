from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, redirect, url_for
import chromedriver_autoinstaller
import re

# chromedriver_autoinstaller.install()
# options = Options()
# options.add_argument("--headless")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options)

options = Options()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1920,1200")

service = Service('/driver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/index')
@app.route('/')
def index():
    driver.get("https://www.cashbackmonitor.com/")

    rates = []
    providers = []

    # rate_box = driver.find_element_by_css_selector('div.fl div.fl table.cbm2 tbody')
    # rate_box = driver.find_element('div.fl div.fl table.cbm2 tbody')
    rate_box = driver.find_element('xpath', '//div[contains(@class, "fl")]/table[contains(@class, "cbm2")]/tbody')
    rows = rate_box.find_elements('tag name', 'tr')

    for item in rows:
        if (item.text.find('%') != -1):
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            providers.append(tmp)
            cells = item.find_elements('css selector', 'td:nth-child(3) a')
        else: continue

        for cell2 in cells:
            if (cell2.text.find('%') != -1):
                tmp = cell2.text.split("%")[0]
                rates.append(tmp + '%')
            else: continue

    return render_template('index.html', len=len(rates), rates=rates, providers=providers)

@app.route('/rates/<store>', methods=['GET'])
def ratepg(store):
    driver.get("https://www.cashbackmonitor.com/cashback-store/" + store.lower())

    rates = []
    providers = []
    links = []
    imgs = []
    top5_rates = []
    top5_stores = []

    img_logo = driver.find_element(By.CSS_SELECTOR, 'div.f div.fl img.slogo').get_attribute("alt")
    tbody = driver.find_element(By.CSS_SELECTOR, 'td.sp.half.tl div.half.fl table.cbm2 tbody')

    for row in tbody.find_elements(By.TAG_NAME, 'tr'):
        if ("Up to" in row.text) or ("up to" in row.text) or ("$" in row.text):
            continue

        if "%" in row.text:
            tmp = row.text.split("%")[0]
            tmp = re.sub("[^A-Za-z' ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            providers.append(tmp)
        else:
            continue

        for cell2 in row.find_elements(By.CSS_SELECTOR, 'td.l span'):
            if ("Up to" in row.text) or ("up to" in row.text) or ("$" in row.text):
                continue

            if "%" in cell2.text:
                tmp = cell2.text.split(' ')[0]
                rates.append(tmp)

        for cell3 in row.find_elements(By.CSS_SELECTOR, 'td.l.lo a'):
            links.append(cell3.get_attribute('href'))

        for cell4 in row.find_elements(By.CSS_SELECTOR, 'td.l.ro'):
            img = cell4.find_element(By.CSS_SELECTOR, 'a img.ficon')
            img_src = img.get_attribute("src")
            if img_src:
                img_src = img_src.split(' ')[-1]  # Retrieve the last URL from "alt src" combination
                imgs.append(img_src)

    print(links)
    print(imgs)

    x = len(rates)
    if x <= 5:
        for i in range(0, x):
            tmp = rates[i].split("%")[0]
            tmp = re.sub("[^\d.]", "", tmp)
            top5_rates.append(tmp)
            top5_stores.append(providers[i])
    else:
        for i in range(0, len(rates)):
            tmp = rates[i].split("%")[0]
            tmp = re.sub("[^\d.]", "", tmp)
            top5_rates.append(tmp)
            top5_stores.append(providers[i])
            if i == 4:  # Changed to i == 4 to get the top 5 rates
                break

    driver.get("https://www.cashbackmonitor.com/")

    store_rates = []
    store_providers = []

    rate_box = driver.find_element(By.CSS_SELECTOR, 'div.fl div.fl table.cbm2 tbody')

    for item in rate_box.find_elements(By.TAG_NAME, 'tr'):
        if "%" in item.text:
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            store_providers.append(tmp)
        else:
            continue

        for cell2 in item.find_elements(By.CSS_SELECTOR, 'td:nth-child(3) a'):
            if "%" in cell2.text:
                tmp = cell2.text.split("%")[0]
                store_rates.append(tmp + '%')
            else:
                continue

    return render_template('rates.html', len=len(rates), rates=rates, providers=providers, img_logo=img_logo,
                            links=links, imgs=imgs, store=store, top5_rates=top5_rates, top5_stores=top5_stores,
                            store_rates=store_rates, store_providers=store_providers)

@app.route('/about')
def aboutpg():
    driver.get("https://www.cashbackmonitor.com/")

    store_rates = []
    store_providers = []

    rate_box = driver.find_element(By.CSS_SELECTOR, 'div.fl div.fl table.cbm2 tbody')

    for item in rate_box.find_elements(By.TAG_NAME, 'tr'):
        if "%" in item.text:
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            store_providers.append(tmp)
        else:
            continue

        for cell2 in item.find_elements(By.CSS_SELECTOR, 'td:nth-child(3) a'):
            if "%" in cell2.text:
                tmp = cell2.text.split("%")[0]
                store_rates.append(tmp + '%')
            else:
                continue

    return render_template('about.html', store_rates = store_rates, store_providers = store_providers)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
    driver.quit()
