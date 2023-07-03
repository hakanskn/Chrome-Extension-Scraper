from extension_scrape_provider import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('category_urls.txt') as f:
        cat_urls = f.readlines()

    cat_urls = [x.strip().replace("\n", "") for x in cat_urls]

    ext_urls = []
    for cat_url in cat_urls:
        provider = ExtensionProvider()
        ext_urls.extend(provider.GetExtensionUrls(cat_url))

    with open("ext_urls.txt", 'w') as output:
        for row in ext_urls:
            output.write(str(row) + '\n')

