import cv2
import numpy as np

# Define dictionary of known colors (in RGB format)
colors = {
    'Red': (255, 0, 0),
    'Green': (0, 255, 0),
    'Blue': (0, 0, 255),
    'Yellow': (255, 255, 0),
    'Cyan': (0, 255, 255),
    'Magenta': (255, 0, 255),
    'Orange': (255, 165, 0),
    'Purple': (128, 0, 128),
    'Brown': (139, 69, 19),
    'White': (255, 255, 255),
    'Black': (0, 0, 0),
    'Gray': (128, 128, 128)
}

def get_closest_color_name(b, g, r):
    # Convert to int to avoid overflow issues
    b, g, r = int(b), int(g), int(r)
    min_distance = float('inf')
    closest_color = "Unknown"
    for color_name, (cr, cg, cb) in colors.items():
        distance = np.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
    return closest_color

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2

    # Get the BGR color at the center pixel
    b, g, r = frame[center_y, center_x]

    # Predict color
    color_name = get_closest_color_name(b, g, r)

    # Show color name on screen
    cv2.putText(frame, f'{color_name}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (int(b), int(g), int(r)), 5)

    cv2.imshow("Color Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
