from vidproc import videoprocessor as vps

titles = []
with open("./downloadlist.txt", "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

READ_DIR = r"./out/videos/"
WRITE_DIR = r"./out/processedvideos/"
TARGET_WIDTH = 640
TARGET_HEIGHT = 360
SAMPLING_RATE = 2
INITIAL_DISCARD_IN_SECONDS = 5
MAX_FRAME_COUNT = 200

for title in titles:
    vps.processvideo(READ_DIR + title + ".mp4", WRITE_DIR + title + ".mp4", TARGET_WIDTH, TARGET_HEIGHT, SAMPLING_RATE, INITIAL_DISCARD_IN_SECONDS, MAX_FRAME_COUNT)