# mia-covid19

All the images size are reduced to 224x224 using [this script](https://github.com/talhaanwarch/mia-covid19/blob/main/resize_script.py)  
# Training 
For training, we have used [final_train](https://github.com/talhaanwarch/mia-covid19/blob/main/final_train.ipynb) script.
Model used are 
1. resnet152_v1
2. densenet201 
3. resnest14
4. resnext50_32x4d
5. se_resnext50_32x4d
6. mobilenetv3_large
7. VGG19_bn		

# Testing
For inference use [this notebook](https://github.com/talhaanwarch/mia-covid19/blob/main/final-inference.ipynb)  

<table><thead><tr><th>Model name</th><th>Model Size</th><th>Test Inference Time</th><th>2D F1-Score</th><th>3D F1-score</th><th>download key (gdown)</th></tr></thead><tbody><tr><td>ResNet152</td><td>472 MB</td><td>3h 15min</td><td>80%</td><td>85%</td><td>1kEbLGawKfccacR1EcbwVJGFct8I1v0gl</td></tr><tr><td>DenseNet201</td><td>166 MB</td><td>2 hrs 48 min</td><td>81%</td><td>84%</td><td>1kcPzR71WjafO7GGWPHdb5ahfHamLtBaT</td></tr><tr><td>ResNest14</td><td>93 MB</td><td>2hrs 22min</td><td>85%</td><td>88%</td><td>1Qj2t54rHr2L563DPUgOB1ysfoudSC1b9</td></tr><tr><td>ResNext50</td><td>203 MB</td><td>2hrs 7 min</td><td>83%</td><td>88%</td><td>1-07LVf5nPVACqnxMzL39LjFZ83Xodint</td></tr><tr><td>Se_ResNext50</td><td>222 MB</td><td>2hrs 49</td><td>84%</td><td>87%</td><td>1-4OGmbeOoTNZKM6itK-06StDu9Wsz_AB</td></tr><tr><td>MobileNetV3</td><td>63 MB</td><td>2hrs 37min</td><td>80%</td><td>86%</td><td>18GCi3fVuwfFRHs4EOhXvb-rqZpByahf-</td></tr><tr><td>VGG19_bn</td><td>1 GB</td><td></td><td>84%</td><td>87%</td><td>1yIJdYC13nW9Wou3aPlNSSE9R-_8aCZfz</td></tr></tbody></table>

# Submission
1. Maximum 
2. 10% threshold
3. 20% threshold
4. 30% threshold
5. All above
# Packages
[MXNet](https://pypi.org/project/mxnet/1.8.0.post0/)  
[autogluon](https://pypi.org/project/autogluon/0.2.1b20210621/)  
[gluoncv](https://pypi.org/project/gluoncv/0.11.0b20210612/)  
