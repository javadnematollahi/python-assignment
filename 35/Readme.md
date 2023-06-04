
# Some operation on color image !
In these projects we will do interenting job.

we want to transparernt some part of an image then we detect color then we pose landmarks on body and the we encrypt a picture and then decrypt the same picture.

lets do it :)


## How to install
Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python file_name.py
example python question2.py

## Results

in the first problem I transparent some part of the microsoft logo picture, so that just the logo and the text in image remaine.

output:

![microsoft_transparent](https://github.com/javad7189/python-assignment/assets/86910174/47ea212b-e827-4cbb-b98c-9da08936c8a8)



In the second problem I draw a color detection that can detect below colors;
white
black
blue
yellow
green
orange
red
purpel

output:




https://github.com/javad7189/python-assignment/assets/86910174/fe05351f-22e7-40fa-9cb1-884ad1d0491d



In the third question I define the landmarks of body in two mode.

1.static mode
2.dynamic mode

To do this you must install mediapipe library on your system, but be careful because 
this library just match with python 3.8,3.9 and 3.10. other version of python can't run this library.

in static mode(question3_image) I read an image of mine, then I define landmarks.

In the dynamic mode(question3_video) I use my mobie camera for record and I can define my body landmarks.

output:

![my_pose_landmard](https://github.com/javad7189/python-assignment/assets/86910174/c36c1263-2d74-4d17-8c9d-9f6366438886)



In fourth question I am getting familiar with pillow library. its a useful library and has some capability that opencv hasn't their.
In this question I just use pillow for imageprocessing.
at first I read an image of a robot then i write a persian text on it. after that I calculate its histogram, next I equalize
this picture and then I cnvert it to a gray picture and finally I equalize the gray picture. In each step I calculate its 
histogram and I save them in an image below each other.

outputs:

![persian_txt](https://github.com/javad7189/python-assignment/assets/86910174/88ad19a4-1db4-4cf7-9508-cbf548235395)


![grayscale_image](https://github.com/javad7189/python-assignment/assets/86910174/eeefebf8-bd82-4470-bea9-af28ff208d96)


![hists](https://github.com/javad7189/python-assignment/assets/86910174/c2891708-c767-4bdd-bc65-f94ad3282456)



In the fifth question I draw  a encrypt-decrypt exe file with pyside6 library so that I upload a predefined picture and
first encrypt it and then decrypt it.

outputs:


![encrypte_image](https://github.com/javad7189/python-assignment/assets/86910174/1981e658-21b1-4d1a-b73e-d861a60eb9d7


![decrypte_image](https://github.com/javad7189/python-assignment/assets/86910174/fed6971c-9d62-43f2-9208-3ac88efb6c87)















