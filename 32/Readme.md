
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



In part 2 we decryption of an image using a blur kernel which size is 3*3. But the values is 1 and 5. we do this by another kernel which size is 5 * 5.

output:




In the second problem we use median filter to remove noise from some pictures.

output:




In the third question we eualize histogram of three pictures to enhance their brightness.
we use same method for first two pictures. we use different method for third picture.

output 1 and 2:




output 3:









