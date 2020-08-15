from yscraper import youtubescraper as yes
import json

VIDEO_PATH = "./out/videos/"
JSON_FILE = "./out/data.json"

titles = []
with open("./downloadlist.txt", "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

infodict = {}
for title in titles:
    searchkey = title + " trailer"
    print(f"Now Working With [{searchkey}]")
    links = yes.getLinks(searchkey)
    infodict[title] = yes.getVideoInfo(links[0])
    yes.downloadVideo(links[0], VIDEO_PATH, title, width=360, extension="mp4")

with open(JSON_FILE, 'w') as fp:
    json.dump(infodict, fp, indent=4)