import os,base64,requests
import telebot
from telebot import types
import tensorflow as tf
import cv2
import numpy as np
import random
import jdatetime
import datetime
import time
import gtts
import string
import qrcode 
from dotenv import load_dotenv
from os import environ as env

load_dotenv()
# TOKEN = os.environ['TOKEN']

TOKEN = os.getenv('TOKEN_BOT')

token = TOKEN
new_game = 0
game = 0
age = 0
voice = 0
max_number = 0
argmax_number = 0
myqrcode = 0
image = 0

labels = ['bluebell', 'buttercup', 'coltsfoot', 'cowslip', 'crocus', 'daffodil', 'daisy', 'dandelion', 'fritillary', 'iris', 'lilyvalley', 'pansy', 'snowdrop', 'sunflower', 'tigerlily', 'tulip', 'windflower']
model = tf.keras.models.load_model('weights/flower_aug1.h5')

my_keyboard = types.ReplyKeyboardMarkup(row_width=1)
key1=types.KeyboardButton("New Game")
key2=types.KeyboardButton("Exit")
my_keyboard.add(key1,key2)

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"{message.from_user.first_name} welcome to NEW_pylearn_bot")
	bot.send_message(message.chat.id,"دستور /help رو بزن تا امکانات ربات رو ببینی.") 

@bot.message_handler(commands=['voice'])
def send_voice(message):
	global voice
	voice=1
	bot.send_message(message.chat.id,"یه جمله ی انگلیسی بفرست تا واست تبدیلش کنم به صدا ") 
	bot.send_message(message.chat.id,"فقط یادت باشه توی جمله ات فقط از حروف انگلیسی و (,) و فاصله می تونی استفاده کنی و هیچ کاراکتر اضافه نباید وارد نکنی.") 


@bot.message_handler(commands=['age'])
def send_age(message):
	global age
	age=1
	bot.send_message(message.chat.id,"تاریخ تولدت رو به صورت هجری شمسی وارد کن تا سنت رو بگم") 
	bot.send_message(message.chat.id,"قالبش هم به این صورت باشه:  yyyy/mm/dd") 

@bot.message_handler(commands=['max'])
def send_max(message):
	global max_number
	max_number=1
	bot.send_message(message.chat.id,"یک آرایه از اعداد وارد کن تا بزرگترینش رو بهت بگم. اعدادی که وارد میکنی رو با (,) از هم جدا کن.") 

@bot.message_handler(commands=['argmax'])
def send_argmax(message):
	global argmax_number
	argmax_number=1
	bot.send_message(message.chat.id,"یک آرایه از اعداد وارد کن تا اندیس بزرگترینش رو بهت بگم. اعدادی که وارد میکنی رو با (,) از هم جدا کن.") 

@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
	global myqrcode
	myqrcode=1
	bot.send_message(message.chat.id,"یک متن وارد کن تا واست تبدیلش کنم به QrCode") 
	
@bot.message_handler(commands=['image'])
def send_image(message):
	global image
	image=1
	bot.send_message(message.chat.id,"عکس یه گل بفرست(به غیر از خودت) تا اسمش رو حدس بزنم") 


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id,"به help بات خوش اومدی:\nتوی این بات از کامندهای زیر می تونی استفاده کنی:\n/start\n/game\n/voice\n/age\n/max\n/argmax\n/qrcode\n/image") 
	bot.send_message(message.chat.id,"/start\nاگر این کامند رو وارد کنی واست پیام خوش آمدگویی میفرستم😊\n/game\nاگر این کامند رو وارد کنی بازی حدس اعداد رو میتونی انجام بدی.اگر New game رو هم بزنی یه دور جدید شروع میشه و اگر Exit رو بزنی از بازی خارج میشه.\n/voice\nاگر این کامند رو وارد کنی میتونی یک متن انگلیسی بفرستی و صدای اون متن رو تحویل بگیری.\n/age\nاگر این کامند رو وارد کنی ، بعدش تاریخ تولدت رو هم وارد کنی، سنت رو بهت میگم😊\n/max\nاگر این کامند رو وارد کنی، بعدش هم یه تعداد عدد وارد کنی، بزرگترین عدد رو بهت میگم.\n/argmax\nاگر این کامند رو وارد کنی و بعدش یه تعداد عدد وارد کنی، اندیس بزرگترین عدد رو بهت میگم.\n/qrcode\n اگر این کامند رو وارد کنی، بعدش هر متنی دلت میخواد بفرست تا واست تبدیلش کنم به QrCode\n/image\n اگر این کامند رو وارد کنی، بعدش میتونی یه عکس گل بفرستی تا بهت اسمش رو بگم ") 

@bot.message_handler(commands=['game'])
def send_game(message):
	global num,game,new_game
	num=random.randint(1,100)
	new_game=1
	game=1
	bot.send_message(message.chat.id,"تو این بازی باید یک عدد رو حدس بزنی. شروع کن", reply_markup=my_keyboard) 


# @bot.message_handler(func=lambda m: True, content_types=['photo'])
# def get_broadcast_picture(message):
# 	file_path = bot.get_file(message.photo[0].file_id).file_path
# 	file = bot.download_file(file_path)
# 	# image = np.frombuffer(file, dtype=np.uint8)
# 	# print(image.shape)
# 	with open("gol.jpg", "wb") as code:
# 		code.write(file)


