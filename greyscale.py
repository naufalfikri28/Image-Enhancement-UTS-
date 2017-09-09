import cv2

image = cv2.imread('E:\Album\Rihlah Malang\Fikri.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('FikriGreyscale.jpg', gray)
