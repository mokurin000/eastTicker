import json
from os import listdir

import pandas as pd

EXPORT_XLSX = True


def main():
    all_reviews = []
    for file in listdir("reviews"):
        path = f"reviews/{file}"
        with open(path, "r", encoding="utf-8") as f:
            reviews = json.load(f)
            all_reviews.extend(
                review
                for review in reviews
                if not any(
                    map(
                        lambda alias: alias in review["title"],
                        ["直播间"],
                    )
                )
            )

    with open("reviews.json", mode="w+", encoding="utf-8") as r:
        json.dump(all_reviews, r, indent=4, ensure_ascii=False)
    print(f"count: {len(all_reviews)}")
    if EXPORT_XLSX:
        df = pd.DataFrame(
            all_reviews,
        )
        df.to_excel(
            "reviews.xlsx",
            index=False,
        )


if __name__ == "__main__":
    main()
