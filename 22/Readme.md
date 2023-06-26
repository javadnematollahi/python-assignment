
# todolist
In these project I use PySide6 library to create User Interface of todolist software.

This software has below features:

1. there is a database that your data store in it when add a new task.
2. you can delete a defined task by click on trash bottun beside of task. then the task is deleted from database and is 
   cleared from UI.
3. You can add priority to your task by choosing high or low radio bottun in the bottom of UI. the default priority is Low.
4. you can set a time for you task if you want by setting a time in timebox below the "Set Time For New Task" label.
5. If you checked a task, then you mean that task is done. and after that time when you open the software you'll see that task   is checked. 
6. If you set the priority of task to Low, the background color of task will be Green, and if you set the prioirity of your task to High then the background of you task will be Red.
7. When you oen the software, all your task sorted automatically so that the checked task will be down and the unchecked task will be on top.

I use pyinstaller library for this project to make an exe file so that you can download only the databse and main.exe to run the todolist software.



## How to install

Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python main.py


## Results

The UI of todolist software is shown below:

![todolistUI](https://github.com/javad7189/python-assignment/assets/86910174/ab985bc0-6aaa-4799-af0f-7ef8c512d8ca)
















