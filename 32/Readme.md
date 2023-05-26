
# Median filter
In these projects we use median filter to remove salt-and-pepper noise on some images.
there is a function in python for this operation call medianBlur.

# equalization
Its an operation in image processing to enhance contrast of an image.
if the histogram of your image focus in black area or white area, then equalizeHist function can solve your problem.
But if your histograms picture is not focus in black or white area you van use CLAHE to solve your problem and 
don't lose details too.



## How to install
Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python file_name.py
example python question2.py

## Results

in the first problem(first part) we applied several different kernels to the same image with filter2D function.

output:

![b_edgedetection](https://github.com/javad7189/python-assignment/assets/86910174/58db2219-d268-482b-b912-f00c71e91a59)


In part 2 we decryption of an image using a blur kernel which size is 3*3. But the values is 1 and 5. we do this by another kernel which size is 5 * 5.

output:

![dycreption](https://github.com/javad7189/python-assignment/assets/86910174/42a2be78-694b-4986-ab2b-ad9a89bfe251)



In the second problem we use median filter to remove noise from some pictures.

output:

![body](https://github.com/javad7189/python-assignment/assets/86910174/8d039448-ca53-4fa6-befb-6af3282d04e1)
![circle](https://github.com/javad7189/python-assignment/assets/86910174/a9ee0935-2595-4ede-9d79-b89996becf56)
![elec](https://github.com/javad7189/python-assignment/assets/86910174/2dbc405e-4c71-4bbf-a287-3e9c3d829566)
![party](https://github.com/javad7189/python-assignment/assets/86910174/a81b1e61-c963-42c4-a667-e9f56cd8d326)
![things](https://github.com/javad7189/python-assignment/assets/86910174/0d16e450-9f85-4ab6-874c-508c0a443827)
![woman](https://github.com/javad7189/python-assignment/assets/86910174/e25213ef-1ef8-479a-814d-80463d72c53d)



In the third question we eualize histogram of three pictures to enhance their brightness.
we use same method for first two pictures. we use different method for third picture.

output 1 and 2:

![city_H_c](https://github.com/javad7189/python-assignment/assets/86910174/114d8ceb-8ca0-4cb4-b7ed-3c83f91642f1)

![rural_H_c](https://github.com/javad7189/python-assignment/assets/86910174/bdc857db-ab29-4e3c-bd07-239c913f83ca)

output 3:

![room_H_c](https://github.com/javad7189/python-assignment/assets/86910174/1f5c2a49-d211-494f-aeb8-3d2b24718938)









