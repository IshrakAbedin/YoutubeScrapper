from yscraper import youtubescraper as yes
from vidproc import videoprocessor as vps
from vidcomp import videocompressor as vcp
import json

# ------------------------------KEY SETTINGS------------------------------------
KEY_FILE_PATH = "./downloadlist.txt"
# ------------------------YOUTUBE SCRAPPER SETTINGS-----------------------------
VIDEO_DIR = "./out/videos/"
JSON_PATH = "./out/data.json"
DESIRED_WIDTH = 360
DESIRED_EXTENSION = "mp4"
# ------------------------VIDEO PROCESSOR SETTINGS------------------------------
VP_READ_DIR = "./out/videos/"
VP_WRITE_DIR = "./out/processedvideos/"
TARGET_WIDTH = 640
TARGET_HEIGHT = 360
SAMPLING_RATE = 2
INITIAL_DISCARD_IN_SECONDS = 5
MAX_FRAME_COUNT = 200
# ------------------------VIDEO COMPRESSOR SETTINGS------------------------------
VC_READ_DIR = "./out/processedvideos/"
VC_WRITE_DIR = "./out/compresseddata/"
XKEY = "video"
YKEY = "label"

################################################################################

#********************************KEY DRIVER***********************************
titles = []
with open(KEY_FILE_PATH, "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

#**********************YOUTUBE SCRAPPER DRIVER********************************
print("\033[1m\033[92m[SCRAPPING STAGE STARTED]\033[0m")
infodict = {}
count = 1
for title in titles:
    searchkey = title + " trailer"
    print(f"Now working with \033[95m[{searchkey}]\033[0m")
    links = yes.getLinks(searchkey)
    infodict[title] = yes.getVideoInfo(links[0])
    yes.downloadVideo(links[0], VIDEO_DIR, title, width=DESIRED_WIDTH, extension=DESIRED_EXTENSION)
    print(f"\033[94mCompleted {count}/{len(titles)}|{count * 100 / (len(titles))}%\033[0m")
    count += 1

with open(JSON_PATH, 'w') as fp:
    json.dump(infodict, fp, indent=4)

print("\033[1m\033[92m[SCRAPPING STAGE COMPLETED]\033[0m")

#**********************VIDEO PROCESSOR DRIVER********************************
print("\033[1m\033[92m[PROCESSING STAGE STARTED]\033[0m")
count = 1
for title in titles:
    print(f"Now processing \033[95m[{title}]\033[0m")
    vps.processvideo(VP_READ_DIR + title + "." + DESIRED_EXTENSION, VP_WRITE_DIR + title + "." + DESIRED_EXTENSION, TARGET_WIDTH, TARGET_HEIGHT, SAMPLING_RATE, INITIAL_DISCARD_IN_SECONDS, MAX_FRAME_COUNT)
    print(f"\033[94mCompleted {count}/{len(titles)}|{count * 100 / (len(titles))}%\033[0m")
    count += 1

print("\033[1m\033[92m[PROCESSING STAGE COMPLETED]\033[0m")

#**********************VIDEO COMPRESSOR DRIVER********************************
print("\033[1m\033[92m[COMPRESSION STAGE STARTED]\033[0m")
count = 1
for title in titles:
    print(f"Now compressing \033[95m[{title}]\033[0m")
    ldr = infodict[title]["likes"] / infodict[title]["dislikes"]
    vcp.compressvideo(VC_READ_DIR + title + "." + DESIRED_EXTENSION, VC_WRITE_DIR + title + ".hdf5", ldr, XKEY, YKEY)
    print(f"\033[94mCompleted {count}/{len(titles)}|{count * 100 / (len(titles))}%\033[0m")
    count += 1

print("\033[1m\033[92m[COMPRESSION STAGE COMPLETED]\033[0m")

################################################################################