# RoadShield AI

RoadShield AI is a smartphone-based AI system that detects potholes using computer vision and the YOLO object detection model.

## Features

- Real-time pothole detection
- Bounding box visualization
- Voice alerts
- GPS location logging
- Smartphone deployment

## Technologies

- Python
- OpenCV
- YOLO
- Google Colab
- GitHub

## Repository Structure

RoadShield-AI/
├── assets/
├── dataset/
├── docs/
├── models/
├── notebooks/
├── outputs/
└── README.md


# Development Progress

## ✅ Day 1

- Created GitHub repository
- Created Google Drive project structure
- Set up Google Colab
- Installed required libraries
- Successfully read and displayed road images using OpenCV

---

## ✅ Day 2

- Selected pothole dataset
- Uploaded dataset to Google Drive
- Verified dataset structure
- Inspected `data.yaml`
- Displayed sample images
- Verified YOLO annotations
- Created dataset summary notebook

---

## Development Progress

### ✅ Day 3

- Dataset validated
- Checked missing labels
- Verified image sizes
- Visualized annotations
- Created dataset report


### ✅ Day 4 YOLO Training Code Explanation

## Training Code

```python
results = model.train(
    data=yaml_path,
    epochs=4,
    imgsz=640,
    batch=16,
    project="/content/drive/MyDrive/RoadShield-AI/models",
    name="yolov8_pothole"
)
```

---

## 🔹 `results =`

- Stores the training result returned by YOLO.
- It can be used later to access training information and metrics.

---

## 🔹 `model.train()`

- Starts training the YOLO model using the given dataset and training settings.

---

## 🔹 `data = yaml_path`

- Specifies the path to the **`data.yaml`** file.
- YOLO reads this file to know:
  - 📂 Training images location
  - 📂 Validation images location
  - 📂 Test images location
  - 🏷️ Class names

---

## 🔹 `epochs = 4`

- The model learns from the **entire dataset 4 times**.
- **1 Epoch = 1 complete pass through all training images.**
- It's like reading one book 4 times
---

## 🔹 `imgsz = 640`

- Resizes every image to **640 × 640 pixels** before training.
- All images must have the same size for the model.

---

## 🔹 `batch = 16`

- Processes **16 images together** in one training step.
- Batch size affects:
  - 🚀 Training speed
  - 💾 GPU memory usage
## Example: Batch Processing

  Suppose the dataset contains **160 training images** and the batch size is **16**.

  Then YOLO divides the dataset into batches like this:

```text
160 Images
│
├── Batch 1  → Images 1 - 16
├── Batch 2  → Images 17 - 32
├── Batch 3  → Images 33 - 48
├── Batch 4  → Images 49 - 64
├── Batch 5  → Images 65 - 80
├── Batch 6  → Images 81 - 96
├── Batch 7  → Images 97 - 112
├── Batch 8  → Images 113 - 128
├── Batch 9  → Images 129 - 144
└── Batch 10 → Images 145 - 160
```

### Summary

- **Total Images:** 160
- **Batch Size:** 16
- **Total Batches:** 10

**Formula:**

```
Number of Batches = Total Images ÷ Batch Size
                   = 160 ÷ 16
                   = 10
```

> **One Batch = One group of images processed together before the model updates its learning.**
---

## 🔹 `project="/content/drive/MyDrive/RoadShield-AI/models"`

- Specifies the folder where all training outputs will be saved.

Example output files:

- `best.pt`
- `last.pt`
- `results.png`
- `results.csv`
- `confusion_matrix.png`
- `PR_curve.png`
- `F1_curve.png`

---

## 🔹 `name="yolov8_pothole"`

- Creates a folder with this name inside the **project** folder.
- All files for this training run are stored in this folder.

Example:

```
models/
└── yolov8_pothole/
    ├── weights/
    │   ├── best.pt
    │   └── last.pt
    ├── results.png
    ├── confusion_matrix.png
    └── results.csv
```

---

# One-Line Summary

**This code trains the YOLO model using the pothole dataset for 4 epochs, resizes all images to 640×640, processes 16 images at a time, and saves the trained model and training results in the specified folder.**

---

## ✅ Day 5

- Loaded trained YOLO model (`best.pt`)
- Performed image inference
- Detected potholes in unseen images
- Learned confidence scores
- Studied Precision, Recall, and mAP
- Saved prediction results

# Training vs Inference in YOLOv8

---

## 1. Training Phase

During training, the YOLO model **learns** from labeled pothole images.

### Workflow

```text
Road Images + Labels
          │
          ▼
      Train YOLOv8
          │
          ▼
 Generate Trained Model
      (best.pt)
```
## 2. Inference Phase

Inference is the process of using the trained model to make predictions on new, unseen images.

```text
New Road Image
       │
       ▼
     best.pt
       │
       ▼
Detect Pothole
Draw Bounding Box
Confidence Score
```
Here, the model is using what it learned to detect potholes in a new image.

