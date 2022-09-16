# 0x01 Image Live Hand Tracking 

## Demo
Live hand tracker using OpenCV and Medipipe 

![demo]

## Files 

- cv2_get_fps.py 
> POC for testing the openCV and getting the frames per second
- image-live-hand-tracking.py
> raw code that makes the logic works 
- hand-detector-module.py
> refactored the script to be able to used as a module for future projects 


## Setup 

```bash
python --version
Python 3.10.6

python -m venv .venv
source .venv/bin/activate

pip install requirements.txt
```



references:
- https://google.github.io/mediapipe/


[demo]: 0x01-live-handtracking-demo.gif