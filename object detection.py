import cv2
import time
# video capture to capture video 0-for web cam,1-some external web cam,2-.....so on for different camersa
# for vedion fies give file location in doube quots
first_frame = None
video = cv2.VideoCapture(0)
while True:
    # check a boolean variable to check if video is on
    # frame captures frame of video
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(
        delta_frame, 100, 255, cv2.THRESH_BINARY_INV)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    (cnts, __) = cv2.findContours(thresh_frame.copy(),
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("gray frame", gray)
    cv2.imshow("delta frame", delta_frame)
    cv2.imshow("threshold frame", thresh_frame)
    cv2.imshow("color", frame)

    key = cv2.waitKey(10)
    print(gray)
    print(delta_frame)
    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()

