import os
import sys
import cv2
import numpy as np
import pandas as pd

from tqdm import tqdm
from EmoPy.src.fermodel import FERModel


if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.exit("Usage: python3 process_emotions.py <video directory> <results directory>")

    video_dir = sys.argv[1]
    result_dir = sys.argv[2]

    files = [(os.path.join(video_dir,f), os.path.join(result_dir,f)) for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir,f))]

    target_emotions = ['anger', 'fear', 'calm', 'sadness', 'happiness', 'surprise', 'disgust']
    model = FERModel(target_emotions, verbose=True)

    for (inF, outF) in files:
        cap = cv2.VideoCapture(inF)
        while cap.isOpened():
            ret, frame = cap.read()
            print(ret)

            v = model.predict(frame)
            print(v)
            break

        cap.release()
        break
