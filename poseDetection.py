import csv
import cv2
import time

from poseDetectionModule import PoseDetector, findCoordinates

cap = cv2.VideoCapture(0)
pTime = 0
TIME = time.time()
detector = PoseDetector()
x_values = []
y_values = []
while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=True)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        # print(lmList[14])

        # Right Leg -------------------------------------------
        x24, y24 = findCoordinates(img, 24, lmList)
        x26, y26 = findCoordinates(img, 26, lmList)
        x28, y28 = findCoordinates(img, 28, lmList)

        left_angle = detector.findAngle(img, 23, 25, 27, lmList)
        print(left_angle)


        x_ = pTime - TIME
        y_ = 360 - left_angle
        if x_ >= 0 and y_ >= 0:
            x_values.append(x_)
            y_values.append(y_)
        # x_values.append(pTime-TIME)
        # y_values.append(360 - left_angle)

        # print(360 - right_angle)
        a1, b1 = lmList[23][1:]
        a2, b2 = lmList[25][1:]
        a3, b3 = lmList[27][1:]
        cv2.circle(img, (a1, b1), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (a2, b2), 15, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (a3, b3), 15, (0, 0, 255), cv2.FILLED)

        # Left Leg -------------------------------------------
        x23, y23 = findCoordinates(img, 23, lmList)
        x25, y25 = findCoordinates(img, 25, lmList)
        x27, y27 = findCoordinates(img, 27, lmList)

        right_angle = detector.findAngle(img, 24, 26, 28, lmList)
        x1, y1 = lmList[24][1:]
        x2, y2 = lmList[26][1:]
        x3, y3 = lmList[28][1:]
        cv2.circle(img, (x1, y1), 15, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 15, (0, 255, 255), cv2.FILLED)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])
        writer.writerows(zip(x_values, y_values))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    # cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
