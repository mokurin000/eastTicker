import json
from time import sleep
from playwright.sync_api import sync_playwright, Playwright, Page


BASE_URL = "https://guba.eastmoney.com/list,zssh000001"


def scrap(page: Page, category: str, page_num: int):
    url = f"{BASE_URL}_{page_num}.html"
    page.goto(url)
    titles = page.query_selector(".table_list").query_selector_all("div.title")
    print(len(titles))
    modtimes = page.query_selector_all("div.update")
    data = []
    for i, title in enumerate(titles):
        tt = title.query_selector("a")
        time = modtimes[i].text_content()
        data.append({"title": tt.get_attribute("title"), "time": time})
    with open(f"{category}_{page_num:06}.json", mode="w+", encoding="utf-8") as free:
        json.dump(data, free, ensure_ascii=False, indent=4)


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(f"{BASE_URL}.html")
    for page_num in range(1, 1175 + 1):
        scrap(page, "reviews", page_num)
        sleep(2)
    browser.close()


def main():
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    main()
