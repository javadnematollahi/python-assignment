
# find contour
In these projects we are going to solve some problems to get more experience
about working with contours in opencv. we use hierarchy to identify parent contour and child contour. 


## How to install
Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python file_name.py
example python question2.py

## Results

in the first problem we try to reconstruct an image from its histogram but its impossible.
if you want to know why, see question1.py file. I explain the reasons there.


In the second problem we load 4 picture of some dices and try to find out the number of each dice.
we use findcontour function and hierarchy parameter of this function to solve this problem.

output:

![5_dice](https://github.com/javad7189/python-assignment/assets/86910174/61bcf3cc-4512-448c-bcae-22c70398c4ae)

![3_dice](https://github.com/javad7189/python-assignment/assets/86910174/657fbe52-701d-401a-b59c-76d83a6e5e0c)

![2_dice](https://github.com/javad7189/python-assignment/assets/86910174/993ad9af-b30e-49bf-8571-269f59582af3)

![1_dice](https://github.com/javad7189/python-assignment/assets/86910174/eff7fda9-ebcc-4331-bedb-f0a323af3bc4)


In the third question I wrote cv2.boundingRect() function from scratch. i compare the result of opencv function and my function.
the results of both are same.

output:

![boundrect](https://github.com/javad7189/python-assignment/assets/86910174/ec2b8393-2018-4f03-baac-d0b791b8dcaa)


In fourth question I wrote cv2.contourArea() function from scratch. i compare the result of opencv function and my function. I use to different idea to solve this problem and the resulte of both idea are almost close to opencv 
result. the code of this part is written in question4.py and question4_1.py files.
The below picture you can see the results.

output:

![contour_area4](https://github.com/javad7189/python-assignment/assets/86910174/ddd7fa29-1078-4334-b4de-5b89b6f0ee7b)
![contour_area4_1](https://github.com/javad7189/python-assignment/assets/86910174/e34d43ff-a397-445e-937b-6fc0d10fe5c6)


In the fifth question i wrote cv2.findContours() function from scratch. for this question i use povlidis algorithm
to find the contours in the picture.
In this question i really close to opencv answers. 

to get more information about this algorithm follow below link:
https://www.imageprocessingplace.com/downloads_V3/root_downloads/tutorials/contour_tracing_Abeer_George_Ghuneim/theo.html

Two below pictures are shown the results.

output:

![Opencv_contours](https://github.com/javad7189/python-assignment/assets/86910174/68721988-d85c-4c1b-983c-88fb9e60231d)
![Our_contours](https://github.com/javad7189/python-assignment/assets/86910174/9cfa82ab-5cd7-4854-932f-e49e4e02783c)


In the sixth question i made a funny webcam video. In this video i try to put part of my face include lips and noise
instead of part of faces that belong to men or womens are painted.

lets see the result. i try to do my best :)

output:


















