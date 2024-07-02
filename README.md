
# ReconAI: Celebrity Image Recognition System

## Overview
ReconAI is an artificial intelligence (AI) project aimed at recognizing and classifying celebrity images through deep learning. Utilizing Python and powerful libraries such as PyTorch, PIL, and Tkinter, it offers a user-friendly graphical interface (GUI), showcasing the strength of convolutional neural networks (CNN) in image recognition.

## Project Structure
### Directories
- **data/**: Houses training and testing datasets.
  - **train/**: Contains images of various celebrities for training.
  - **test/**: Holds images for evaluating the model's accuracy.
- **utils/**: Includes utility scripts for the GUI, model training, prediction, and preprocessing.
  - **gui.py**: Graphical user interface script for image selection.
  - **model_training.py**: Trains the CNN model with PyTorch.
  - **prediction.py**: Predicts the celebrity in an input image.
  - **preprocessing.py**: Prepares the dataset for training and testing.

### Model File
- **celebrity_model.pth**: The trained PyTorch model for celebrity recognition.

## Installation
ReconAI requires Python 3.6 or newer. Install the following packages:
- PyTorch
- torchvision
- PIL (Pillow)
- Tkinter
- ttkbootstrap

Use pip to install the dependencies:
```bash
pip install torch torchvision Pillow tk ttkbootstrap
```

## How to Use
### Training the Model
To train the model with a custom dataset:
1. Place your images in the `data/` directory, following the structure provided.
2. Run the following command to train and save the model:
```bash
python utils/model_training.py
```

### Making Predictions
For direct predictions without the GUI:
1. Adjust the `test_image_path` in `utils/prediction.py`.
2. Run:
```bash
python utils/prediction.py
```

### Running the GUI
To launch the ReconAI GUI:
1. Navigate to the project directory.
2. Execute:
```bash
python main.py
```
3. Use the GUI to select and predict celebrity images.

## How It Works
ReconAI employs a ResNet50 model, initially trained on ImageNet and fine-tuned using the provided celebrity dataset. It classifies images into celebrity categories based on the dataset under `data/train` and `data/test`. The GUI simplifies system interaction, enabling instant upload and recognition.

---

**Enjoy exploring ReconAI for your celebrity recognition projects! We welcome your feedback and contributions to further enhance and broaden the project.**
