import os
import sys

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


class MySpider(scrapy.Spider):
    # The name of the spider
    name = "myspider"
    # The base URL of the website
    base_url = "https://www.griffith.ie/"
    # The index of the current page
    index = 0

    def start_requests(self):
        # Start by crawling the homepage of the website
        yield scrapy.Request(self.base_url, self.parse)

    def parse(self, response):
        # Extract all the links on the page
        for url in response.css("a::attr(href)").getall():
            # Skip the link to the homepage
            if url == self.base_url:
                continue
            # Build the full URL of the page
            url = response.urljoin(url)
            # Follow the first 20 links on the page
            if self.index < 20:
                yield scrapy.Request(url, self.parse_page)
            else:
                break

    def parse_page(self, response):
        # Extract the text content of the page
        content = response.css("body *::text").getall()
        # Concatenate the content into a single string
        content = ' '.join(content)
        # Save the content to a file in the DOC folder
        if self.index < 20:
            self.save_to_file(content)

    def save_to_file(self, content):
        try:
            # Get the output folder from the command line arguments
            outfolder = sys.argv[1]
            # Ensure the output folder ends with a slash
            outfolder = outfolder if outfolder.endswith(
                "/") else outfolder + "/"
            # Create the output folder if it doesn't exist
            if not os.path.exists(outfolder):
                os.mkdir(outfolder)
            # Generate the filename for the output file
            filename = outfolder + f"D{self.index + 1}.txt"
            # Open the file in write mode
            with open(filename, "w+") as file:
                # Write the content to the file
                file.write(content)
            # Increment the index
            self.index += 1
            print(str(self.index))
            # print(str(self.index))
        except Exception as e:
            print(f"{filename} File can not be created: {e}")


def run_spider(spider):
    # Configure logging for the crawl
    configure_logging()
    # Create an instance of CrawlerProcess
    process = CrawlerProcess()
    # Add the spider to the process
    process.crawl(spider)
    # Start the crawl
    process.start()


if __name__ == "__main__":
    # Run the spider
    run_spider(MySpider)
