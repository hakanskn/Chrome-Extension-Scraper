from extension_scrape_provider import *
import time


if __name__ == '__main__':

    with open('category_urls.txt') as f:
        cat_urls = f.readlines()

    cat_urls = [x.strip().replace("\n", "") for x in cat_urls]

    scrape_url_list = []

    room_list = []
    error_list = {}

    provider = ExtensionProvider()

    for i, visit_url in enumerate(scrape_url_list):
        start_time = time.time()
        try:
            room_list.append(provider.GetExtensionDetails(visit_url))
        except Exception as e:
            error_list[visit_url] = e
        end_time = time.time()

        print(str(i+1) + ": " + "{:.2f}".format(end_time-start_time))

    print("")
