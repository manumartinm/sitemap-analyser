import pandas as pd
from bs4 import BeautifulSoup
import requests

stop_words = ['wp-content', 'media', 'static', 'public']


def meta_robots(meta_robots):
    if len(meta_robots) > 0:
        robots = meta_robots[0]["content"]
        robots = robots.split(",")
        robots = ",".join(robots[:2])
    else:
        robots = "No robots tag found"
    
    return robots

def get_sitemap_df(sitempas):
    urls = []
    for sitemap in sitempas:
        res = requests.get(sitemap)
        soup = BeautifulSoup(res.text, 'xml')
        loc_tags = soup.find_all("loc")
        for url in loc_tags:
            if not any(value in url.text for value in stop_words):
                res = requests.get(url.text)
                soup = BeautifulSoup(res.text, 'html.parser')
                robots_tag = soup.find_all("meta", {"name": "robots"})
                robots = meta_robots(robots_tag)
                url_info = [url.text, res.status_code, robots, sitemap]
                urls.append(url_info)

    df = pd.DataFrame(urls, columns=["url", "status_code", "meta_robots", "sitemap"])
    return df

    
