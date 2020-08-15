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
    # pafy likes and dislikes do not work
    # info["likes"] = video.likes
    # info["dislikes"] = video.dislikes

    # manual scraping for likes and dislikes
    LIKE_REG = r'{"label":"([0-9,]*) likes"}'
    DISLIKE_REG = r'{"label":"([0-9,]*) dislikes"}'
    page = requests.get(url).text

    # find links using regex
    likes = re.findall(LIKE_REG, page)
    dislikes = re.findall(DISLIKE_REG, page)

    info["likes"] = int(likes[0].replace(',',''))
    info["dislikes"] = int(dislikes[0].replace(',',''))
    return info

def downloadVideo(url : str, path : str, filename : str, width = 360, extension = "mp4"):
    video = pafy.new(url)
    widthdels = []
    extensions = []
    index = -1
    # debugcounter = 0
    for strm in video.videostreams:
        # print(debugcounter, strm.resolution, strm.extension)
        # debugcounter += 1
        res = str(strm.resolution).split('x')
        widthdels.append(abs(int(res[1]) - width))
        extensions.append(1) if extension == strm.extension else extensions.append(0)
    
    mindelta = min(widthdels)
    if(sum(extensions) > 0):
        for i in range(len(widthdels) -1, -1, -1):
            if(widthdels[i] == mindelta and extensions[i] == 1):
                index = i
                break
    elif(sum(extensions) == 0):
        for i in range(len(widthdels) -1, -1, -1):
            if(widthdels[i] == mindelta):
                index = i
                break
    
    # print(f"FOUND OUT MATCHING INDEX TO BE {index}")
    # strm = video.streams[0]
    print(f"Target Video Resolution: {video.videostreams[i].resolution} and extension: {video.videostreams[i].extension}")
    vs = video.videostreams[i]
    strippedpath = path.rstrip('/').rstrip('\\').rstrip('/')
    vs.download(filepath=f"{strippedpath}/{filename}.{vs.extension}")
