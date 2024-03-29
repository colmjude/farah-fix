import json
import math
import os

import requests

data_dir = "tmp"


def read_farah_json(file_name="output.json"):
    with open(file_name, "r") as file:
        farah_json = json.load(file)
    return farah_json


def fetch_pages(page, limit=24, max_page=None):
    # make sure the directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    print(f"Fetching page {page}")
    # url for all clothing
    url = (
        f"https://services.mybcapps.com/bc-sf-filter/filter?t=1705475243235&_"
        f"=pf&shop=farahuk.myshopify.com&page={page}&limit={limit}&sort=manual"
        f"&display=grid&collection_scope=131523674211&tag=&product_available="
        f"true&variant_available=true&build_filter_tree=false&check_cache=false"
        f"&locale=en&sid=b6b8e1dc-57f9-4c68-9143-cd0334445cbe&callback="
        f"BoostPFSFilterCallback&event_type=page"
    )
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        # Remove prefixes and suffixes
        prefix = "/**/ typeof BoostPFSFilterCallback === 'function' && BoostPFSFilterCallback("
        suffix = ");"

        if content.startswith(prefix):
            content = content[len(prefix) :]
        if content.endswith(suffix):
            content = content[: -len(suffix)]

            # Save the content to a file
            file_name = f"{data_dir}/all_page{page}.json"
        with open(file_name, "w") as file:
            file.write(content)
        print(f"Collected data from page {page} - saved to {file_name}")
    else:
        print(f"Error: {response.status_code}, unable to collect page {page}")

    if max_page is None:
        first_page_json = read_farah_json(file_name)
        total_product_count = first_page_json["total_product"]
        max_page = math.ceil(total_product_count / limit)
        print(f"Total products = {total_product_count}, pages = {max_page}")

    if page < max_page:
        fetch_pages(page + 1, max_page=max_page)


def extract_products_from_files():
    # Get a list of all files in the directory
    files = [f for f in os.listdir(data_dir) if f.endswith(".json")]
    products = {}

    for f in files:
        full_filename = os.path.join(data_dir, f)
        farah_json = read_farah_json(full_filename)
        print(f'{full_filename} -> {len(farah_json["products"])}')
        for product in farah_json["products"]:
            if product["id"] not in products.keys():
                products[product["id"]] = product

    return products
