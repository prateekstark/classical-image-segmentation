# classical-image-segmentation
In this repository, we use classical computer vision techniques to segment real ultrasound
images and extract Gall Bladder from the images.

## Usage
For segmentating images and obtaining Gall Bladder:
```bash
python gen_det.py --img_path <img_folder> --det_path <name_of_output_folder>
# python gen_det.py --img_path img/ --det_path det/
```
Running Evaluation Script:
```bash
python eval.py --img_path <img_folder> --det_path <path_to_output_folder> --gt_path <path_to_ground_truth_folder>
# python eval.py --img_path img/ --det_path det/ --gt_path annotation
```

## Techniques Used:
For the image segmentation, we are using a series of thresholding. Then we find closed contours in the images. In the images, we notice that the largest contour is formed by the curves on the boundary and the second-largest closed contour is the Gallbladder, that we want. In this, I tried several variation techniques to make this work well.

### Code Flow:
* RawImage
* Sharpening
* GaussianBlur
* Threshold
* Take Bitwise And with Raw Image
* Threshold
* Close the open contours using MORPH_CLOSE
* Find Closed contours and pick the second largest one

## Techniques Tried:
I tried several other approaches, before coming to this final code structure. Other
techniques which I tried were:
* Watershed Algorithm
* Canny edge detector
* Laplacian of Gaussian (LoG) edge detector
* Adaptive Thresholding

Of course, none of the above techniques was able to surpass the technique finally used above.


## Results:
On the validation set, the average IOU is: ​ *0.7623344553319458*

**[Details]**

Number of images: 10

Number of detections: 10

Number of ground truths: 10
- IoU for image img/0000.jpg = 0.7233911954626925
- IoU for image img/0001.jpg = 0.8209175952675747
- IoU for image img/0002.jpg = 0.8514002443379382
- IoU for image img/0003.jpg = 0.8499851889467225
- IoU for image img/0004.jpg = 0.81443763518385
- IoU for image img/0005.jpg = 0.783661161368855
- IoU for image img/0006.jpg = 0.7386243991760129
- IoU for image img/0007.jpg = 0.5810126582278481
- IoU for image img/0008.jpg = 0.880874951606659
- IoU for image img/0009.jpg = 0.579039523741305

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.