
# telegram bot with pytohn

Hi again.

In this part I want to do an interesting project. As you can see in title I write a telgram bot.

Lets do it:

At first we should go to @botfather bot. In this bot enter /newbot command. then you should enter a name for your bot and next you should enter a username for your bot. after that you received a Congratulations message and you also received a token.

Then you can write your bot.

I use python to write my bot. you should use your token in below line in your code.

bot = telebot.TeleBot(token, parse_mode=None)

If someone hack your token, you can get another token for your bot to solve the problem.

# Feature of my bot:

## you can enter my bot with below username:


@NEW_pylearn_bot



## My bot has below command:


/start
/game
/voice
/age
/max
/argmax
/qrcode
/help

##  /start:

This command send you a welcome message.

##  /game:

This command let you play guess numbers. In this game you should guess some numbers to guess the number that game has chosen.
If you can guess the correct number you will win. You can als play a new game whenever you want and you can exit the game by clicking Exit.

## /voice:

When you run this command, you should send an English text, then you received voice of your text. 

##  /age:

This command give your birth date and send you your age.

## /max:

This command give some numbers and send the biggest one of all.

##  /argmax:

This command give some numbers too and send index of the biggest one of all.

##  /qrcode

This command give a text and send you qrcode of that text.

##  /help:

This command send you an instruction that explain how to use bot.




## How to install
Run following command :

pip install -r requirements.txt


## How to Run

run in terminal:

 python NEW_pylearn_bot.py  to run bot.




















