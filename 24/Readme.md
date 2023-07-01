
# Thread

What is thread?

This is the question that we found its answer in this part.

If I want to explain an abstract about it I should say thread help us to run our code faster than past.
In fact thread can run several function at same time. 

For example when you must have more than one While loop in your code, then you must use thread to run all
While loop. without thread you cant do this because the code will be stick in first while loop.

another example is when you want run several function same time. In an online video conference software, you should play
video in the same time of audio. if you first play video in your code and then you play audio, your software always has a delay.
althought your hardware is very fast.


## first problem
to show this first I solve a problem one time in usual way and another time with thread and I compare the process time.

the problem is about convert video files to audio files. 
I convert 5 video files to audio file with moviepy library.

Without thread the process time is 30.3709774017334 second.
With thread the process time is 13.974942684173584 second.




In second problem I rewrite a part of interstellar game that I wrote it in 14th session.
when I want to creat enemy in this game I check time in onupdate method and each time 3 second has passed, I create a new enemy.
I use thread for this part. I mske a function which name is creat_enemy in Game class with a while loop and i use a 3second delay
to create new enemy. I put this function in a thread and I start it. So the main code will run and at the same time the create_enemy function will run too.


## How to install

Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
Run the cells in question1.ipynb file.

















