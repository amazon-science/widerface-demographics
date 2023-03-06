## Amazon Alexa WiderFace Demographics

Fairness has become an important agenda in computer vision and
artificial intelligence. Recent studies have shown that many com-
puter vision models and datasets exhibit demographic biases and
proposed mitigation strategies. These works attempt to address
accuracy disparity, spurious correlations, or unbalanced representa-
tions in datasets in tasks such as face recognition, verification and
expression and attribute classification. These tasks, however, all
require face detection as the first preprocessing step, and surpris-
ingly, there has been little effort in identifying or mitigating biases
in face detection. Biased face detectors themselves pose a threat
against fair and ethical AI systems, and their biases may be further
passed on to subsequent downstream tasks such as face recognition
in a computer vision pipeline. We collect perceived demographic attributes
on a popular face detection benchmark dataset, WIDER FACE. In this repository, we release the demographic annotations for a subset of Widerface data which can be used by works to retrospect on their model fairness, and to mitigate biases in face detection.

More information about our work can be found in 
https://dl.acm.org/doi/abs/10.1145/3514094.3534153

## Dataset statistics
We annotate a subset of WiderFace data using mechanical turks and get demographic attributes such as perceived age, perceived gender and perceived skintone

From the training split we annotated around 9k faces, and trained a demographic classifier using those images and generated psuedolabels for the remaining faces, totalling to aroung 150k faces, from 12k images

For Validation,
We annotated 12k faces from 3200 images using mechanical turks.

Since we do not have test bounding boxes, we only annotate training anf validation data


#### The annotation file

The annotation file contains Image Filename | perceived_gender | perceived_age | perceived_skin | face | x_min | y_min | width | height | blur | illumination | occlusion |pose |


Please download the images from Widerface website - http://shuoyang1213.me/WIDERFACE/

## Citation

@Inproceedings{Yang2022,
 author = {Yu Yang and Aayush Gupta and Jianwei Feng and Prateek Singhal and Vivek Yadav and Yue Wu and Pradeep Natarajan and Varsha Hedau and Jungseock Joo},
 title = {Enhancing fairness in face detection in computer vision systems by demographic bias mitigation},
 year = {2022},
 url = {https://www.amazon.science/publications/enhancing-fairness-in-face-detection-in-computer-vision-systems-by-demographic-bias-mitigation},
 booktitle = {AIES 2022},
}


## License Summary

The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License. See the LICENSE file.

The files within this documentation are made available under the MIT-0 license. 
