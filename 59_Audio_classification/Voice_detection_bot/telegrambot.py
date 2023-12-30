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
import pydub
import numpy as np
from collections import Counter
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
new_voice=0
singer=0
singers = ['chavoshi', 'ebi', 'rezasadeghi', 'shadmehr', 'yegane']
persons = ['abdollah', 'azra', 'davood', 'javad', 'kiana', 'matin', 'mohamad', 'mohamadd', 'mona', 'nima', 'omid', 'parisa', 'parsa', 'saeedi', 'sajedeh', 'shima', 'tara', 'valipour']
labels = ['bluebell', 'buttercup', 'coltsfoot', 'cowslip', 'crocus', 'daffodil', 'daisy', 'dandelion', 'fritillary', 'iris', 'lilyvalley', 'pansy', 'snowdrop', 'sunflower', 'tigerlily', 'tulip', 'windflower']
model = tf.keras.models.load_model('best_model_flower/flower_aug1.h5')
friend_model = tf.keras.models.load_model('best_friend_model')
singer_model = tf.keras.models.load_model('best_singer_model')

my_keyboard = types.ReplyKeyboardMarkup(row_width=1)
key1=types.KeyboardButton("New Game")
key2=types.KeyboardButton("Exit")
my_keyboard.add(key1,key2)

bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"{message.from_user.first_name} welcome to NEW_pylearn_bot")
	bot.send_message(message.chat.id,"دستور /help رو بزن تا امکانات ربات رو ببینی.") 

@bot.message_handler(commands=['text_to_voice'])
def send_game(message):
	global voice
	voice=1
	bot.send_message(message.chat.id,"یه جمله ی انگلیسی بفرست تا واست تبدیلش کنم به صدا ") 
	bot.send_message(message.chat.id,"فقط یادت باشه توی جمله ات فقط از حروف انگلیسی و (,) و فاصله می تونی استفاده کنی و هیچ کاراکتر اضافه نباید وارد نکنی.") 


@bot.message_handler(commands=['age'])
def send_game(message):
	global age
	age=1
	bot.send_message(message.chat.id,"تاریخ تولدت رو به صورت هجری شمسی وارد کن تا سنت رو بگم") 
	bot.send_message(message.chat.id,"قالبش هم به این صورت باشه:  yyyy/mm/dd") 

@bot.message_handler(commands=['max'])
def send_game(message):
	global max_number
	max_number=1
	bot.send_message(message.chat.id,"یک آرایه از اعداد وارد کن تا بزرگترینش رو بهت بگم. اعدادی که وارد میکنی رو با (,) از هم جدا کن.") 

@bot.message_handler(commands=['argmax'])
def send_game(message):
	global argmax_number
	argmax_number=1
	bot.send_message(message.chat.id,"یک آرایه از اعداد وارد کن تا اندیس بزرگترینش رو بهت بگم. اعدادی که وارد میکنی رو با (,) از هم جدا کن.") 

@bot.message_handler(commands=['qrcode'])
def send_game(message):
	global myqrcode
	myqrcode=1
	bot.send_message(message.chat.id,"یک متن وارد کن تا واست تبدیلش کنم به QrCode") 
	
@bot.message_handler(commands=['image'])
def send_game(message):
	global image
	image=1
	bot.send_message(message.chat.id,"عکس یه گل بفرست(به غیر از خودت) تا اسمش رو حدس بزنم") 

@bot.message_handler(commands=['help'])
def send_game(message):
	bot.send_message(message.chat.id,"به help بات خوش اومدی:\nتوی این بات از کامندهای زیر می تونی استفاده کنی:\n/start\n/game\n/audio\n/singer\n/text_to_voice\n/voice\n/age\n/max\n/argmax\n/qrcode\n/image") 
	bot.send_message(message.chat.id,"/start\nاگر این کامند رو وارد کنی واست پیام خوش آمدگویی میفرستم😊\n/singer\nاگر این کامند رو وارد کنی و بعد یک آهنگ بفرستی میتونم بهت اسم خواننده رو بگم.\n/audio\nاگر این کامند رو وارد کنی و بعد صداتو بفرستی میتونم بهت بگم تو کی هستی. \n/game\nاگر این کامند رو وارد کنی بازی حدس اعداد رو میتونی انجام بدی.اگر New game رو هم بزنی یه دور جدید شروع میشه و اگر Exit رو بزنی از بازی خارج میشه.\n/text_to_voice\nاگر این کامند رو وارد کنی میتونی یک متن انگلیسی بفرستی و صدای اون متن رو تحویل بگیری.\n/age\nاگر این کامند رو وارد کنی ، بعدش تاریخ تولدت رو هم وارد کنی، سنت رو بهت میگم😊\n/max\nاگر این کامند رو وارد کنی، بعدش هم یه تعداد عدد وارد کنی، بزرگترین عدد رو بهت میگم.\n/argmax\nاگر این کامند رو وارد کنی و بعدش یه تعداد عدد وارد کنی، اندیس بزرگترین عدد رو بهت میگم.\n/qrcode\n اگر این کامند رو وارد کنی، بعدش هر متنی دلت میخواد بفرست تا واست تبدیلش کنم به QrCode\n/image\n اگر این کامند رو وارد کنی، بعدش میتونی یه عکس گل بفرستی تا بهت اسمش رو بگم ") 

