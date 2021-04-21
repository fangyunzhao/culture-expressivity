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

    files = [(os.path.join(video_dir,f), os.path.join(result_dir,os.path.splitext(f)[0]+'.csv')) for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir,f))]

    target_emotions = ['anger', 'fear', 'calm', 'sadness', 'happiness', 'surprise', 'disgust']
    model = FERModel(target_emotions, verbose=True)

    temp_file = os.path.join(result_dir,'temp_img.jpg')

    for (inF, outF) in files:
        cap = cv2.VideoCapture(inF)

        data = []

        flag = True
        frameId = 0
        while cap.isOpened() and flag:
            flag, frame = cap.read()

            if flag:
                cv2.imwrite(temp_file,frame)

                v = model.predict(temp_file)

                data.append([frameId,v])
                print(frameId)

                frameId += 1

        cap.release()

        df = pd.DataFrame(data, columns=['frameId','emotion'])
        df.to_csv(outF, index=False)
