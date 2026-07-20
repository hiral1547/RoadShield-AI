import cv2
from ultralytics import YOLO

# -----------------------------
# Load Trained Model
# -----------------------------
model = YOLO("G:\My Drive\RoadShield-AI\models\yolov8_pothole-2\weights/best.pt")

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found!")
    exit()

print("Camera started successfully.")
print("Press 'q' to quit.")

# -----------------------------
# Real-Time Detection Loop
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot read frame.")
        break

    # YOLO Prediction
    results = model.predict(
        source=frame,
        conf=0.5,
        verbose=False
    )

    # Draw Bounding Boxes
    annotated_frame = results[0].plot()

    # Display Output
    cv2.imshow("RoadShield AI - Real-Time Detection", annotated_frame)

    # Press q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()

print("Program Closed.")