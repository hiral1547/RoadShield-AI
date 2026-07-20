import cv2
import pyttsx3
import threading
import time
from ultralytics import YOLO

# ======================================
# Load YOLO Model
# ======================================

MODEL_PATH = r"G:\My Drive\RoadShield-AI\models\yolov8_pothole-2\weights\best.pt"

model = YOLO(MODEL_PATH)

print("=" * 50)
print("RoadShield AI Started")
print("Press 'q' to Quit")
print("=" * 50)

# ======================================
# Open Webcam
# ======================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found!")
    exit()

# ======================================
# Voice Alert Settings
# ======================================

ALERT_INTERVAL = 3      # Speak every 3 seconds
DETECTION_MEMORY = 1.0  # Remember pothole for 1 second

last_alert_time = 0
last_detection_time = 0

# Prevent multiple speech threads
is_speaking = False


# ======================================
# Voice Alert Function
# ======================================

def speak_alert():
    global is_speaking

    is_speaking = True

    try:
        # Create a NEW engine every time
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)

        engine.say("Pothole Ahead")
        engine.runAndWait()

        engine.stop()

        del engine

    except Exception as e:
        print("Voice Error:", e)

    is_speaking = False


# ======================================
# Main Loop
# ======================================

while True:

    success, frame = cap.read()

    if not success:
        print("Cannot read frame.")
        break

    # ----------------------------------
    # YOLO Prediction
    # ----------------------------------

    results = model.predict(
        source=frame,
        conf=0.20,
        verbose=False
    )

    annotated_frame = results[0].plot()

    boxes = results[0].boxes

    current_time = time.time()

    # ----------------------------------
    # Detection Memory
    # ----------------------------------

    if len(boxes) > 0:

        last_detection_time = current_time

        print("Pothole Detected")

    pothole_present = (
        current_time - last_detection_time
        <= DETECTION_MEMORY
    )

    # ----------------------------------
    # Voice Alert Every 3 Seconds
    # ----------------------------------

    if pothole_present:

        if (
            current_time - last_alert_time >= ALERT_INTERVAL
            and not is_speaking
        ):

            print("🔊 Pothole Ahead")

            last_alert_time = current_time

            threading.Thread(
                target=speak_alert,
                daemon=True
            ).start()

    # ----------------------------------
    # Show Detection Window
    # ----------------------------------

    cv2.imshow(
        "RoadShield AI - Real-Time Detection",
        annotated_frame
    )

    # ----------------------------------
    # Press Q to Exit
    # ----------------------------------

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ======================================
# Cleanup
# ======================================

cap.release()
cv2.destroyAllWindows()

print("RoadShield AI Closed.")