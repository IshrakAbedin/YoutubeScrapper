from yscraper import youtubescraper as yes
import json

VIDEO_DIR = "./out/videos/"
JSON_PATH = "./out/data.json"

titles = []
with open("./downloadlist.txt", "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

infodict = {}
count = 1
for title in titles:
    searchkey = title + " trailer"
    print(f"Now working with \033[95m[{searchkey}]\033[0m")
    links = yes.getLinks(searchkey)
    infodict[title] = yes.getVideoInfo(links[0])
    yes.downloadVideo(links[0], VIDEO_DIR, title, width=360, extension="mp4")
    print(f"\033[94mCompleted {count}/{len(titles)}|{count * 100 / (len(titles))}%\033[0m")
    count += 1

with open(JSON_PATH, 'w') as fp:
    json.dump(infodict, fp, indent=4)