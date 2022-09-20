import json
import requests
import time
import re
import fnmatch
import datetime
from datetime import date


source =requests.get("https://legacy.cafebonappetit.com/api/2/menus?cafe=1374").json()
#source =requests.get("https://legacy.cafebonappetit.com/api/2/menus?cafe=1374&date=2021-05-02").json() #syntax for arbitrary date selection
webhookURL = "Webhook URL Goes Here"

day = datetime.datetime.today().weekday()

breakfastData = []
#Breakfast Data
items = source['days'][0]['cafes']['1374']['dayparts'][0][0]['stations'][0]['items']
for item in items:
    if item[0] == '1':
        breakfastData.append(source['items'][item]['label'].title()+ "\n")

#Lunch Data
lunchData = [[],[], [], []]
items = source['days'][0]['cafes']['1374']['dayparts'][0][1]['stations'][1]['items']
for item in items:
    if item[0] == '1':
        lunchData[0].append(source['items'][item]['label'].title()+ "\n")

items = source['days'][0]['cafes']['1374']['dayparts'][0][1]['stations'][2]['items']
for item in items:
    if item[0] == '1':
        lunchData[1].append(source['items'][item]['label'].title()+ "\n")

items = source['days'][0]['cafes']['1374']['dayparts'][0][1]['stations'][3]['items']
for item in items:
    if item[0] == '1':
        lunchData[2].append(source['items'][item]['label'].title()+ "\n")

items = source['days'][0]['cafes']['1374']['dayparts'][0][1]['stations'][4]['items']
for item in items:
    if item[0] == '1':
        lunchData[3].append(source['items'][item]['label'].title()+ "\n")

#Dinner Data
dinnerData = [[],[],  [],[]]
items = source['days'][0]['cafes']['1374']['dayparts'][0][2]['stations'][1]['items']
for item in items:
    if item[0] == '1':
        dinnerData[0].append(source['items'][item]['label'].title()+ "\n")
items = source['days'][0]['cafes']['1374']['dayparts'][0][2]['stations'][2]['items']
for item in items:
    if item[0] == '1':
        dinnerData[1].append(source['items'][item]['label'].title()+ "\n")
items = source['days'][0]['cafes']['1374']['dayparts'][0][2]['stations'][3]['items']
for item in items:
    if item[0] == '1':
        dinnerData[2].append(source['items'][item]['label'].title()+ "\n")
items = source['days'][0]['cafes']['1374']['dayparts'][0][2]['stations'][4]['items']
for item in items:
    if item[0] == '1':
        dinnerData[3].append(source['items'][item]['label'].title()+ "\n")

prefacePayload = {
    "username": "Howard",
    "content": "###############\n **Menu for " + str(date.today()) + "** \n ###############"
}
breakfastPayload = {
  "username": "Howard",


  "embeds": [
    {
          "title": "**Breakfast**",
          "color" : 15777828,
      "fields": [
        {
          "name": "Rise",
          "value": "".join(breakfastData)

        }
      ]


    }
  ]
}

lunchPayload = {
  "username": "Howard",
  "embeds": [
    {
      "title": "**Lunch**",
      "color":2262002,
      "fields": [
        {
          "name": "Roots",
          "value": "".join(lunchData[0])

        },
        {
            "name": "Sizzle",
            "value": "".join(lunchData[1])
        },
        {
            "name":"Rosie's Favorites",
            "value": "".join(lunchData[2])
        },
        {
            "name":"Pomodoro",
            "value": "".join(lunchData[3])
        }
      ]

    }
  ]
}


dinnerPayload = {
  "username": "Howard",
  "embeds": [
    {
      "title": "**Dinner**",
      "color":14557013,
      "fields": [
        {
          "name": "Roots",
          "value": "".join(dinnerData[0])
        },
        {
            "name": "Sizzle",
            "value": "".join(dinnerData[1])
        },
        {
            "name":"Rosie's Favorites",
            "value": "".join(dinnerData[2])
        },
        {
            "name":"Pomodoro",
            "value": "".join(dinnerData[3])
        }

      ]

    }
  ]
}




req = requests.post(webhookURL, json=prefacePayload)
req = requests.post(webhookURL, json=breakfastPayload)
req = requests.post(webhookURL, json=lunchPayload)
req = requests.post(webhookURL, json=dinnerPayload)
if(req.status_code != 204):
  errorPayload = {
      "username": "Howard's Boss",
      "content": "Uh oh, Howard died and the menu isn't working today."
  }
  req = requests.post(webhookURL,  json=errorPayload)
  print(req.status_code)

celebrationInOrder = False
for station in breakfastData:
  if fnmatch.fnmatch("".join(breakfastData).replace("\n", " "), "* Biscuits And * Gravy *"):
    celebrationInOrder = True
  if celebrationInOrder:
    celebrationPayload = {
      "username": "Howard",
      "content": "**Holy cow we have biscuits and gravy today! Best come soon before we run out! Hold on to ya butts!**"
    }
    req = requests.post(webhookURL, json=celebrationPayload)
  # celebrationInOrder = False
  # for station in brunchData:
  #   if fnmatch.fnmatch("".join(brunchData).replace("\n", " "), "* Biscuits And * Gravy *"):
  #     celebrationInOrder = True
  #   if celebrationInOrder:
  #     celebrationPayload = {
  #       "username": "Howard",
  #       "content": "**Holy shit we have biscuits and gravy today! Best come soon before we run out! Hold on to ya mfn butts!**"
  #     }
  #     req = requests.post(webhookURL, json=celebrationPayload)
