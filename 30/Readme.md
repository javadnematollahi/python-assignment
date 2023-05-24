
# Detect Eye and Lips
In these projects we use github.com/1996scarlet/openVtuber repository to do some changes on different image.
our goal is to detect face and eyes and lips and earn their cordinates in image.


## How to install
Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python file_name.py
example python question2.py

## Results

in the first problem eyes and lips of a person in a picture are detected at the first level. then we extract them and put then on some fruit.   

output:

![apple](https://github.com/javad7189/python-assignment/assets/86910174/a92dd9a5-9f7f-4096-9f87-c0ebc9534d73)
![carrot](https://github.com/javad7189/python-assignment/assets/86910174/01d213c5-a6b7-4890-8999-d9733f3f90aa)
![orange](https://github.com/javad7189/python-assignment/assets/86910174/2e091978-dba0-4cb9-9b0c-8f65f61de6a0)


In the second problem eyes and lips are extracted and each eye and lips are rotated 180 degree in their places.
for example right eye is extracted and rotated 180 degree put is put it back on previous location. finally we rotate the main image 180 degree.

output:

![odd_face](https://github.com/javad7189/python-assignment/assets/86910174/a8f60762-7fa8-4ce2-967e-9bf0960eccf4)


In the third question we use mtcnn library to detect coordinates of eyes and lips. then we use these data to find out the angle of head and then we turn picture by the angle that we calculated from the previous step.

output:

![rotate_face](https://github.com/javad7189/python-assignment/assets/86910174/1258e613-220f-40ec-b14f-cc1273d208d9)


4.In the fourth problem eyes and lips of a person in a picture are detected and we make them bigger than usual. 

output:

![Big_eye_lips](https://github.com/javad7189/python-assignment/assets/86910174/8dd59789-fa41-44da-9a67-ddbff9cb351c)









