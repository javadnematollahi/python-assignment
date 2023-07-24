
# Machine learning 7_ LLS

LLS or linear least sqaure is a regression algorithm and it is useful for solving linear problem.

In this algorithm we find the slope of a line that pass through all the data.


## fisrt problem:

### Students Performance

In this problem I find a relation between study hours and grade of students with LLS algorithm.

First of all I made a data for study hours and grades of student with numpy library.
then I wrote a class for LLS algorithm and I use it for predict the slope of a line that pass through students data.

you can see the result and data in result part first problem.

## second problem:

### Boston house-prices

In this problem I find a relation between house price in boston and other parameter with LLS algorithm.

I use Boston dataset in kaggle site for this problem.
you can find this dataset in below link:
https://www.kaggle.com/datasets/puxama/bostoncsv

I find correlation of different features indataset to find two feature that have more relation to price of houses.

I found these two feature is rm and zn respectivily.

then I use my lls algorithm to find two slope.

and then I draw a 3d plot by using matplotlib. I showed my predicted plane and real data in this plot.
you can see this plot in result part second problem.


## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

#### first problem:

students data and predicted line with my LLS class.






students data and predicted line with my LLS class and predicted line with scipy:




#### second problem:

real data and the plane predicted with my lls algorithm


