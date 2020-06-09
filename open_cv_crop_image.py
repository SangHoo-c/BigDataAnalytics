import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_casecade = cv2.CascadeClassifier('./haarcascade_eye.xml')


def crop(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]

        # crop 된 이미지를 공통의 pixel 크기로 변경한다,
        cropped_resize = cv2.resize(cropped, dsize=(100, 100))
        # BGR 을 GRAY 로 변환 하면서 차원을 줄인다.
        # 100*100*3 --> 100*100*1 으로 줄어든다.
        cropped_resize_grey = cv2.cvtColor(cropped_resize, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("images/sh_/cropped" + str(imgnum) + ".png", cropped_resize_grey)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_casecade.detectMultiScale(roi_gray)
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


imgnum = 1
for i in range(0, 100):
    # open cv 에서 얼굴을 detect 하지 못하는 경우, error 를 발생시키기 때문에
    # try except 를 사용해서 오류를 건너뛰었다.
    if imgnum < 10:
        try:
            img = cv2.imread('./images/sh/00000' + str(imgnum) + ".jpg")
            print("imgnum: " + str(imgnum))
            crop(img)
        except:
            img = cv2.imread('./images/sh/00000' + str(imgnum - 1) + ".jpg")
            print("imgnum: " + str(imgnum))
            crop(img)

    elif imgnum >= 10:
        try:
            img = cv2.imread('./images/sh/0000' + str(imgnum) + ".jpg")
            print("imgnum: " + str(imgnum))
            crop(img)
        except:
            img = cv2.imread('./images/sh/0000' + str(imgnum - 1) + ".jpg")
            print("imgnum: " + str(imgnum))
            crop(img)
    else:
        continue

    imgnum += 1

cv2.imshow('Image view', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
