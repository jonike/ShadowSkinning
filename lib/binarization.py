import cv2


def to_binary_image(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    return binary


def to_binary_inv_image(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, binary_inv = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    return binary_inv