@bot.message_handler(content_types = ["photo"])
def photo(message):
	global image,model,labels
	if image == 1 : 
		file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open("gol.jpg", "wb") as new_file:
			new_file.write(downloaded_file)

		user_image = cv2.imread('gol.jpg')
		user_image = cv2.resize(user_image, (224,224))
		# print(np.max(user_image))
		# user_image = np.array(user_image)/255
		# print(np.max(user_image))
		user_image = np.expand_dims(user_image, axis=0) 
		# print(user_image.shape)
		result = model.predict(user_image)
		out = np.argmax(result)
		# print(result)
		# print(out)
		bot.send_message(message.chat.id , f' احساس میکنم اسم گلت {labels[out]} باشه.')
		image = 0 

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global num,game,new_game,age,voice,max_number,argmax_number,myqrcode,image

	if image == 1 : 
		bot.send_message(message.chat.id, " یه عکس گل گفتم بفرست بیزحمت ")	
		image=0            

	if game==1:
		try:
			if message.text == "New Game": 
				num=random.randint(1,100)
				bot.send_message(message.chat.id, " بازی جدید شروع شد.  ")
				new_game=1
			elif message.text == "Exit": 
				my_keyboard = types.ReplyKeyboardRemove(selective=False)
				bot.send_message(message.chat.id, " مرسی از اینکه این بازی رو انجام دادی. ", reply_markup=my_keyboard)
				# bot.send_message(message.chat.id, " مرسی از اینکه این بازی رو انجام دادی. ")	
				game=0
				new_game=0
			if new_game==1:
				if int(message.text) < num: 
					bot.send_message(message.chat.id, " برو بالا ") 
				elif int(message.text) > num: 
					bot.send_message(message.chat.id, " برو پایین ") 
				elif int(message.text) == num: 
					bot.send_message(message.chat.id, " برنده شدی")
					new_game=0
		except:
			bot.send_message(message.chat.id, " یک عدد وارد کن")
			message.text = ""


	if age==1:
		try:
			birthdate=message.text.split('/')
			year=int(birthdate[0])
			month=int(birthdate[1])
			day=int(birthdate[2])
			# convert birth date to gregorian
			gregorian_date = jdatetime.date(year,month,day).togregorian()
			birthdate=str(gregorian_date).split("-")
			date_time = datetime.datetime(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]), 0, 0)
			
			
			# convert gregorian birth date to timestamp
			birth_time=time.mktime(date_time.timetuple())

			# get current date
			datetime_obj = datetime.datetime.now()
			date_time = datetime.datetime(datetime_obj.year, datetime_obj.month, datetime_obj.day, datetime_obj.hour, datetime_obj.minute)

			#convert current date to timestamp
			time_now=time.mktime(date_time.timetuple())

			#calculate timestamp age 
			age=time_now-birth_time

			#convert timestamp age year and mont and day
			date_time = datetime.datetime.fromtimestamp(age)
			bot.send_message(message.chat.id, f"سن شما برابر است با: ")	
			bot.send_message(message.chat.id, f" روز{date_time.day} و ماه {date_time.month} و سال{(date_time.year-1970)}")	
		except:
			bot.send_message(message.chat.id, f"قرار بود تاریخ تولدت رو به این صورت وارد کنی:🤦‍♂️  yyyy/mm/dd")	
			bot.send_message(message.chat.id, f"اگر خواستی یه بار دیگه از اول انجام بده تا سنت رو بگم 😊")	
		age=0

	if voice==1:
		my_text = message.text
		char_set = string.ascii_letters
		for x in my_text:
			if  x in char_set or x==" " or x==",":
				check=True
			else:
				check=False
		if check==True:
			x=gtts.gTTS(my_text,lang="en",slow=False)
			x.save("output/voice.mp3")
			bot.send_audio(chat_id=message.chat.id, audio=open('output/voice.mp3', 'rb'))
		elif check==False:
			bot.send_message(message.chat.id,"قرار بود جمله ای که وارد کنی فقط و فقط حروف انگلیسی و فاصله و (,) داشته باشه.") 
			bot.send_message(message.chat.id,"😊اگر خواستی دوباره از اول انجام بده ") 
		voice=0
		

	if max_number==1:
		try:
			number_list=[]
			my_text = message.text
			numbers = my_text.split(",")
			for i in numbers:
				number_list.append(int(i))
			bot.send_message(message.chat.id,f" بزرگترین عدد {max(number_list)} است. ") 
		except:
			bot.send_message(message.chat.id,"یه مشکلی توی اعدادی که وارد کردی وجود داره.") 
		max_number=0

	if argmax_number==1:
		try:
			number_list=[]
			my_text = message.text
			numbers = my_text.split(",")
			for i in numbers:
				number_list.append(int(i))
			bot.send_message(message.chat.id,f" اندیس بزرگترین عدد {number_list.index(max(number_list))} است. ") 
		except:
			bot.send_message(message.chat.id,"یه مشکلی توی اعدادی که وارد کردی وجود داره.") 
		argmax_number=0
		

	if myqrcode==1:

		my_text = message.text
		qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
		qr.add_data(my_text)
		qr.make(fit = True)
		img = qr.make_image(fill_color = 'red', back_color = 'white')
		img.save("output/user_qrcode.png")
		photo = open("output/user_qrcode.png","rb")
		bot.send_photo(message.chat.id,photo)

		myqrcode=0



bot.infinity_polling()