@bot.message_handler(commands=['audio'])
def send_game(message):
	global new_voice
	new_voice=1
	bot.send_message(message.chat.id,"یک صدا از خودت بفرست که حداقل 10 ثانیه باشه، بعد بهت میگم تو کی هستی.") 

@bot.message_handler(commands=['singer'])
def send_game(message):
	global singer
	singer=1
	bot.send_message(message.chat.id,"یک آهنگ از یک خواننده بفرست، تا خوانندش رو بهت بگم.") 

@bot.message_handler(commands=['game'])
def send_game(message):
	global num,game,new_game
	num=random.randint(1,100)
	bot.send_message(message.chat.id,"تو این بازی باید یک عدد رو حدس بزنی. شروع کن", reply_markup=my_keyboard) 

# @bot.message_handler(func=lambda m: True, content_types=['photo'])
# def get_broadcast_picture(message):
# 	file_path = bot.get_file(message.photo[0].file_id).file_path
# 	file = bot.download_file(file_path)
# 	# image = np.frombuffer(file, dtype=np.uint8)
# 	# print(image.shape)
# 	with open("gol.jpg", "wb") as code:
# 		code.write(file)
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
	global new_voice, singer
	if new_voice == 1:
		file_info = bot.get_file(message.voice.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open('new_file.wav', 'wb') as new_file:
			new_file.write(downloaded_file)
		audio = pydub.AudioSegment.from_file('new_file.wav')
		audio = audio.set_sample_width(2)
		# audio = audio.set_frame_rate(48000)
		audio = audio.set_channels(1)
		chunks = pydub.silence.split_on_silence(audio, min_silence_len=1000, silence_thresh=-45)
		result = sum(chunks)
		chunkses = pydub.utils.make_chunks(result, 1000)
		os.makedirs('sample', exist_ok=True)
		for fr in os.listdir('sample'):
			os.remove(os.path.join('sample',fr))
		
		for i,chunk in enumerate(chunkses):
			if len(chunk) >= 1000:
				chunk.export(os.path.join('sample', f'voice_{i}.wav'), format='wav')
		preds = []
		for f in os.listdir('sample'):
			if os.path.isfile(os.path.join('sample',f)):
				x = tf.io.read_file(os.path.join('sample',f))
				x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=48000,)
				x = tf.squeeze(x, axis=-1)
				x = x[tf.newaxis,...]
				pred = friend_model(x)
				preds.append(np.argmax(pred))
		unique = Counter(preds).keys()
		num = Counter(preds).values()
		unique=list(unique)
		num=list(num)
		print("someone send a voice: ",persons[unique[np.argmax(num)]])
		bot.send_message(message.chat.id , f' صدات خیلی شبیه {persons[unique[np.argmax(num)]]} است.')
		new_voice = 0
	if singer == 1:
		file_info = bot.get_file(message.voice.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open('new_file.wav', 'wb') as new_file:
			new_file.write(downloaded_file)
		audio = pydub.AudioSegment.from_file('new_file.wav')
		audio = audio.set_sample_width(2)
		# audio = audio.set_frame_rate(48000)
		audio = audio.set_channels(1)
		chunks = pydub.silence.split_on_silence(audio, min_silence_len=2000, silence_thresh=-45)
		result = sum(chunks)
		chunkses = pydub.utils.make_chunks(result, 1000)
		os.makedirs('sample', exist_ok=True)
		for fr in os.listdir('sample'):
			os.remove(os.path.join('sample',fr))
		
		for i,chunk in enumerate(chunkses):
			if len(chunk) >= 1000:
				chunk.export(os.path.join('sample', f'voice_{i}.wav'), format='wav')
		preds = []
		for f in os.listdir('sample'):
			if os.path.isfile(os.path.join('sample',f)):
				x = tf.io.read_file(os.path.join('sample',f))
				x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=48000,)
				x = tf.squeeze(x, axis=-1)
				x = x[tf.newaxis,...]
				pred = singer_model(x)
				preds.append(np.argmax(pred))
		unique = Counter(preds).keys()
		num = Counter(preds).values()
		unique=list(unique)
		num=list(num)
		bot.send_message(message.chat.id , f' خواننده:  {singers[unique[np.argmax(num)]]}')
		print("singer: ",singers[unique[np.argmax(num)]])
		
		singer = 0




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
	global num,game,new_game,age,voice,max_number,argmax_number,myqrcode,image,new_voice
	print("vvvv")
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

	if new_voice == 1:
		bot.send_message(message.chat.id,"قرار بود فایل صوتی بفرستی.") 
		new_voice=0




bot.infinity_polling()