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

# import cv2
# import numpy as np

# TARGET_WIDTH = 640
# TARGET_HEIGHT = 360
# SAMPLING_RATE = 2
# INITIAL_DISCARD_IN_SECONDS = 5
# MAX_FRAME_COUNT = 200

# cap = cv2.VideoCapture("./out/videos/The Trial of The Chicago 7.mp4")
# src_fps = cap.get(cv2.CAP_PROP_FPS)

# discard_frame_count = INITIAL_DISCARD_IN_SECONDS * round(src_fps)
# frame_skip = round(src_fps) / SAMPLING_RATE
# #frame_end = (MAX_FRAME_COUNT / SAMPLING_RATE) * round(src_fps)

# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('./out/processedvideos/The Trial of The Chicago 7.mp4',fourcc, SAMPLING_RATE, (TARGET_WIDTH, TARGET_HEIGHT))

# counter = 0
# counter2 = 0
# sample_frame = None
# sample_collected = False
# while True:
#     counter += 1
#     ret, frame = cap.read()
#     if ret == True:
#         if (counter > discard_frame_count) and (counter % frame_skip == 0):
#             counter2 += 1
#             b = cv2.resize(frame,(TARGET_WIDTH, TARGET_HEIGHT),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
#             if not sample_collected:
#                 sample_frame = b
#                 sample_collected = True
#             out.write(b)
#         if(counter2 == MAX_FRAME_COUNT):
#             break
#     else:
#         break
    
# debug_counter = 0
# if(counter2 < MAX_FRAME_COUNT):
#     black_frame = sample_frame * 0
#     for i in range(MAX_FRAME_COUNT - counter2):
#         debug_counter += 1
#         out.write(black_frame)

# print(debug_counter)

# cap.release()
# out.release()
# cv2.destroyAllWindows()