from ec_crawler import ec_url_manager
from ec_crawler import ec_downloader
from ec_crawler import ec_parser
from ec_crawler import ec_outputer


class CrawlerMain(object):

    def __init__(self):
        self.url = ec_url_manager.UrlManager()
        self.downloader = ec_downloader.Downloader()
        self.parser = ec_parser.Parser()
        self.outputer = ec_outputer.Outputer()

    def craw(self, root_url):
        count = 1
        self.url.add_new_url(root_url)
        while self.url.has_new_url():
            try:
                new_url = self.url.get_new_url()
                print("craw", count, ",", new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.url.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count += 1
            except:
                print("craw fail")
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    crawler = CrawlerMain()
    crawler.craw(root_url)
