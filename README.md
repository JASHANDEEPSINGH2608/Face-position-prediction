# Image Prediction with Landing AI

This project uses the Landing AI platform to make predictions on a set of images. The predictions include the score, label name, and label index for each image, and the results are saved into a CSV file. The project is implemented in Python and leverages the `landingai.predict` library.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Input Directory](#input-directory)
- [Example](#Example)
- [Live link](#Livelink)


## Introduction
This project processes a batch of images and predicts the presence of certain objects or features using a pre-trained model from Landing AI. The predictions are made using the `landingai.predict` library, and the results are saved in a CSV file for easy analysis.

## Features
- **Image Processing:** Processes images from a specified directory, supporting formats such as `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif`.
- **Prediction:** Utilizes a Landing AI model to predict the content of each image, including the score, label name, and label index.
- **CSV Output:** Saves the prediction results into a CSV file, including the image name, prediction score, label name, and label index.
- **Progress Tracking:** Displays progress in the console as images are processed.

## Installation
To run this project, you'll need to have Python installed, along with the necessary libraries:
   
## Usage
- Give folder name in image_folder
- Result filename in output_csv
```bash
image_folder = <folderName>
output_csv = <predictionresultsCSV>
```

## Example
```python
image_folder = "Google_images"
output_csv = "predictionsoffaces.csv"
```

## Live link
[https://app.landing.ai/predict/eb43103c-7b67-40b6-bdcd-dbacd6b434de](https://app.landing.ai/predict/90b45bc5-6029-4a94-8acc-dc2735081e39)


