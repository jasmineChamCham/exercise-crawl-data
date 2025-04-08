from flask import Flask
import logging
import json
from crawl.lookfantastic.crawl_product_list import crawl_product_list
from crawl.lookfantastic.crawl_product import crawl_pages_by_url
from crawl.utils import get_uncrawled_page_urls
import concurrent.futures
app = Flask(__name__)

@app.route("/crawl/look-fantastic", methods = ['GET'])
def crawl_look_fantastic():
    # crawl_product_list()
        
    while True:
        uncrawled_page_urls = get_uncrawled_page_urls()
        
        if not uncrawled_page_urls: 
            logging.info("No uncrawled pages found, exiting.")
            break

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(crawl_pages_by_url, uncrawled_page_urls)
    
    response = app.response_class(
        response=json.dumps({"message": "Successfully crawled lookfantastic.com"}),
        status=200,
        mimetype='application/json'
    )
    return response