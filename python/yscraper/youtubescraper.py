import requests
import re
import pafy
from bs4 import BeautifulSoup as bs

## REMEMBER TO REMOVE PYPETEER, LOCAL CHROMIUM AND REQUESTS_HTML AND MAYBE PAFY AND YTDL TOO

def getLinks(searchTitle : str) -> list:
    cleanedTitle = (searchTitle.strip()).replace(' ', '+')
    SEARCH_PRE = "https://www.youtube.com/results?search_query="
    VIDEO_REG = r'"/watch\?v=.*?"'
    YOUTUBE_BASE = "https://www.youtube.com"
    
    # craft url
    url = SEARCH_PRE + cleanedTitle
    # fetch page
    page = requests.get(url).text

    # find links using regex
    links = re.findall(VIDEO_REG, page)

    # format links
    links = [YOUTUBE_BASE + link.strip('"') for link in links]

    # return
    return links

def getVideoInfo(url : str) -> dict:
    video = pafy.new(url)
    info = {}
    info["title"] = video.title
    info["rating"] = video.rating
    info["author"] = video.author
    info["length"] = video.length
    info["viewcount"] = video.viewcount
    info["likes"] = video.likes
    info["dislikes"] = video.dislikes
    return info

def downloadVideo(url : str):
    video = pafy.new(url)
    strm = video.streams[0]
    vs = video.videostreams[-1]
    vs.download(filepath="./tmp/vid." + strm.extension)
