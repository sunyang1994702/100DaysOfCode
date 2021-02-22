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
    with open("C:/Users/sunya/OneDrive/桌面/100DaysOfCode/Day06/Douban_review_500.csv", 'a+', newline='', encoding='utf-8-sig') as f:
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
        'cookie': 'bid=gcfyoWWiWJY; __utmc=30149280; __utmz=30149280.1613896443.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmz=223695111.1613896443.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; __gads=ID=16f40c9c51ec6f38-2271effe1ec60002:T=1613896444:RT=1613896444:S=ALNI_MZtzdODWQ96vdeGl6QSiegiQOtWXA; trc_cookie_storage=taboola%2520global%253Auser-id%3D8f472d2d-bccd-4c89-977c-925932754229-tuct5d349b1; _vwo_uuid_v2=D3C960EACC1C5F6E07A9429106CAF3B96|d247d26b8d01296568a2856d36f93df0; dbcl2="154772613:RlHyYstmHIc"; ck=I-92; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15477; loc-last-index-location-id="118254"; ll="118254"; _ga=GA1.2.292864210.1613896443; ap_v=0,6.0; __utma=30149280.292864210.1613896443.1613896443.1613999766.2; __utma=223695111.1046750037.1613896443.1613896443.1613999766.2; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1613999766%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=7378738c5e5949d2.1613896443.2.1614000525.1613899841'
    }
    main()