import os
import shutil
import random as rnd

# Set the paths for your dataset
dataset_path = '../data'
train_path = '../data/train'
test_path = '../data/test'

# Creating train and test directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Set the percentage of images for training and testing
train_percentage = 0.7
test_percentage = 0.3

# Create train and test directories for each class
classes = ['Angelina Jolie', 'Brad Pitt', 'Denzel Washington', 'Hugh Jackman', 'Jennifer Lawrence', 'Johnny Depp',
           'Kate Winslet']
for class_name in classes:
    os.makedirs(os.path.join(train_path, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_path, class_name), exist_ok=True)
    image_dir = os.path.join(dataset_path, class_name)
    image_files = os.listdir(image_dir)
    rnd.shuffle(image_files)
    num_images = len(image_files)
    num_train_images = int(train_percentage * num_images)
    num_test_images = int(test_percentage * num_images)
    train_images = image_files[:num_train_images]
    test_images = image_files[num_train_images:]
    for train_image in train_images:
        shutil.copy(os.path.join(image_dir, train_image), os.path.join(train_path, class_name))
    for test_image in test_images:
        shutil.copy(os.path.join(image_dir, test_image), os.path.join(test_path, class_name))
