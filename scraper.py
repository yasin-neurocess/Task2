# -*- coding: utf-8 -*-

# Interview for Software Engineer position of Neurocess Inc. in July 2022 : Task2
# Candidate: Yasin Ozdemir - tr.yasinozdemir@gmail.com

# I had some tests and I have seen that occasionally the web page freezes an empty list based on its stuck...
# ...that's way unfortunately you may be exposed to the 500 error.. you need to try again..

# I'm sure code's working when I uploaded on Github the latest...
# ...if you have problems about code, please feel free to contact me..

# thank you for giving me the opportunity to be a part of Neurocess Inc.

from flask import Flask, request
from autoscraper import AutoScraper
from amazon import *
# from flask_restful import Api, Resource, reqparse

scraper = AutoScraper()
# scraper.load('order-list')
app = Flask(__name__)
# api = Api(app)


# building API and call the order-lis(product name, product price)
def getData(search_query):
    amazon_url = "https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4" % search_query
    # if you want to show runtime datas, should be active the following two lines
    run_scraper()
    scraper.load('order-list')
    # getting the datas with group IDs
    output = scraper.get_result_similar(amazon_url, group_by_alias=True)
    return ok_result(output)


# actually doing nothing.. just formatting data properly
def ok_result(output):
    outputData = []
    print(list(output.values())[0])
    for i in range(len(list(output.values())[0])):
        try:
            outputData.append({alias: output[alias][i] for alias in output})
        except:
            pass
    return outputData


# routing to 'locolhost' as 'GET' method for show the datas
@app.route('/', methods=['GET'])
def run_api():
    query = request.args.get('q')
    print(query)
    return dict(output=getData(query))


# just doing everything
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
