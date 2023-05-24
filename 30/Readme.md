
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

In the second problem eyes and lips are extracted and each eye and lips are rotated 180 degree in their places.
for example right eye is extracted and rotated 180 degree put is put it back on previous location. finally we rotate the main image 180 degree.

output:


In the third question we use mtcnn library to detect coordinates of eyes and lips. then we use these data to find out the angle of head and then we turn picture by the angle that we calculated from the previous step.

output:



4.In the fourth problem eyes and lips of a person in a picture are detected and we make them bigger than usual. 

output:










