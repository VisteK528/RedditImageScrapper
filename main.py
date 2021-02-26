import requests
import urllib.request
import time
import os

"""

Web Scrapping API by VisteK528
©2021

"""


"""
 
Insert here your client id and secret key which you can find after API registration 
with this link https://www.reddit.com/prefs/apps

"""

CLIENT_ID = "YOUR_CLIENT_ID"
SECRET_KEY = "YOUR_SECRET_KEY"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)


"""

In my opinion loading password from different file is much more safe,
but you can write down your password instead of password variable if you want

"""

with open('pw.txt', 'r') as f:
    password = f.read()

"""

Here type in your Reddit Username and password which by default will be loaded from pw.txt file, so first go there and
change default text to your password

"""

data = {
    'grant_type': 'password',
    'username': 'USERNAME',
    'password': password
}

# Here you should type in name of your API
headers = {'User-Agent': 'YOUR_API_NAME'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

req = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)


number = 0
test_number = 0
number_allowed = 0



def find_images(URL, PATH):
    global number, number_allowed

    # Getting response JSON file from targeted subreddit ( 100 indexes )
    req = requests.get(URL, headers=headers, params={'limit': '100'})

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

            try:
                # print(image_src)
                image_src = image_src.replace('amp;s', 's')
                print(image_src)
                end = image_src[-4:]
                print(end)
                if end == '.jpg' or end == '.png':
                    filename = str(number) + ".png"
                    fullfilename = os.path.join(PATH, filename)
                    print("PNG")
                    urllib.request.urlretrieve(image_src, fullfilename)
                    after = post['kind'] + '_' + post['data']['id']
                    # print(after)

                    number += 1
                    number_allowed += 1
                    time.sleep(0.3)

                elif end == '.gif':
                    filename = str(number) + ".gif"
                    fullfilename = os.path.join(PATH, filename)
                    print("GIF")
                    urllib.request.urlretrieve(image_src, fullfilename)
                    after = post['kind'] + '_' + post['data']['id']
                    # print(after)

                    number += 1
                    number_allowed += 1
                    time.sleep(0.3)

                """

                Test part of the code with including video download feature, unhappily not working yet

                """
                """
                else:
                    media_url = post['data']['secure_media']['reddit_video']['fallback_url']
                    print(media_url)
                    #media_url = post['data']['secure_media']['reddit_video']['scrubber_media_url']
                    after = post['kind'] + '_' + post['data']['id']

                    print("Other")
                    rsp = urllib.request.urlopen(media_url)
                    fullfilename = os.path.join(PATH, 'film.mp4')
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

            except Exception as e:
                print(e)
                continue


        req = requests.get(URL, headers=headers, params={'limit': '100', 'after': after})

        time.sleep(0.75)


"""

One important thing, your URL should look like this one:
https://oauth.reddit.com/r/PrequelMemes/hot

I mean it should contain this: https://oauth.reddit.com and then add rest of your url

e.g.
You want to use r/memes subreddit?
Your URL should look like this: https://oauth.reddit.com/r/memes/

Of course you can add at the end of line hot or new keyword and then URL will look like my r/PrequelMemes example


"""

while True:
    URL = input("Subreddit URL: ")
    PATH = input("Your PATH where images will be stored: ")

    find_images(URL, PATH)




