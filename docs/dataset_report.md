# Dataset Report

## Project Information

**Project Name:** RoadShield AI  
**Tagline:** *Saving lives by detecting dangerous potholes before people reach them.*

---

# 1. Objective

The objective of this dataset is to train an Object Detection model (YOLO) capable of detecting potholes 
from road images captured using a smartphone camera. The trained model will later be deployed for real-time 
pothole detection and voice alerts.

---

# 2. Dataset Source

- **Platform:** Roboflow Universe
- **Dataset Type:** Object Detection
- **Annotation Format:** YOLO
- **Class:** Pothole

---

# 3. Dataset Directory Structure

```
pothole_dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

---

# 4. Dataset Split

| Dataset Split | Description |
|---------------|-------------|
| Train | Used for training the YOLO model |
| Validation | Used during training to monitor model performance |
| Test | Used for final evaluation of the trained model |

---

# 5. Image Format

- Image Type: JPG / JPEG / PNG
- Color Format: RGB
- Resolution: Varies by image

---

# 6. Annotation Format

Each image has a corresponding text file inside the **labels** folder.

Example:

```
0 0.512 0.437 0.182 0.146
```

where

| Value | Description |
|--------|-------------|
| 0 | Class ID (Pothole) |
| 0.512 | Normalized X-center |
| 0.437 | Normalized Y-center |
| 0.182 | Normalized Width |
| 0.146 | Normalized Height |

All coordinates are normalized between **0 and 1**.

---

# 7. Dataset Classes

| Class ID | Class Name |
|----------|------------|
| 0 | Pothole |

Number of Classes: **1**

---

# 8. Label Visualization

The annotations were verified using OpenCV by drawing bounding boxes on the images.

Verification process:

1. Read image.
2. Read corresponding YOLO label file.
3. Convert normalized coordinates into pixel coordinates.
4. Draw bounding boxes.
5. Display annotated image.

This confirms that the dataset labels are correctly aligned with the potholes.

---

# 9. Data Configuration File

The dataset contains a `data.yaml` file used by YOLO during training.

Example structure:

```yaml
train: train/images
val: valid/images
test: test/images

nc: 1

names:
  0: pothole
```

---

# 10. Tools Used

- Python
- Google Colab
- OpenCV
- Matplotlib
- Roboflow
- GitHub

---

# 11. Dataset Verification

The following checks were successfully performed:

- Google Drive mounted
- Dataset loaded successfully
- Images accessed successfully
- Label files accessed successfully
- Bounding boxes displayed correctly
- Training, validation, and testing folders verified

---

# 12. Future Work

The verified dataset will be used to:

- Train a YOLO Object Detection model.
- Evaluate model accuracy using validation and test datasets.
- Perform real-time pothole detection.
- Generate voice alerts such as:
  > **"Pothole Ahead! Slow Down."**
- Deploy the trained model on a smartphone-based RoadShield AI application.

---

# Conclusion

The pothole dataset has been successfully explored and verified. Images and annotations are correctly organized in YOLO format, making the dataset ready for training an object detection model in the next phase of the RoadShield AI project.
