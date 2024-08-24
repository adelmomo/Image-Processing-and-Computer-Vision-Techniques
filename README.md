# Image Processing and Computer Vision Techniques
This repository is intended to demonstrate and implement the fundamental topics in Image Processing and Computer Vision

## Features

- **ImageTransformation**: Tools and algorithms for altering and enhancing images through various transformation techniques.
<p align="center">
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <div><strong>Input Image</strong></div>
    <img src="./ImageTransformation/sample.jpg" alt="Input Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center;">
    <div><strong>Image Output After Histogram Equalization</strong></div>
    <img src="./ImageTransformation/histogram_equalization_output.jpg" alt="Output Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center;">
    <div><strong>Image Output After Gaussian Blurring</strong></div>
    <img src="./ImageTransformation/gaussian_blur_output.jpg" alt="Output Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <div><strong>Input Image with Salt & Pepper Noise</strong></div>
    <img src="./ImageTransformation/sample_with_salt_and_pepper.jpg" alt="Input Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <div><strong>Image Output After Median Filtering</strong></div>
    <img src="./ImageTransformation/median_output.jpg" alt="Input Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
</p>

- **EdgeDetection**: Implementations of edge detection algorithms to identify and outline features within images.
<p align="center">
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <div><strong>Input Image</strong></div>
    <img src="./EdgeDetection/sample.jpg" alt="Input Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center;">
    <div><strong>Image Edges</strong></div>
    <img src="./EdgeDetection/output.jpg" alt="Output Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
</p>

- **ImageSegmentation**: Tools and algorithms for segmenting an image into `k` clusters/groups.
<p align="center">
  <div style="display: inline-block; text-align: center; margin-right: 20px;">
    <div><strong>Input Image</strong></div>
    <img src="./ImageSegmentation/giraffe.png" alt="Input Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
  <div style="display: inline-block; text-align: center;">
    <div><strong>Segmented Image</strong></div>
    <img src="./ImageSegmentation/output.jpg" alt="Output Image" width="300" style="border: 1px solid #ddd; padding: 5px;">
  </div>
</p>

## Edge Detection Application Demo

This is an application that strongly relies on Edge Detection to detect whether the Camera is covered or not. Here is a demo video showcasing the output after running the application:

https://github.com/user-attachments/assets/79bcd89e-ce39-4dee-9a63-e590748f968d

## Sub-Repositories

### Image Transformation

This sub-repository focuses on various image transformation techniques, including resizing, rotation, and color adjustments. It provides tools to modify images efficiently and effectively, offering a range of utilities to meet diverse transformation needs.

### Edge Detection

Dedicated to edge detection methods, this sub-repository includes algorithms for identifying boundaries and contours within images. It supports a variety of edge detection techniques, such as Sobel, Canny, and Laplacian, to assist in feature extraction and object recognition tasks.

### Edge Detection

This sub-repository is centered around image segmentation techniques, with a focus on dividing an image into meaningful regions or clusters. Utilizing methods like K-Means clustering, it enables the separation of different objects or areas within an image based on color, texture, and intensity. The tools provided are essential for tasks such as object recognition, scene understanding, and image analysis, making segmentation more accessible and efficient.

## Usage

To get started with the tools and techniques provided in this repository, follow the instructions in each sub-repository's README files. Comprehensive guides and examples are included to help you integrate and utilize these tools in your own projects.