## ✅ Day 6

- Implemented pothole detection on recorded road videos
- Processed videos frame by frame using YOLO
- Generated output video with bounding boxes
- Learned how videos are processed as image sequences
- Prepared the project for real-time camera detection

# 📅 Day 7 – Real-Time Webcam Detection using YOLOv8
## RoadShield AI 🚧

### Project Goal

RoadShield AI aims to detect dangerous potholes in real-time using Artificial Intelligence and Computer Vision.

**Objective:**

"Saving lives by detecting dangerous potholes before people reach them."

---

## 🎯 Day 7 Objectives

On Day 7, the following tasks were completed:

- Configure the local environment for real-time pothole detection.
- Load the trained YOLOv8 pothole detection model.
- Perform real-time inference using webcam.
- Understand OpenCV-based live detection pipeline.
- Prepare Android development environment for future mobile deployment.
- Setup Git for project version control.

---

## 🛠️ Tools and Technologies Used

| Technology | Purpose |
|------------|---------|
| YOLOv8 | Object detection model |
| OpenCV | Webcam access and image processing |
| Python | Programming language |
| PyTorch | Deep learning framework |
| VS Code | Local development environment |
| Android Studio | Future mobile deployment |
| Git | Version control |

# 🖥️ Google Drive Integration

## Google Drive for Desktop

To access the trained YOLOv8 model directly from VS Code, Google Drive for Desktop was configured.

Google Drive appears as a local drive in Windows.

Example structure:
```text
G:\
│
└── My Drive
    │
    └── RoadShield-AI
        │
        ├── dataset
        │
        ├── models
        │
        └── notebooks
```

This allows the same trained model to be accessed from:

- Google Colab
- VS Code
- Local Python environment


### Advantages

✅ Automatic synchronization with Google Drive.

✅ No need to manually copy trained models.

✅ Central storage for datasets, models, and notebooks.

✅ Easy switching between cloud and local development.

# Import YOLO library

from ultralytics import YOLO

# 📦 Loading Trained YOLOv8 Model

The trained model file: best.pt contains learned pothole detection weights.
The model is loaded using Ultralytics YOLO.

# Example model loading path
# This path is used in local VS Code environment

model_path = r"G:\My Drive\RoadShield-AI\models\yolov8_pothole-2\weights\best.pt"

model = YOLO(model_path)

print("YOLOv8 Model Loaded Successfully")

# 🐍 Python Environment Configuration

## Problem Encountered

During webcam testing, the OpenCV camera window was not closing properly using the `q` key.

Possible reason:

Python 3.14 is a very recent release.

Some AI libraries may not yet have complete compatibility:

- OpenCV
- PyTorch
- Ultralytics

Therefore, a stable Python 3.12 environment was created.

# ⚙️ Python 3.12 Virtual Environment Setup

## Create Environment

Command: cd D:\Hiral\pothole_detection > py -3.12 -m venv .venv

## Activate Environment - 
..venv\Scripts\activate
After activation: (.venv) PS D:\Hiral\pothole_detection>

## Upgrade pip 
python -m pip install --upgrade pip

## Install Required Libraries
python -m pip install ultralytics opencv-python torch torchvision

# 🎥 Real-Time Webcam Detection

The trained YOLOv8 model was tested using a live webcam.

The detection pipeline:
```text
Webcam
|
↓
Capture Frame
|
↓
YOLOv8 Model
|
↓
Pothole Detection
|
↓
Bounding Box + Confidence Score
```
# ▶ Running Real-Time Detection
The application is executed locally using VS Code:
Command: python day7_realtime_camera.py

Expected output:
Camera started successfully.
Press 'q' to quit.

## 📷 Expected Webcam Window

When the application starts, an OpenCV window opens displaying the live webcam feed.

```text
+--------------------------------------------------+
|                                                  |
|        RoadShield AI - Real-Time Detection       |
|                                                  |
|              Live Webcam Feed                    |
|                                                  |
|        [ Webcam Video Stream ]                   |
|                                                  |
+--------------------------------------------------+
```

## 🚧 Pothole Detection Output

When the YOLOv8 model detects a pothole, a bounding box with the class name and confidence score appears on the live video.

Example:

```text
+--------------------------------------------------+
|                                                  |
|        RoadShield AI - Real-Time Detection       |
|                                                  |
|       ┌──────────────────────────┐               |
|       │       pothole 92%        │               |
|       └──────────────────────────┘               |
|                                                  |
+--------------------------------------------------+
```

The output contains:

- Bounding box
- Class name
- Confidence percentage

## How to quit the webcam?
OpenCV Window Focus
OpenCV receives keyboard input only when the webcam window is active.

Steps:
```text
    1. Open webcam window.
    2. Click inside the window.
    3. Press: q
```
# 📱 Android Development Environment Setup

Android Studio was installed for future RoadShield AI mobile application development.

