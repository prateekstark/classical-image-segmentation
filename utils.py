import matplotlib.pyplot as plt
import cv2


def plot_image(image):
    plt.imshow(image)
    plt.show()


def load_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    print("Dimension of Image:", image.shape)
    # plot_image(image)
    print("Image loaded...")
    return image


def save_mask(image, output_folder, output_name):
    cv2.imwrite(output_folder + output_name, image)
    print(output_folder + output_name)
    print("Mask saved")
