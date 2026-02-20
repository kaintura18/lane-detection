import cv2
import numpy as np

#img = cv2.imread('road.png')
cap = cv2.VideoCapture('lane.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output.mp4', fourcc, 24.0, (int(cap.get(3)), int(cap.get(4))))


def region_of_interest_mask(image, vertices):
    
    mask = cv2.fillPoly(np.zeros_like(image), vertices, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_lines(image, lines):
  if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
  return image

def make_coordinates(img, line_parameters):
    slope, intercept = line_parameters
    y1 = img.shape[0]
    y2 = int(y1 * 0.6)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(img, lines):
    left_fit = []
    right_fit = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope, intercept = parameters

            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))

    averaged_lines = []
    if left_fit:
        left_avg = np.average(left_fit, axis=0)
        averaged_lines.append([make_coordinates(img, left_avg)])
    if right_fit:
        right_avg = np.average(right_fit, axis=0)
        averaged_lines.append([make_coordinates(img, right_avg)])

    return averaged_lines


def process(img):
  height, width, _ = img.shape
  
  polygons = np.array([[
        (int(0.1*width), height),
        (int(0.45*width), int(0.6*height)),
        (int(0.55*width), int(0.6*height)),
        (int(0.9*width), height)
    ]], dtype=np.int32)
  
  grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(grey, (5, 5), 0)
  edges =cv2.Canny(blurred, 50, 150)

  region_of_interest = np.array([polygons], dtype=np.int32)
  croped_image = region_of_interest_mask(edges, region_of_interest)
  lines=cv2.HoughLinesP(croped_image, 2, np.pi/180, 140, minLineLength=40, maxLineGap=20)
  
  averaged_lines = average_slope_intercept(img, lines)
  lines_image = draw_lines(img, averaged_lines)
  return lines_image


while cap.isOpened():
    ret, img = cap.read()
    frame = process(img)
    cv2.imshow('frame', frame)
    output.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
output.release()
cv2.destroyAllWindows()
print("Processing complete. Output video saved as output.mp4")