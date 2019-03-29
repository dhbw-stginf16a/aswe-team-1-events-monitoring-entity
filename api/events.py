#!/usr/bin/env python3

import logging
import requests
import json
logger = logging.getLogger(__name__)


def getEvents(body): 
    location = "@48.7744476,9.1714984,17.5"
    endpoint = "https://api.predicthq.com/v1/events/?within=20km" + body['payload']['location'] + "?start.gte=" + body["payload"]["start_date"] + "&start.lte=" + body["payload"]["end_date"] + "&start.tz=Europe/Berlin"

    headers = {
        "Authorization": "Bearer l5w7oDrJCUi4LTD77TnHdXJTKIEI6t",
        "Accept": "application/json"
        }
    data = requests.get(endpoint, headers=headers).json()
    print(json.dumps(data, indent=4, sort_keys = True))
    response = {
        'type': 'event',
        'payload': {
            'events': []
        }
    }

    data_filtered = []
    for x in body['payload']['categories']:
        print(x)
        for y in data["results"]:
            print(y)
            if y["category"] == x:
                print(y)
                data_filtered.append(y)
        #data_filtered.append(y for y in data["results"] if y['category'] == x)

    print(data_filtered)
    for x  in data_filtered:
        temp = {}
        temp["title"] = x["title"]
        temp["description"] = x["description"]
        temp["start"] = x["start"]
        temp["location"] = x["location"]
        temp["category"] = x["category"]
        response['payload']['events'].append(temp)
    return [response], 200