import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = imageRGB.shape

# Rectangle 1 
rect1_width, rec1_height = 180, 120
top_left1 = (40, 40)

bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rec1_height)
cv2.rectangle(imageRGB, top_left1, bottom_right1, (0,255,255), 3)

# Rectangle 2 
rect2_width, rect2_height = 220,160
top_left2 = (width - rect2_width - 40, height - rect2_height - 40)

bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(imageRGB, top_left2, bottom_right2, (255,0,255), 3)

# Circles at centers
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rec1_height // 2

center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_height // 2

cv2.circle(imageRGB, (center1_x, center1_y), 20, (0,255,0), -1)
cv2.circle(imageRGB, (center2_x, center2_y), 20, (0,255,0), -1)

# Line connecting centers
cv2.line(imageRGB, (center1_x, center1_y), (center2_x, center2_y), (0,255,0), 3)

# Text annotations
font = cv2.FONT_HERSHEY_COMPLEX

cv2.putText(imageRGB, 'region 1', (top_left1[0], top_left1[1]-15),
            font, .8, (255,255,255), 2, cv2.LINE_AA)

cv2.putText(imageRGB, 'region 2', (top_left2[0], top_left2[1]-15),
            font, .8, (255,255,255), 2, cv2.LINE_AA)

cv2.putText(imageRGB, 'center 1', (center1_x-50, center1_y+45),
            font, .7, (0,0,255), 2, cv2.LINE_AA)

cv2.putText(imageRGB, 'center 2', (center2_x-50, center2_y-45),
            font, .7, (255,255,255), 2, cv2.LINE_AA)

# Bi-directional arrows 
arrow_start = (width-70, 40)
arrow_end = (width-70, height-40)

cv2.arrowedLine(imageRGB, arrow_start, arrow_end, (255,255,0), 3, tipLength=0.07)
cv2.arrowedLine(imageRGB, arrow_end, arrow_start, (255,255,0), 3, tipLength=0.07)


width_label_position = (arrow_start[0]-160, (arrow_start[1]+arrow_end[1])//2)

cv2.putText(imageRGB, f'width: {width}px',
            width_label_position, font, .9, (255,255,0), 2, cv2.LINE_AA)

plt.figure(figsize=(12,8))
plt.imshow(imageRGB)
plt.title("Annotated Image")
plt.axis('off')
plt.show()