# Email-query-specific-notifier

Often people wait for certain email about important subjects/from important organizations. They open their emails regularly, or check their emails for every notification.

This project aims to only notify you when an email arrives matching a certain query you specify 

This was done using python. The code runs once and needs a scheduler to run (ex: crontab on linux).

It is preferable to include the code on an always running computer (ex: raspberry pi).

This project was done using GMAIL API, and Pushbullet notifier API


# Dependencies

(you can install these using pip)

pushbullet.py

google-api-python-client google-auth-httplib2 google-auth-oauthlib


# First time initialization

You need to get your own gmail api credentials (you can download the credentials.json for your gmail from google cloud https://console.cloud.google.com/apis/api/gmail.googleapis.com/).

You need to sign up for Pushbullet (https://www.pushbullet.com/), download the application on your mobile phone (iOS/Android), and get the API key and device name, and put them in pushbullet_parameters.json


# How to Run

Put the code, credentials.json inside the folder

Fill in the desired query options in query.json
Run query_notify.py
