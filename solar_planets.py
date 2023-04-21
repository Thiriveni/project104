import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"SUN",(20,120),
            cv2.FONT_ITALIC,
            1.7,
            (255,255,255))

cv2.putText(img,"MERCURY",(80,200),
            cv2.FONT_ITALIC,
            0.7,
            (255,255,255)
            )

cv2.putText(img,"VENUS",
            (165,250),
            cv2.FONT_ITALIC,
            0.7,
            (255,255,255))

cv2.putText(img,"EARTH",
            (265,180),
            cv2.FONT_ITALIC,
            0.7,
            (255,255,255))

cv2.putText(img,"MARS",
            (365,240),
            cv2.FONT_ITALIC,
            0.7,
            (255,255,255))

cv2.putText(img,"JUPITER",
            (470,100),
            cv2.FONT_ITALIC,
            1,
            (255,255,255))

cv2.putText(img,"SATURN",
            (740,265),
            cv2.FONT_ITALIC,
            1,
            (255,255,255))

cv2.putText(img,"URANUS",
            (950,270),
            cv2.FONT_ITALIC,
            1,
            (255,255,255))

cv2.putText(img,
            "NEPTUNE",
            (1120,270),
            cv2.FONT_ITALIC,
            1,
            (255,255,255))








cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solare_systemwithname.jpg",img)