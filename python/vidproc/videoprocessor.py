import cv2
import numpy as np

def processvideo(filepath : str, output: str, target_width = 640, target_height = 360, sampling_rate = 2, initial_discard_in_seconds = 5, maximum_frame_count = 200):
    cap = cv2.VideoCapture(filepath)
    src_fps = cap.get(cv2.CAP_PROP_FPS)

    discard_frame_count = initial_discard_in_seconds * round(src_fps)
    frame_skip = round(src_fps) / sampling_rate
    #frame_end = (MAX_FRAME_COUNT / SAMPLING_RATE) * round(src_fps)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, sampling_rate, (target_width, target_height))

    counter = 0
    counter2 = 0
    sample_frame = None
    sample_collected = False
    while True:
        counter += 1
        ret, frame = cap.read()
        if ret == True:
            if (counter > discard_frame_count) and (counter % frame_skip == 0):
                counter2 += 1
                b = cv2.resize(frame,(target_width, target_height),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
                if not sample_collected:
                    sample_frame = b
                    sample_collected = True
                out.write(b)
            if(counter2 == maximum_frame_count):
                break
        else:
            break
        
    if(counter2 < maximum_frame_count):
        black_frame = sample_frame * 0
        for i in range(maximum_frame_count - counter2):
            out.write(black_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()