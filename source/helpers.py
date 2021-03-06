# -*- encoding: utf-8 -*-

import datetime
import json
import codecs
import subprocess
from collections import OrderedDict


def wind_direction(direction: int):

    if 338 <= direction <= 360 or 1 <= direction <= 22:
        return "North"
    elif 23 <= direction <= 67:
        return "North-East"
    elif 68 <= direction <= 112:
        return "East"
    elif 113 <= direction <= 157:
        return "South-East"
    elif 158 <= direction <= 202:
        return "South"
    elif 203 <= direction <= 247:
        return "South-West"
    elif 248 <= direction <= 292:
        return "West"
    elif 293 <= direction <= 337:
        return "North-West"


def format_datetime(unix_time, offset):
    
    formatted_datetime = datetime.datetime.fromtimestamp(unix_time + offset - 3600).strftime('%H:%M')
    return formatted_datetime


def edit_config(key: str, value: str):

    with codecs.open('config.json', 'r', encoding = 'utf-8') as f:
        data = json.load(f, object_pairs_hook = OrderedDict)

    data[key] = value

    with codecs.open('config.json', 'w') as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)
    
    f.close()