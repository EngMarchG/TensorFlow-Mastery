# Developing With TensorFlow
This repository tackles a variety of projects in order to get familiar with the TensorFlow Framework.

## [1. Regression With TensorFlow](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/1_Regression/01_Neural_Network_Regression_With_TensorFlow.ipynb)
This section introduces the basics of tensorflow and many methods that are incorporated in the framework from other modules. Later on, a simple introduction the steps to building a model using the Sequential Model approach.
The main takeaways are:
- Creating a Model, compiling it and fitting it
- Learning how to expand the dimensions or squeeze it 
- Predicting and Evaluating the model
- Understanding different optimizers and metrics

## [2. Classification With TensorFlow](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/2_Classification/02_Neural_Network_Classification_With_TensorFlow.ipynb)
This section further elaborates on the Sequential Modelling in TensorFlow. 
The key takeaways are:
- Tweak the model after evaluating it
- Visualize data to further understand it
- Finding the best learning rate (around 10x before the lowest point)
- Building Binary and Multi-Class Classification Models

## [3. Computer Vision With TensorFlow](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/3_Computer%20Visision/03_Computer_Vision_With_TensorFlow.ipynb)
This section focuses preprocessing images into batches and building a CNN model:
The main points are:
- Using ImageDataGenerator from tensorflow to rescale images and batchify them
- Applying Data Augmentation to images 
- Building binary and multi-class classification models 
- Trying out custom data on the model

## [4. Transfer Learning With TensorFlow](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/4_Transfer%20Learning/04_Transfer_Learning.ipynb)
This section focuses on best practices when building a model for doing tasks:
- Setting up callbacks
- Loading pretrained models using [Tensor Hub](https://tfhub.dev/)
- Testing out ResNet vs Efficientnet
- Using less validation data during fitting to speed up the process

## [5. Transfer Learning With TensorFlow Part 2](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/5_Transfer%20Learning%20Part%202/05_Transfer_Learning_P2.ipynb)
This section attempts to compare the results of a pre-trained model by adding new parameters:
- Trying varying amounts of train data
- Implementing data augmentation 
- Fine-Tuning the loaded pre-trained model
- Utulizing the full data

## [6. Transfer Learning With TensorFlow Part 3](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/6_Transfer%20Learning%20Part%203/06_Transfer_Learning_p3.ipynb)
This section attempts to tackle a much bigger dataset (10x the previous section) with different models:
- Trying varying amounts of train data
- Visualizing each step of the process with different visual techniques
- Finding the most wrong predictions (model-driven data exploration)

## [7. Transfer Learning Capstone](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/7_Transfer_Learning_Capstone/07_Food_Vision_Big_Milestone_Project_.ipynb)
This section attempts to build a baseline for you to improve on:
- Building a pre-trained baseline model for the Kaggle 101 Food dataset (70% accuracy)
- Fine-Tune the built model to beat the baseline (73% accuracy)
- Try improving the model even further? (Add dropout layers, further augmentation, longer training time, unfreeze more layers)
- Load and test model made in the notebook for less clutter. How about custom data?
- Try different architectures e.g EfficientNetv2 (try to avoid the larger models like sticking to B0/lite versions)
- After even further improvements 75% accuracy, EfficientNetv2 77% accuracy

## [8. NLP with TensorFlow](https://github.com/EngMarchG/TensorFlow-Mastery/blob/master/8_NLP_With_TensorFlow/08_NLP_with_TensorFlow_Introduction.ipynb)
This section introduces the field of NLP and its implementation in TensorFlow:
- Creating a tokenization vector (mapping words to numbers)
- Building an embedding layer (creating a feature vector matrix for each token)
- Utulizing bidirectional layers
- Transfer Learning with pre-trained models
