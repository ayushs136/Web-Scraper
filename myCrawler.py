'''
Created by AYUSH SHARMA aka KRONO$
on 2018-06-08 at 2:14am
'''

import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from io import BytesIO
import os

n = 0


class Bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[96m'


def links():
    search = input("Search for: ")
    params = {"q": search}
    r = requests.get("http://www.flipkart.com/search", params=params)

    soup = bs(r.text, "html.parser")
    titles = soup.findAll("div", {"class": "_3wU53n"})
    results = soup.findAll("a", {"class": "_31qSD5"})

    for title in titles:
        for items in results:
            href = "http://www.flipkart.com" + items.get('href')
            print(title.string)
            print("URL:")
            print(href)
            print("\n---------------------------------------------------------------------------------\n")


def searchImages():
    search = input("What do u wanna search: ")
    params = {"q": search}
    dir_name = search.replace(" ", "").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = bs(r.text, "html.parser")
    link = soup.findAll("a", {"class", "thumb"})

    for item in link:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("URL: " + item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("could not save images...")
        except:
            print("could not request image...")


def intro():
    print(Bgcolors.OKBLUE + "\t* HEY GUYS THIS IS A WEB CRAWLER OR WEB SPIDER OR WHATEVER...JK\n" +
          "\t* HERE YOU CAN SEARCH FOR THE LINKS OF THE PRODUCTS ON flipkart.com\n" +
          "\t* AND CAN SEARCH FOR IMAGES ON bing.com(download automatically)\n")


def menu():
    global n
    print(
        Bgcolors.OKBLUE + "\t* here is the main menu...\n" + Bgcolors.ENDC + Bgcolors.FAIL + "PRESS\n" + Bgcolors.ENDC +
        Bgcolors.OKGREEN + "\t\t 1. to search for images on bing.com\n" +
        "\t\t 2. to search for products on flipkart.com\n" +
        "\t\t 3. to quit the application\n" + Bgcolors.ENDC)
    n = int(input("Enter your choice: "))


def select():
    global n
    print(Bgcolors.HEADER)

    print(Bgcolors.ENDC)
    while n > 0:
        if n == 1:
            searchImages()
            menu()
        elif n == 2:
            links()
            menu()
        elif n == 3:
            print(Bgcolors.BLUE + "thanks for using this application.\n" + Bgcolors.ENDC)
            break
        else:
            print(Bgcolors.WARNING + "\nWrong input...\n\n" + Bgcolors.ENDC)
            select()


intro()
menu()
select()
