import cv2

if __name__ == "__main__":
    image = cv2.imread("assg1_release/val/img/0000.jpg")
    edges = cv2.Canny(image, 100, 255)
    cv2.imshow("image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
