import os
import easyocr
path = "chinese_english_farsi"
texts = dict()
text_list = []


files_language = ['en', 'ch', 'fa']
lanuages = ['en', 'ch_sim', 'fa']
for i,file_name in enumerate(os.listdir(path)):
    file_path = os.path.join(path, file_name)
    for j in range(3):
      if os.path.isfile(file_path) and file_name.startswith(files_language[j]):
        reader = easyocr.Reader([lanuages[j]])
        result = reader.readtext(file_path)
        for item in result:
          print(item)
          if item[2]:
            text_list.append(item[1])
        texts[file_name] = text_list.copy()
        text_list.clear()

f = open('chinese_english_farsi/image_text.txt', 'w' , encoding="utf-8")   

for key in texts:
  f.write(f"{key}:\n")    
  for i in texts[key]:
    print(i)
    f.write(f"{i}\n")  
  f.write("\n")  

