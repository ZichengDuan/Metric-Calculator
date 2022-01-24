# Metric calculator for oriented bounding boxes and object occupancy accuracy.

## Introduction
This toolkit calculates several metrics related to object 3D pose estimation and its corresponding occupancy accuracy.

For oriented bounding boxes:

- `AP_3D (Iou = 0.25, 0.5, etc.)`, average precision for 3D detection.
- `AOS (Iou = 0.25, 0.5, etc.)`, average orientation similarity.
- `OS`, orientation ocore.

For object occupancy:
- `MODA`, multi-object detection accuracy.
- `MODP`, multi-object detection precision.
- `Precision`.
- `Recall`.

## Requirements
- Install module shapely using `pip install shapely`.
- Install MATLAB and MATLAB engine, [link](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html).


## Data Preparation and Usage
Both of your ground truth data and results should be capsuled in text file and formatted into a `n,14` matrix as below, where `n` represents the number of samples you have in you data:

`frame num | occ_x | occ_y | w | h | r_x1 | r_y1 | r_x2 | r_y2 | r_x3 | r_y3 | r_x4 | r_y4 | degree`

where 
- `frame num` refers to the frame identity number,
- `occ_x` & `occ_y` refers to object global coordinate on occupacy map,
- `w` & `h` refers to object origin width and height,
- `r_x`/`r_y` refer to the rotated coordinates of the bounding boxes.
- `degree` refers to the orientation degree of the current bounding box.

Please refer to example [gt.txt](https://github.com/ZichengDuan/Metric-Calculator/blob/main/code/gt.txt) and [results.txt]((https://github.com/ZichengDuan/Metric-Calculator/blob/main/code/results.txt)) for sample data, [evaluation.py](https://github.com/ZichengDuan/Metric-Calculator/blob/main/code/evaluation.py) to specify your file path.

Run the script using `cd code && evaluate.py` to evaluate the template results, the expected output should be:
![](https://github.com/ZichengDuan/Metric-Calculator/blob/main/misc/output.png)

## Parameter settings
Specify distance threshold (in centimeters) for calculating `MODA` and `MODP` in [CLEAR_MOD_HUN.m](https://github.com/ZichengDuan/Metric-Calculator/blob/main/code/motchallenge-devkit/utils/CLEAR_MOD_HUN.m) line 35.
