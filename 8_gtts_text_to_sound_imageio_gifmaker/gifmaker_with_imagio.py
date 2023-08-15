import os
import imageio

file_list = sorted(os.listdir("OutputPics"))

IMAGES=[]
for filename in file_list:

    file_path = "OutputPics/"+filename
    image=imageio.imread(file_path)
    IMAGES.append(image)


imageio.mimsave("output/my_output.gif",IMAGES)