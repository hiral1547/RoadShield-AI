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

## ✅ Day 7 – Real-Time Webcam Detection & Android Development Setup

## 🎯 Objectives

On Day 7 of the **RoadShield AI** project, the following objectives were completed:

- Configure the local development environment for real-time pothole detection.
- Load the trained YOLOv8 pothole detection model in VS Code.
- Perform real-time pothole detection using the system webcam.
- Prepare the environment for future Android mobile application development.
- Install Git for version control and project management.

---

# 🖥️ Development Environment Setup

## Google Drive for Desktop Integration

To access the trained YOLOv8 model directly from VS Code while maintaining synchronization with Google Drive, **Google Drive for Desktop** was installed.

After installation, Google Drive becomes available as a local drive on Windows.

Example structure:
G:
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


The trained YOLO model can now be accessed directly:

```python
from ultralytics import YOLO

model = YOLO(
    r"G:\My Drive\RoadShield-AI\models\yolov8_pothole-2\weights\best.pt"
)

Advantages
✅ Automatic synchronization with Google Drive.
✅ No need to manually transfer model files.
✅ Same model can be accessed from Google Colab and VS Code.
✅ Centralized storage for datasets, models, and project files.

🐍 Python Environment Configuration

During real-time webcam testing, an issue was observed where the OpenCV camera window was not closing properly using the q key.

One possible reason identified was the use of Python 3.14, which is a very recent Python release. Some AI and computer vision libraries such as:

- OpenCV
- PyTorch
- Ultralytics YOLO

may not yet have complete compatibility with the latest Python version.

Therefore, a dedicated Python 3.12 virtual environment was created.

Create Virtual Environment
Navigate to the project directory: cd D:\Hiral\pothole_detection

Create Python 3.12 environment: py -3.12 -m venv .venv

Activate Virtual Environment : .\.venv\Scripts\activate

After activation: (.venv) PS D:\Hiral\pothole_detection>

Upgrade pip: python -m pip install --upgrade pip

Install Required Libraries : python -m pip install ultralytics opencv-python torch torchvision
