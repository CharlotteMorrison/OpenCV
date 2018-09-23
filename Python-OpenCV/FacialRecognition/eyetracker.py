import cv2


class EyeTracker:
    def __init__(self, facecascadepath, eyecascadepath):
        self.faceCascade = cv2.CascadeClassifier(facecascadepath)
        self.eyeCascade = cv2.CascadeClassifier(eyecascadepath)

    def track(self, image):
        facerects = self.faceCascade.detectMultiScale(image,
                    scaleFactor=1.1, minNeighbors=5,
                    minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        rects = []

        for (fX, fY, fW, fH) in facerects:
            # face region of interest faceroi
            faceroi = image[fY:fY + fH, fX:fX + fW]
            rects.append((fX, fY, fX + fW, fY + fH))

            eyerects = self.eyeCascade.detectMultiScale(faceroi,
                        scaleFactor=1.1, minNeighbors=10,
                        minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

            for (eX, eY, eW, eH) in eyerects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

        return rects
