# Soal

## Learning Outcome

- **LO 1:** Execute structured deep learning experimentation workflows, including data preparation, model training, and evaluation
- **LO 2:** Construct deep learning models using modern programming tools and frameworks
- **LO 3:** Analyze the behavior and performance of theoretical and practical deep learning models under various training scenarios
- **LO 4:** Evaluate the suitability and limitations of different deep learning approaches for solving real-world problems across domains

## I. Case (100%)

### 1. [LO 1, LO 2, LO 3, LO 4 – 30 points] Deep learning for room temperature prediction

Instruction:

1. Clone the following repository: <https://github.com/wawancenggoro/Room-Climate-Datasets>
2. Add your student ID in `get_dataset_part.ipynb` in the repository, then run the notebook
3. Use the files as printed in the notebook as your dataset

TODOS:

a. [10 points] Construct and train a deep learning model with temperature, relative humidity, light sensor 1, and light sensor 2 as input, and the temperature of the next timestamp (next row in the csv files) as the label. You can set each of the hyperparameters to any value.
b. [5 points] Plot the training and validation losses over epochs, analyze and explain what happens in the training based on the plot.
c. [10 points] Do hyperparameter tuning to improve the deep learning model based on the result of point b and any other results you get from the training process.
d. [5 points] Test the model on a separate test set with appropriate metrics

### 2. [LO 1, LO 2, LO 3, LO 4 – 70 points] Deep learning for AI-generated image prediction

Instruction:

1. Clone the following repository: <https://github.com/wawancenggoro/CIFAR-100-dataset>
2. Add your student ID in `get_class_to_work.ipynb` in the repository, then run the notebook
3. Use the class as printed in the notebook from the train folder as your training dataset

TODOS:

a. [10 points] Construct and train a deep learning model as an image generator by using the images in your training dataset to train the model.
b. [5 points] Plot the training and validation losses over epochs, analyze, and explain what happened in the generative training based on the plot.
c. [10 points] Generate 500 images by using the trained model from point a.
d. [5 points] Compare 10 generated images and 10 original images, analyze and explain the comparison.
e. [10 points] Construct a new dataset for classification with 2 classes: original and fake. Use your original training dataset as the original class and the generated images from point b as the fake class.
f. [10 points] Construct and train a deep learning model to classify original versus fake images by using the dataset from point d.
g. [5 points] Plot the training and validation losses over epochs, analyze, and explain what happened in the classification training based on the plot.
h. [10 points] Do hyperparameter tuning to improve the deep learning model based on the result of point b and any other results you get from the training process.
i. [5 points] Test the classification model on a separate test set with appropriate metrics.

*Good Luck*
