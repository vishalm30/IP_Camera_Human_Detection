import cv2

# print("Before URL")
cap = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov')
# https://security.world/rtsp/
# print("After URL")

while True:

    # print('About to start the Read command')
    ret, frame = cap.read()
    # print('About to show frame of Video.')
    cv2.imshow("Capturing", frame)
    # print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
