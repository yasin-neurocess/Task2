# Task2
Interview for Software Engineer position of Neurocess Inc. in July 2022 : Task2

Task2: In this part, you need to build a simple API and scrape amazon page.

  Page Link:

      https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4
      
Before scraping the web page, we expect you to build a basic API with a single “GET” route, which is called getData(). After building your API, you need to trigger your web scraping function. 
In the web scraping part, we expect you to take name and price data of listed products. (It is enough to scrape just 1 page, you don't need to scrape all pages).
Finally, your API system will take these scraped name and prices data and show them on a local webpage. (Visualization of the web page is not important, just showing the data is enough for the task.)

Solution: This task is with the API built using the Flask backend framework, and the 'amazon' url given above and the name and price of the products are scraped with the AutoScrape library. And it is transferred to a list and then displayed on localhost with the 'GET' method.
