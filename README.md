### ReconAI: Celebrity Image Recognition System

ReconAI is an advanced artificial intelligence(AI) project designed to recognize and classify images of celebrities using deep learning techniques. Built with Python and leveraging powerful libraries such as PyTorch, PIL, and Tkinter, ReconAI provides an intuitive graphical user interface (GUI) for users to easily interact with the system. This project demonstrates the capabilities of convolutional neural networks (CNNs) for image recognition tasks.

#### Project Structure
- **data/**: Directory containing the training and testing datasets.
  - **train/**: Training data set with images of various celebrities.
  - **test/**: Testing data set used to evaluate the model's performance.
- **utils/**: Contains utility scripts including the GUI and model prediction functionality.
  - **gui.py**: Script for the graphical user interface allowing users to select an image for recognition.
  - **model_training.py**: Training script for the CNN model using PyTorch.
  - **prediction.py**: Script for predicting the celebrity in a given image.
  - **preprocessing.py**: Script for preprocessing the dataset into a suitable format for training and testing.
- **celebrity_model.pth**: The trained PyTorch model for celebrity recognition.

#### Installation
To run ReconAI, you will need Python 3.6 or above. Ensure you have the following packages installed:
- PyTorch
- torchvision
- PIL (Pillow)
- Tkinter
- ttkbootstrap

You can install these dependencies using pip:
```bash
pip install torch torchvision Pillow tk ttkbootstrap
```

#### Training the Model
If you wish to retrain the model with a custom dataset, place your images in the `data/` directory following the existing structure, then run:
```bash
python utils/model_training.py
```
This will train a new model and save it as `celebrity_model.pth` in the project root.

#### Prediction
For direct prediction without using the GUI, you can use the `prediction.py` script:
```bash
python utils/prediction.py
```
Make sure to modify the `test_image_path` variable in the script to point to the image you want to predict.

#### Running the GUI
To start ReconAI, navigate to the project directory and run the `main.py` script:
```bash
python main.py
```
The GUI will open, allowing you to browse and select an image for celebrity recognition. The model's prediction will be displayed in the interface.



#### How It Works
ReconAI uses a ResNet50 model pre-trained on ImageNet and fine-tuned on the celebrity dataset provided. The model is trained to classify images into different celebrity categories based on the dataset structure under `data/train` and `data/test`.

The GUI script `gui.py` provides a user-friendly interface for interacting with the system, allowing users to upload images and view the recognition results instantly. 

---

We hope you enjoy using ReconAI for your celebrity recognition needs. Your feedback and contributions are welcome to improve and expand the project's capabilities.
