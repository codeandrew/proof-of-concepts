#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 
import time 
# For Mac M1 chips pip install mediapipe-silicon
import mediapipe as mp  

cap = cv2.VideoCapture(0)
pTime = 0
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0 

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handsLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handsLms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y * h)
                # if
                cv2.circle(img, (cx, cy), 3, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handsLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime

    cv2.putText(img, f"FPS: { fps}" , (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0), 2)
    cv2.imshow("Test Image", img)
    cv2.waitKey(1)
    