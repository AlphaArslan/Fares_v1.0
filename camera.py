###################################### import
import cv2

###################################### Camera class
class Camera():
    def __init__(self, ID):
        self.stream = cv2.VideoCapture(ID, cv2.CAP_DSHOW)

    def __del__(self):
        self.stream.release()

    def get_image(self):
        print("[CAM] getting image ...")
        ret, img = self.stream.read()
        if ret:
            print("[CAM] returned an image")
            im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            print("[CAM] no image")
            im_rgb = [0]
        return im_rgb

###################################### test
if __name__ == '__main__':
    print("[TEST] starting test")
    cam = Camera(0)
    img = cam.get_image()
    if len(img) > 1:
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
