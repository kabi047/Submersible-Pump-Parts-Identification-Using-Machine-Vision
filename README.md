# 🤖 Submersible Pump Parts Identification System

![Python](https://img.shields.io/badge/Python-3.14-blue) ![YOLOv8](https://img.shields.io/badge/Model-YOLOv8m--seg-green) ![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey) ![License](https://img.shields.io/badge/License-MIT-orange)

## 📝 Overview
This project is a high-performance computer vision application designed for industrial automation. It utilizes deep learning (**Instance Segmentation**) to detect, classify, and segment mechanical pump components in real-time.

The system is engineered to integrate with a **Gantry Robot** setup, providing precise visual feedback for automated handling, sorting, or quality inspection.

## 🚀 Key Features
* **Real-Time Performance:** Optimized for NVIDIA GPUs, achieving **75+ FPS** on RTX 4060 hardware.
* **High Precision:** Trained for 200 epochs on a custom dataset, achieving **99.5% accuracy** on critical components.
* **Instance Segmentation:** Utilizes `yolov8m-seg` to provide pixel-level masks, offering superior precision over standard bounding boxes.
* **Smart Tracking:** Implements object tracking logic (`persist=True`) to maintain stable IDs across video frames.
* **Standalone Deployment:** Packaged as a portable Windows executable (`.exe`) requiring no external Python or CUDA installation.

## 🛠️ Tech Stack
* **Core Model:** Ultralytics YOLOv8 (Medium-Segmentation Architecture)
* **Framework:** PyTorch (GPU-accelerated)
* **Language:** Python 3.14
* **Computer Vision:** OpenCV, NumPy
* **Packaging:** PyInstaller (Custom build with NVIDIA driver integration)

## 🔍 Supported Components
The model is trained to identify and segment the following industrial parts:
* ✅ Impellers
* ✅ NRV Cones & Stems
* ✅ Stage Casings
* ✅ Suction Housings
* ✅ Discharge Outlets
* ✅ Bushings & Washers

## 📊 Model Performance
| Metric | Value |
| :--- | :--- |
| **mAP50** | 98.4% |
| **Inference Time** | ~10ms (100 FPS potential) |
| **Training Epochs** | 200 |
| **Input Resolution** | 640x640 |
| **Precision** | High (Confidence Threshold > 0.60) |

## 💻 Installation & Usage

### Method 1: Portable Executable (Recommended for Users)
*No Python installation required.*
1.  Go to the **[Releases](../../releases)** section of this repository.
2.  Download the `Pump_Tool_Final.zip` file (Hosted on Google Drive due to size).
3.  Unzip the folder to your location of choice.
4.  Double-click **`START_APP.bat`**.
5.  The application will launch and open the camera feed automatically.

### Method 2: Running from Source (For Developers)
1.  Clone the repository:
    ```bash
    git clone [https://github.com/kabi047/Submersible-Pump-Parts-Identification-Using-Machine-Vision.git](https://github.com/kabi047/Submersible-Pump-Parts-Identification-Using-Machine-Vision.git)
    cd Submersible-Pump-Parts-Identification-Using-Machine-Vision
    ```
2.  Install dependencies:
    ```bash
    pip install ultralytics opencv-python numpy torch
    ```
3.  Run the main script:
    ```bash
    python main.py
    ```

## 📂 Project Structure
```text
├── main.py              # Main inference script with tracking logic
├── best.pt              # Trained YOLOv8m-seg model weights
├── data.yaml            # Dataset configuration
├── START_APP.bat        # Universal launcher for the portable app
└── README.md            # Project documentation
