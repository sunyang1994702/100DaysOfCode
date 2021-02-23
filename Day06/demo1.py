"""This is a expamle for chinese movie website : https://movie.douban.com/.
   These has a very popular movie released named: 你好，李焕英
   
   So next, I will crawl some comments about this movie.
"""

from bs4 import BeautifulSoup
import requests
import csv
import time
import random


def get_each_review(item):
    comment_info = item.find('span', class_="comment-info")
    user_url = comment_info.find('a')['href']
    user_id = comment_info.find('a').text
    rate = get_comment_rate(comment_info.find('span', class_="rating"))
    comment_time = comment_info.find('span', class_="comment-time")['title']
    comment_content = item.find('p').text.strip()
    user_city = get_user_info(user_url)

    return [user_id, comment_content, rate, comment_time, user_city]


def get_comment_rate(comment_rate):
    if comment_rate:
        comment_str = comment_rate['class'][0]
        return int(comment_str[-2])
    else:
        return 0


def get_user_info(user_url):
    ## set time sleep.
    time.sleep(round(random.uniform(1, 2), 2))
    ## request user's website
    user_req = requests.get(user_url, headers=headers)
    user_bf = BeautifulSoup(user_req.text)
    city_info = user_bf.find('div', class_="user-info")
    city = ""

    try:
        city = city_info.find('a').text
    except Exception:
        pass

    return city
    

def get_one_page(url):
    req = requests.get(url, headers=headers, cookies=cookies)
    bf = BeautifulSoup(req.text)
    return bf.find_all('div', class_="comment-item")


def save_data(results):
    with open("Douban_review_500.csv", 'a+', newline='', encoding='utf-8-sig') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(results)


def main():
    results = [['UserID', 'Content', 'Rate', 'Time', 'City']]
    for i in range(20):
        url = "https://movie.douban.com/subject/{}/comments?start={}&limit=20&status=P&sort=new_score".format(movie_id, 20*i)
        items = ""
        try:
            items = get_one_page(url)
        except Exception:
            print("Number : {} Request Failled!!".format(i+1))
            time.sleep(random.randint(1,10))
            items = get_one_page(url)

        if items:
            for each_item in items:
                results.append(get_each_review(each_item))
            print("Number : {} page finished!!".format(i+1))
        else:
            print("Number : {} page Null!!".format(i+1))

    save_data(results)


if __name__ == '__main__':
    movie_id = "34841067"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    cookies = {
        'cookie': ''    }
    main()
