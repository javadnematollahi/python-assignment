# Emoji_text_Classification

In this part we want to calssify text to five class:



## Description

For text classification I use feature of each word. These features are provided by standford NLP team for 6B tokens.

link of word features:

https://nlp.stanford.edu/data/glove.6B.zip

Our dataset include some sentences about five subjects. The subject are our classes and they are about love, sport, pleasure, sad, food and I choose an emoji for each subject respectevily.  ["❤️", "⚾", "🙂", "😒", "🍴" ]

link of dataset:

https://drive.google.com/drive/folders/1bgbdrrIAxBeof4cwuM5H15Azehr68TwT?usp=sharing

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run Below command in terminal to play snake:

```
python emoji_text_classification.py
```


# results

I use just one dense layer with 5 neuron because I have 5 class.

For 50d feature, loss and accuray were 0.6375,0.8214 and when I add a dropout layer before dense layer the loss and accuray were 0.7824 and 0.8214.

| Feature vector dimension  | Train Loss | Train Accuracy  | Test Loss | Test Accuracy  | Inference Time |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 50d  | 0.5123  | 0.8485  | 0.6375  | 0.8214  | 0.0609s  |
| 100d  | 0.3826  | 0.9394  | 0.5790  | 0.8750  | 0.0616s  |
| 200d  | 0.3844  | 0.9318  | 0.5583  | 0.8750  | 0.0705s  |
| 300d  | 0.2233  | 0.9848  | 0.5236  | 0.8750  | 0.0731s  |





