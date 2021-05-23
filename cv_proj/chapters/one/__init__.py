import cv2

def display_img():
    img = cv2.imread("resources/paint.jpg")
    cv2.imshow("output", img)
    cv2.waitKey(0)

def use_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 100)

    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xDD ==ord('q'):
            break