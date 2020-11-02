from splinter import Browser
from config import path_to_chromedriver
import pandas as pd
from IPython.display import display, HTML


def scrape_function():
    browser = Browser('chrome', executable_path=path_to_chromedriver)
    dict = {}

    # 1.) NASA Mars News

    browser.visit("https://mars.nasa.gov/news/")
    el = browser.find_by_xpath(
        "/html/body/div[3]/div/div[3]/div[3]/div/article/div/section/div/ul/li[1]/div/div/div[2]/a")
    news_title = el.text
    el = browser.find_by_xpath(
        "/html/body/div[3]/div/div[3]/div[3]/div/article/div/section/div/ul/li[1]/div/div/div[3]")
    news_p = el.text

    dict["news_title"] = news_title
    dict["news_p"] = news_p

    print("news_title = ", news_title)
    print("news_p =", news_p)

    # 2.) JPL Mars Space Images - Featured Image

    browser.visit(
        "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    el = browser.find_by_xpath(
        "/html/body/div[1]/div/div[3]/section[1]/div/div/article/div[1]/footer/a")
    featured_image_url = "https://www.jpl.nasa.gov" + el['data-link']
    browser.visit(featured_image_url)
    el = browser.find_by_text("Full-Res JPG: ")
    el.click()
    featured_image_url = browser.url

    dict["featured_image_url"] = featured_image_url

    # 3.) Mars Weather

    browser.visit("https://twitter.com/marswxreport?lang=en")
    el = browser.find_by_xpath(
        "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span")
    mars_weather = el.text

    dict["mars_weather"] = mars_weather

    # 4.) Mars Facts

    df = pd.read_html("https://space-facts.com/mars/")[0]
    df.columns = ["Description", "Value"]
    html_string = df.to_html(
        classes="table table-striped", index=False)

    dict['html_string'] = html_string

    # 5.) Mars Hemispheres

    hemisphere_image_urls = []
    browser.visit(
        "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    hemispheres_text = [
        "Cerberus Hemisphere Enhanced",
        "Schiaparelli Hemisphere Enhanced",
        "Syrtis Major Hemisphere Enhanced",
        "Valles Marineris Hemisphere Enhanced"
    ]

    for hemisphere in hemispheres_text:
        el = browser.find_by_text(hemisphere)
        title = el.text
        el.click()
        el = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a')
        img_url = el['href']

        hemisphere_image_urls.append({
            "title": " ".join(title.split()[:-1]),
            "img_url": img_url
        })
        browser.back()

    dict['hemisphere_image_urls'] = hemisphere_image_urls

    # hemisphere_image_urls
    browser.quit()

    return dict
