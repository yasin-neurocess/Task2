# Interview for Software Engineer position of Neurocess Inc. in July 2022 : Task2
# Candidate: Yasin Ozdemir - tr.yasinozdemir@gmail.com

# I had some tests and I have seen that occasionally the web page freezes an empty list based on its stuck...
# ...that's way unfortunately you may be exposed to the 500 error.. you need to try again..

# I'm sure code's working when I uploaded on Github the latest...
# ...if you have problems about code, please feel free to contact me..

# thank you for giving me the opportunity to be a part of Neurocess Inc.

from autoscraper import AutoScraper

scraper = AutoScraper()


# main scrape method
def run_scraper():
    base_url = "https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4"
    order_list = ["Apple AirPods (3. nesil)", "2.986,01TL"]

    output = scraper.build(base_url, order_list)
    print(scraper.get_result_similar(base_url, grouped=True))

    # if you want to list regularly, you need to activate the following two lines..but have some must tricks...if you need it, please contact me..
    #scraper.set_rule_aliases({'rule_bew4': 'Product Name', 'rule_6sfd': 'Product Price'})
    #scraper.keep_rules(['rule_bew4', 'rule_6sfd'])
    scraper.save('order-list')
