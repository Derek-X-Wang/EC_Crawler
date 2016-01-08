from urllib.request import urlopen


class Downloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read().decode('UTF-8')
