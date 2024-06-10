import json
import os
from time import sleep
from datetime import datetime

from auth import get_access_token
from sentiment_classify import sentiment_classify, PER_SEC


if __name__ == "__main__":
    access_token = get_access_token()

    with open("../data_process/reviews.json", "r", encoding="utf-8") as f:
        reviews = json.load(f)
    
    if os.path.isfile("reviews_tagged.json"):
        with open("reviews_tagged.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []
    
    to_skip = set(map(lambda d: d["text"], data))
    for review in reviews:
        if review["title"] in to_skip:
            continue
        try:
            prev = datetime.now()

            text = review["title"]
            date = f"2024-{review["time"]}"
            fields = sentiment_classify(access_token=access_token, text=text) | {
                "text": text,
                "date": date,
            }
            data.append(fields)
            print(fields)

            to_sleep = 1/PER_SEC-(datetime.now()-prev).seconds
            if to_sleep > 0:
                sleep(to_sleep)
        except:
            break


    with open("reviews_tagged.json", "w+", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
