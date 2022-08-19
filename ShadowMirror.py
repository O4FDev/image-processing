from random import randint
import cv2
import numpy as np


def takePicture():
    """
    @requires(Camera input)
    Take a picture with the camera input.
    """
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    img = cv2.resize(img, (600, 600))
    return img


def calculate_processed_values(img):
    sub_group_size = 10
    sub_group_total_y = img.shape[0] // sub_group_size
    sub_group_total_x = img.shape[1] // sub_group_size
    sub_group_total = sub_group_total_y * sub_group_total_x

    sub_group_radius = []
    sub_group_coords = []
    colours = []

    for y in range(sub_group_total_y):
        for x in range(sub_group_total_x):
            # Create a subgroup
            sub_group = img[y * sub_group_size, x * sub_group_size]
            # Calculate the average brightness of the subgroup.
            brightness = np.average(sub_group)
            # Calculate the radius of the circle to be rendered.
            radius = brightness / (sub_group_total*4)
            # Append the radius to the list.
            sub_group_radius.append(radius)
            # Append the coordinates of the subgroup to the list.
            sub_group_coords.append((x * sub_group_size, y * sub_group_size))
            # Depending on the y and x coordinates, the colour will be different starting from the top left.
            colours.append(
                (x * sub_group_size, y * sub_group_size, brightness))
            # colours.append(np.array([brightness, brightness, brightness]))
    return sub_group_radius, sub_group_coords, colours


def create_new_image(img, sub_group_radius, sub_group_coords, colours):
    new_img = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for i in range(len(sub_group_radius)):
        # Convert radius to an int
        radius = int(sub_group_radius[i] * img.shape[0])
        # Draw a circle at the coordinates of the subgroup
        cv2.circle(new_img, sub_group_coords[i], radius, colours[i], -1)
    return new_img


def convertImage():
    """
    Apply a dot filter to the image.
    """

    img = takePicture()
    # img = cv2.imread("turing.jpeg")

    sub_group_radius, sub_group_coords, colours = calculate_processed_values(
        img)

    new_img = create_new_image(
        img, sub_group_radius, sub_group_coords, colours)

    # Save the new image.
    cv2.imwrite('new_image' + str(randint(1, 1000000000000)) + '.jpg', new_img)


convertImage()
