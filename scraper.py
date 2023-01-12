from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

import re

chromedriver_autoinstaller.install()
options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/index')
@app.route('/')
def index():
    driver.get("https://www.cashbackmonitor.com/")

    rates = []
    providers = []

    rate_box = driver.find_element_by_css_selector('div.fl div.fl table.cbm2 tbody')

    for item in rate_box.find_elements_by_css_selector('tr'):
        if (item.text.find('%') != -1):
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            providers.append(tmp)
        else: continue

        for cell2 in item.find_elements_by_css_selector('td:nth-child(3) a'):
            if (cell2.text.find('%') != -1):
                tmp = cell2.text.split("%")[0]
                rates.append(tmp + '%')
            else: continue

    return render_template('index.html', len = len(rates), rates = rates, providers = providers)

@app.route('/rates/<store>', methods=['GET'])
def ratepg(store):
    driver.get("https://www.cashbackmonitor.com/cashback-store/" + store.lower())

    rates = []
    providers = []
    links = []
    imgs = []
    top5_rates = []
    top5_stores = []

    img_logo = driver.find_element_by_css_selector('div.f div.fl img.slogo').get_attribute("src")
    tbody = driver.find_element_by_css_selector('div.half.fl table tbody')

    for row in tbody.find_elements_by_tag_name('tr'):
        if ("Up to" in row.text):
            continue
        if ("up to" in row.text):
            continue
        if ("$" in row.text):
            continue
        if (row.text.find('%') != -1):
            tmp = row.text.split("%")[0]
            tmp = re.sub("[^A-Za-z' ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            providers.append(tmp)
        else: continue

        for cell2 in row.find_elements_by_css_selector('td.l span'):
            if ("Up to" in row.text):
                continue
            if ("up to" in row.text):
                continue
            if ("$" in row.text):
                continue
            if (cell2.text.find('%') != -1):
                tmp = cell2.text.split(' ')[0]
                rates.append(tmp)

        for cell3 in row.find_elements_by_tag_name('td.l.lo a'):
            links.append(cell3.get_attribute('href'))

        for cell4 in row.find_elements_by_tag_name('td.l.ro'):
            imgs.append(cell4.find_element_by_css_selector('a img').get_attribute("src"))

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
            if (i == 5): break

    driver.get("https://www.cashbackmonitor.com/")

    store_rates = []
    store_providers = []

    rate_box = driver.find_element_by_css_selector('div.fl div.fl table.cbm2 tbody')

    for item in rate_box.find_elements_by_css_selector('tr'):
        if (item.text.find('%') != -1):
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            store_providers.append(tmp)
        else: continue

        for cell2 in item.find_elements_by_css_selector('td:nth-child(3) a'):
            if (cell2.text.find('%') != -1):
                tmp = cell2.text.split("%")[0]
                store_rates.append(tmp + '%')
            else: continue

    return render_template('rates.html', len = len(rates), rates = rates,
    providers = providers,  img_logo = img_logo, links = links, imgs = imgs, store = store,
    top5_rates = top5_rates, top5_stores = top5_stores, store_rates = store_rates,
    store_providers = store_providers)

@app.route('/about')
def aboutpg():
    driver.get("https://www.cashbackmonitor.com/")

    store_rates = []
    store_providers = []

    rate_box = driver.find_element_by_css_selector('div.fl div.fl table.cbm2 tbody')

    for item in rate_box.find_elements_by_css_selector('tr'):
        if (item.text.find('%') != -1):
            tmp = item.text.split("%")[0]
            tmp = re.sub("[^A-Z.a-z ]", "", tmp)
            tmp = tmp[::-1].replace('.'[::-1], '', tmp.count('.')-1)[::-1]
            tmp = tmp[:-1]
            store_providers.append(tmp)
        else: continue

        for cell2 in item.find_elements_by_css_selector('td:nth-child(3) a'):
            if (cell2.text.find('%') != -1):
                tmp = cell2.text.split("%")[0]
                store_rates.append(tmp + '%')
            else: continue

    return render_template('about.html', store_rates = store_rates, store_providers = store_providers)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)