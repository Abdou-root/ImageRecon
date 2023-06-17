import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from torchvision.datasets import ImageFolder

# Define the transformation for the test image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# Load the saved model
model = models.resnet50(weights='ResNet50_Weights.DEFAULT')
num_classes = 7  # Number of classes in your dataset
num_features = model.fc.in_features
model.fc = torch.nn.Linear(num_features, num_classes)
model.load_state_dict(torch.load('celebrity_model.pth'))
model.eval()

# Load the class labels
train_dataset = ImageFolder('data/train', transform=transform)


def predict(file_path):
    # Load and preprocess the test image
    test_image = Image.open(file_path).convert('RGB')
    test_image = transform(test_image).unsqueeze(0)

    # Make a prediction on the test image
    with torch.no_grad():
        outputs = model(test_image)
        _, predicted = torch.max(outputs.data, 1)
        predicted_class = train_dataset.classes[predicted.item()]

    return predicted_class


test_image_path = 'ang.jpg'
predicted_class = predict(test_image_path)
