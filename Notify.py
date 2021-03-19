from pushbullet import Pushbullet
from time import sleep
import gmailReader
from datetime import datetime
import json


with open("parameters.json") as file:
    #Load parameters:
    parameters=json.loads(file)
    searchFor=parameters["search_for_word"]
    received_from_email=parameters['received_from_word']
    pb = Pushbullet(parameters['pushbullet'])
    dev = pb.get_device(parameters['device'])

    #results for the searchFor query
    results = gmailReader.search_messages(gmailReader.service, searchFor)
    # for each email matched, read it
    for msg in results:
        # sender=True if you are the sender
        # msg is dict with keys: From, To, Subject, text
        sender,msg=gmailReader.read_message(gmailReader.service, msg,parameters['your_email'])
        if sender: #Don't want notifications upon sending, only receiving
            continue
        msgDate=gmailReader.convertToDateTime(msg['Date'])
        # want to only check the emails from past 24 hours (new emails)
        dayDiff=abs((datetime.now() - msgDate).days)
        # no LinkedIn emails (hate it!!!)
        if(dayDiff<1 and "LinkedIn" not in msg['Subject'] and "linkedin" not in msg['From'] and received_from_email in msg['From']):
            # give notification as:
            # <Subject>
            # <plain/text message>
            push = dev.push_note(msg['Subject'], msg['text'])
            #print in the console
            out=[": ".join([key,msg[key]]) for key in ['Subject','text']]
            print(", ".join(out),"Date: "+msgDate.strftime("%d/%m/%Y"))



    