from PIL import ImageFont, ImageDraw, Image ,ImageOps
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

image_pil=Image.open("input/AI.jpg")
image_pil_copy=image_pil.copy()
text = "این دنیای جدیده!"
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction

draw = ImageDraw.Draw(image_pil)  
font = ImageFont.truetype("input/B Morvarid.ttf", 82)  
draw.text((100,60), bidi_text, font=font, fill=(128, 20, 128))  

image_pil.show()
image_pil.save("output/persian_txt.jpg")

figure, axis = plt.subplots(4,1,figsize=(7, 23))

# histogram of color image
r, g, b = image_pil_copy.split()

colors=['red','green','blue']
images=[r,g,b]
for i,color in enumerate(colors):
    hist = images[i].histogram()
    # plt.plot(hist,color=color)
    axis[0].plot(hist)
    axis[0].set_title("hist")


# equalize histogram of color image and save it
im2 = ImageOps.equalize(image_pil_copy, mask = None)

r, g, b = im2.split()

colors=['red','green','blue']
images=[r,g,b]
for i,color in enumerate(colors):
    hist_equalize = images[i].histogram()
    axis[1].plot(hist_equalize)
    axis[1].set_title("hist_equalize")


# convert to gray
image_gray = image_pil_copy.convert("L")

# Save the grayscale image
image_gray.save("output/grayscale_image.jpg")

hist_gray = image_gray.histogram()
axis[2].plot(hist_gray)
axis[2].set_title("hist_gray")


im3 = ImageOps.equalize(image_gray, mask = None)
hist_gray_qualize = im3.histogram()
axis[3].plot(hist_gray_qualize)
axis[3].set_title("hist_gray_qualize")

plt.savefig('output/hists.png')
plt.show()