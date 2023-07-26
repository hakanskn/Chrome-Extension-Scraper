from extension_scrape_provider import *
import time
import pandas as pd

if __name__ == '__main__':

    with open('ext_urls.txt') as f:
        ext_urls = f.readlines()

    ext_urls = [x.strip().replace("\n", "") for x in ext_urls]

    extension_list = []
    error_list = {}

    provider = ExtensionProvider()

    for i, visit_url in enumerate(ext_urls):
        start_time = time.time()
        try:
            extension_list.append(provider.GetExtensionDetails(visit_url))
            end_time = time.time()
            print(str(i + 1) + ": " + extension_list[-1].title + "\t - \t {:.2f}".format(end_time - start_time))
        except Exception as e:
            error_list[visit_url] = e

    print("")
    df = pd.DataFrame([o.__dict__ for o in extension_list])
