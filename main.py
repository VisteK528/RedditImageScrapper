import requests
import urllib.request
import time
import os

allowed = True

url_main = ['https://oauth.reddit.com/r/PrequelMemes/hot', "https://oauth.reddit.com/r/memes/", 'https://oauth.reddit.com/r/cursedtoilets/',
            'https://oauth.reddit.com/r/hmmm/', 'https://oauth.reddit.com/r/starwarsmemes/', 'https://oauth.reddit.com/r/cursedimages/']
myPath = ['C:\\Users\ppato\PycharmProjects\WebScrapping2\PrequelMemes\\', 'C:\\Users\ppato\PycharmProjects\WebScrapping2\Memes\\',
          'C:\\Users\ppato\PycharmProjects\WebScrapping2\Toilets\\', 'C:\\Users\ppato\PycharmProjects\WebScrapping2\CursedImages\\',
          'C:\\Users\ppato\PycharmProjects\WebScrapping2\Test\\']

test_path = 'C:\\Users\ppato\PycharmProjects\WebScrapping2\Test\\'

CLIENT_ID = "0tkz2ASDwHfRHQ"
SECRET_KEY = "tKeMcBgWf30pTKKg6SkdM3tAhvXAVQ"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

with open('pw.txt', 'r') as f:
    pw = f.read()

data = {
    'grant_type': 'password',
    'username': 'VisTech528',
    'password': pw
}

headers = {'User-Agent': 'Python Reddit Web Scrapper by VisteK528'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

req = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)

#print(soup.prettify())

number = 0
test_number = 0
number_allowed = 0



def find_memes(URL, PATH):
    global number, number_allowed, url_main, test_path

    # Getting response JSON file from targeted subreddit ( 100 indexes )




    # Repeating 20 times whole sequence
    for i in range(20):
        # Printing how many times sequence has started
        print(i)

        # Itering through all post in JSON file
        for post in req.json()['data']['children']:
            try:
                # Trying to find post's url which may contain image, gif or video
                image_src = post['data']['url_overridden_by_dest']
            except:
                continue

            # print(image_src)
            image_src = image_src.replace('amp;s', 's')
            print(image_src)
            end = image_src[-4:]
            print(end)
            """
            if end != '.jpg' and end != '.png':
                print(post['data']['secure_media']['reddit_video']['scrubber_media_url'])
            """
            if end == '.jpg' or end == '.png':
                test_path = 'C:\\Users\ppato\PycharmProjects\WebScrapping2\PrequelMemesSorted\images\\'
                filename = str(number) + ".png"
                fullfilename = os.path.join(test_path, filename)
                print("PNG")
                urllib.request.urlretrieve(image_src, fullfilename)
                after = post['kind'] + '_' + post['data']['id']
                # print(after)

                number += 1
                number_allowed += 1
                time.sleep(0.5)

            elif end == '.gif':
                test_path = 'C:\\Users\ppato\PycharmProjects\WebScrapping2\PrequelMemesSorted\gifs\\'
                filename = str(number) + ".gif"
                fullfilename = os.path.join(test_path, filename)
                print("GIF")
                urllib.request.urlretrieve(image_src, fullfilename)
                after = post['kind'] + '_' + post['data']['id']
                # print(after)

                number += 1
                number_allowed += 1
                time.sleep(0.5)

            """

            Test part of the code with including video download feature, unhappily not working yet

            """
            """
            else:
                test_path = 'C:\\Users\ppato\PycharmProjects\WebScrapping2\PrequelMemesSorted\others\\'
                media_url = post['data']['secure_media']['reddit_video']['fallback_url']
                print(media_url)
                #media_url = post['data']['secure_media']['reddit_video']['scrubber_media_url']
                after = post['kind'] + '_' + post['data']['id']

                print("Other")
                rsp = urllib.request.urlopen(media_url)
                fullfilename = os.path.join(test_path, 'film.mp4')
                with open(fullfilename, 'wb') as f:
                    f.write(rsp.read())
                """

            print(number)
            if number_allowed >= 60:
                time1 = time.time()
                while time.time() - time1 < 15:
                    print(time.time() - time1)
                    time.sleep(1)
                    print("Waiting...")
                    number_allowed = 0



        req = requests.get(url_main[0], headers=headers, params={'limit': '100', 'after': after})

        time.sleep(1)




while True:
    URL = input("Type URL: ")
    PATH = input("Type PATH: ")


    find_memes(URL, PATH)



#print(link)