Completed:
```text
✅ Android Studio installed
✅ Android SDK installed
✅ Android Emulator installed
✅ Android Virtual Device created
✅ Emulator tested successfully
```
SDK Location: C:\Users\DELL\AppData\Local\Android\Sdk

# ☕ Java Verification
Android development requires Java.
Check installation: java -version

# 🌿 Git Version Control

Git was installed for managing the RoadShield AI project.

Git will be used for:

- Source code management
- Version history
- Branch management
- Backup
- Future collaboration
- 
# Day 7 Summary
Completed:
```text
✅ Google Drive integration
✅ YOLOv8 model access from local environment
✅ Python 3.12 virtual environment setup
✅ Installed AI dependencies
✅ Real-time webcam detection implementation
✅ Investigated OpenCV webcam issue
✅ Android Studio setup
✅ Android emulator testing
✅ Git installation
```

# 📅 Day 8 – Real-Time Pothole Detection with Voice Alert

## 🎯 Objective

The objective of Day 8 was to develop a real-time pothole detection system using a webcam and integrate an offline voice alert mechanism. The system detects potholes using a custom-trained YOLOv8 model, displays bounding boxes around detected potholes, and announces "Pothole Ahead" at regular intervals to warn the user.

---

## ✅ Work Completed

### 1. Loaded the Trained YOLOv8 Model

- Loaded the custom-trained YOLOv8 pothole detection model (`best.pt`).
- Verified that the model initializes successfully before starting real-time detection.

---

### 2. Connected the Webcam

- Accessed the default webcam using OpenCV.
- Added a check to ensure the camera is available before running the application.

---

### 3. Implemented Real-Time Pothole Detection

- Captured live video frames continuously from the webcam.
- Passed each frame to the YOLOv8 model for inference.
- Detected potholes in real time using a confidence threshold of **0.20**.

---

### 4. Displayed Detection Results

- Drew bounding boxes around detected potholes.
- Displayed the annotated video stream in a live OpenCV window.
- Updated the detection results continuously as new frames were captured.

---

### 5. Integrated Offline Voice Alerts

- Used the **pyttsx3** library to generate offline text-to-speech alerts.
- Configured the application to announce:

> **"Pothole Ahead"**

whenever a pothole is detected.

---

### 6. Added Alert Interval

To avoid continuous and repetitive announcements:

- Introduced a **3-second alert interval**.
- The application now repeats the warning only once every three seconds while the pothole remains visible.

---

### 7. Implemented Detection Memory

Real-time object detection may occasionally miss detections for one or two frames due to camera movement or lighting conditions.

To improve stability:

- Implemented a **1-second detection memory**.
- The system remembers a recent pothole detection for a short duration.
- Prevents unnecessary interruptions in voice alerts caused by temporary missed detections.

---

### 8. Prevented Multiple Voice Threads

To ensure smooth execution:

- Added an `is_speaking` flag.
- Prevented multiple speech engines from running simultaneously.
- Ensured only one voice alert is spoken at a time.

---

### 9. Used Multithreading

Implemented Python threading for the voice alert system.

Benefits include:

- Smooth webcam video streaming
- Non-blocking speech execution
- Improved real-time application performance

---

### 10. Implemented Proper Resource Cleanup

When the user presses **Q**:

- Webcam is released.
- OpenCV windows are closed.
- The application terminates safely without leaving background processes.

---

## 📚 Concepts Learned

- Real-time computer vision
- YOLOv8 live inference
- Webcam video capture using OpenCV
- Offline text-to-speech with pyttsx3
- Python multithreading
- Detection memory for stable object detection
- Alert interval mechanism
- Safe resource management

---

## 📂 Project Structure

```text
RoadShield-AI
│
├── models
│   └── yolov8_pothole-2
│       └── weights
│           └── best.pt
│
├── notebooks
│   └── Day8_Real_Time_Detection.py
│
└── README.md
```

---

## 🎥 Output

The application performs the following operations:

- Opens the webcam.
- Detects potholes in real time.
- Draws bounding boxes around detected potholes.
- Announces **"Pothole Ahead"** through the speaker.
- Repeats the voice alert every **3 seconds** while the pothole remains visible.
- Stops announcing once the pothole is no longer detected.
- Closes the application safely when **Q** is pressed.

---

## 🚀 Skills Gained

- Real-Time AI Application Development
- YOLOv8 Deployment
- Computer Vision with OpenCV
- Offline Voice Alert Integration
- Python Multithreading
- Event-Based Alert System Design
- Real-Time Object Detection Pipeline

---

## 📅 Day 8 Summary

By the end of Day 8, a fully functional desktop prototype of **RoadShield AI** was developed. The application successfully performs real-time pothole detection using a webcam, displays live detection results, and provides offline voice alerts to notify users of upcoming potholes. This milestone establishes the core real-time detection pipeline and prepares the project for future enhancements such as GPS location tracking, mobile application integration, and cloud-based reporting.
