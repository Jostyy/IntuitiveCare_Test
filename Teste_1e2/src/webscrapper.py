from bs4 import BeautifulSoup
from pathlib import Path
import requests


class WebScrapper:
    def __init__(self, url):
        self.url = url

    # Search for href list of TISS files
    def get_recent_version_link(self):
        response = requests.get(self.url).text
        soup = BeautifulSoup(response, "html.parser")
        content = soup.find("div", {"id": "content-core"})
        return content.find("p", class_="callout").a['href']

    # Get link for specific file
    def get_file(self, link, tissfile):
        response = requests.get(link).text
        soup = BeautifulSoup(response, "html.parser")
        trs = soup.tbody
        for tr in trs.find_all('a'):
            if tissfile in tr.span.string:
                filelink = tr['href']
                break
        return filelink

    # Download the file from url
    def download_file(self, link, tissfile):
        fileurl = self.get_file(link, tissfile)
        filename = Path(fileurl.split("/")[-1])
        response = requests.get(fileurl, stream=True)
        filename.write_bytes(response.content)

    def scrappe(self, tissfile):
        link = self.get_recent_version_link()
        self.download_file(link, tissfile)
