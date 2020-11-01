import os
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
from utils import plot_image, load_image, save_mask


def get_number_of_closed_contours(contours):
    closed_contours = []
    for cnt in contours:
        if cv2.isContourConvex(cnt) == True:
            closed_contours.append(cnt)
        else:
            pass
    return len(closed_contours)


def find_laplacian_of_gaussian(image):
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    laplacian = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    result = cv2.convertScaleAbs(laplacian, alpha=2)
    return result


def find_second_largest_contour(thresh):
    contours, hierarchy = cv2.findContours(
        thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    contoursSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    mask = np.zeros(thresh.shape, np.uint8)
    cv2.drawContours(mask, contoursSorted, len(contoursSorted) - 2, 255, cv2.FILLED)
    return mask


def segment_image(image, raw_image, contrast_factors=[1.5, 0]):
    ret, thresh = cv2.threshold(image, 65, 200, 0)
    thresh = np.bitwise_and(thresh, raw_image)
    ret, thresh = cv2.threshold(thresh, 40, 150, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    result = find_second_largest_contour(thresh)

    while (result > 0).sum() < 20000:
        kernel = np.ones((3, 3), np.uint8)
        thresh = cv2.dilate(thresh, kernel, iterations=1)
        result = find_second_largest_contour(thresh)

    result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)
    result = cv2.medianBlur(result, 17)
    result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for segmentation of Gall Bladder Images")
    parser.add_argument("--img_path", type=str, default="img/", help="Path for the image folder")
    parser.add_argument("--det_path", type=str, default="det/", help="Path for the output masks folder")
    args = parser.parse_args()
    
    if(not os.path.exists(args.det_path)):
        os.mkdir(args.det_path)

    path = os.walk(args.img_path)
    for _, _, files in path:
        for file in files:
            output_name = file.split(".")[0] + ".png"
            image = load_image(args.img_path + file)
            raw_image = image.copy()

            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            image = cv2.filter2D(image, -1, kernel)
            image = cv2.GaussianBlur(image, (5, 5), 0)

            mask = segment_image(image, raw_image)
            # plot_image(mask)
            save_mask(mask, args.det_path, output_name)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
