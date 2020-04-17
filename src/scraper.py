from PIL import Image
import requests
from bs4 import BeautifulSoup
from io import BytesIO


def scraper():
    print("words to search online:")
    searchkeyword = input()
    print(" searching on bing.com")
    param = {"q": searchkeyword, "qft": "+filterui:imagesize-wallpaper"}
    search_url = "https://www.bing.com/images/search"
    data = requests.get(search_url, params=param)
    beautifulsoup = BeautifulSoup(data.text, "html.parser")
    links = beautifulsoup.findAll("a", {"class": "thumb"})
    for items in links:
        try:
            img_url = requests.get(items.attrs["href"])
            filename = items.attrs["href"].split("/")[-1]
            img = Image.open(BytesIO(img_url.content))
            print("size of image is :", img.size)
            if img.size[0] > 500:
                print(" **************Saving file from :", filename, " with display size : ", img.size)
                img.save("../scraped/" + filename, img.format)
        except:
            print("save failed")

    scraper()


if __name__ == "__main__":
    scraper()
