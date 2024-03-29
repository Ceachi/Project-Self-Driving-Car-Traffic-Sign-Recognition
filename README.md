# **Traffic Sign Recognition** 

In this project, we use convolutional neural networks to classify traffic signs. We 
will train a model so it can decode traffic signs from natural images by using 
the [German Traffic Sign Dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset). 

After the model is trained, we will then test model program on new images of traffic signs we find on 
the web.


THE WRITEUP TEMPLATE FOR THE PROJECT IS PRESENTED IN [Traffic_Sign_Classifier.ipynb](Traffic_Sign_Classifier.ipynb)

#### Examples of traffic sign classification
RGB images are converted to grayscale for processing
![][image0]


## Code & Files
### 1. Dependencies & environment

Anaconda is used for managing my [**dependencies**](https://github.com/udacity/CarND-Term1-Starter-Kit).

* Jupyter, NumPy, SciPy, scikit-learn, TensorFlow, Matplotlib, Pandas, Python3.5
* OS: Ubuntu 16.04 (should work on other platform too)

### 2. My project files

* [Traffic_Sign_Classifier.ipynb](Traffic_Sign_Classifier.ipynb) is the main code for demos.

* [images](images) folder contains the test images.

* [data](data) folder user should download training and testing pickled data and put them into this folder.

### 3. How to run the code

(1) Download German Traffic Sign Dataset: [training data](https://drive.google.com/open?id=0B5WIzrIVeL0WR1dsTC1FdWEtWFE) 
and [test data](https://drive.google.com/open?id=0B5WIzrIVeL0WLTlPNlR2RG95S3c). This is a pickled dataset 
in which we've already resized the images to 32x32. Then save them into [data](data) folder.

(2) If you using Anaconda or miniconda, activate your environment which includes the dependencies by:
```sh
source activate your-conda-environment
```

(2) Load _jupyter notebook_ and then select the `Traffic_Sign_Classifier.ipynb` by:
```sh
jupyter notebook Traffic_Sign_Classifier.ipynb
```
