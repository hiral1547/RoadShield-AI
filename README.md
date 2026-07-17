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

# 📌 One-Line Summary

**This code trains the YOLO model using the pothole dataset for 4 epochs, resizes all images to 640×640, processes 16 images at a time, and saves the trained model and training results in the specified folder.**

---

# 💡 Memory Trick

| Parameter | Easy Meaning |
|-----------|--------------|
| `results` | Stores the training output |
| `model.train()` | Starts model training |
| `data` | Dataset information (`data.yaml`) |
| `epochs` | Number of learning rounds |
| `imgsz` | Input image size |
| `batch` | Images processed together |
| `project` | Save location of training outputs |
| `name` | Folder name for this training run |
