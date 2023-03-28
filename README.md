
![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
[![Build Status](https://travis-ci.org/anfederico/clairvoyant.svg?branch=master)](https://travis-ci.org/anfederico/clairvoyant)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

<a name="readme-top"></a>

# # Mini-MIAS images'cropping.

Mini-MIAS (Mini Mammographic Image Analysis Society) is a publicly available dataset of digitized mammograms for research purposes. It consists of 322 mammography images in bitmap format and their corresponding radiological reports, and it was created to aid in the development and evaluation of computer-aided diagnosis (CAD) systems for breast cancer detection.

The images in the Mini-MIAS dataset were obtained from a variety of sources, including several hospitals in the UK and Europe, and they were digitized using a laser film scanner. The images are in grayscale and have a resolution of 1024x1024 pixels. The dataset includes images with benign and malignant lesions, as well as normal images.

Each image in the Mini-MIAS dataset is associated with a radiological report that describes the findings in the image. The reports include information about the location, size, and shape of any abnormalities detected, as well as other relevant clinical information.

The Mini-MIAS dataset has been used in a variety of research studies, including the development of CAD systems for breast cancer detection, the evaluation of image segmentation algorithms, and the analysis of breast cancer risk factors. It has also been used as a benchmark dataset for evaluating the performance of different algorithms and techniques for mammography image analysis.

This algorithm is necessary for the MINI-MIAS dataset because it enables researchers to focus on the regions of interest within the mammography images. By extracting and cropping the ROIs, researchers can improve the accuracy of their analysis and reduce the time required for processing. Additionally, this algorithm can be used to create a more compact dataset for storage and distribution.

## Setup

Clone the repository:

```python
cd ~/Projects
git clone https://github.com/DreamnovaCesar/Crop_images_Mini_MIAS.git
```

To create a virtual environment with TensorFlow using Anaconda, follow these steps:

Open the Anaconda Prompt by clicking the Start button and typing "Anaconda Prompt".
Type the following command to create a new virtual environment called "tfenv":

```python
conda create --name tfenv
```

Activate the virtual environment by typing:

```python
conda activate tfenv
```

Finally, install requirements.txt.

```python
conda install requirements.txt
```

You'll need to use the main.py to run the script

```python
python main.py
```
## Co-authors

- Dr. Hermilo Sanchez Cruz

### Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)&nbsp;

### Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

### 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.linkedin.com/in/cesar-eduardo-mu%C3%B1oz-chavez-a00674186/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/CesarEd43166481"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://www.facebook.com/cesareduardo.munozchavez/"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/></a>
<a href="mailto:cesareduardomucha@hotmail.com"><img src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white"/></a>
<a href="mailto:cesareduardomucha@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>
