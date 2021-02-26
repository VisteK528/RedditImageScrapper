## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is simple Reddit API used for image scraping from chosen subreddit  
	
## Technologies
Project is created with:
* Python 3.8

Libraries:
* Requests 2.25.1

Default libraries used in this project:
* urllib
* time
* os

	
## Setup
To run this project, first of all you have to register your Bot/API [here](https://www.reddit.com/prefs/apps) on the Reddit

After this process your API site should provide you two ID's
* Client ID, which you can find under your API name titled as **personal use script**
* Secret Key, which will be simple titled as **secret**

Then you should copy those tokens and put them in the **main.py** file in correct place, accordingly Client ID in bracket named as **YOUR_CLIENT_ID** and Secret Key in bracket named as **YOUR_SECRET_KEY**

Finally before running the code, you have to replace **USERNAME** with your Reddit username in data dictionary in main file, in headers replace **YOUR_API_NAME** with name of your API and at the end in **pw.txt** file you should text which is there with your Reddit account password.

After all of these steps your code is ready to begin scraping images for U
I hope you'll enjoy it

