import numpy as np

class Score():
    def __init__(self,labels):
        self.label=labels

    def true_positive(self,y_true, y_pred):
        tp = 0
        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                tp += 1
        return tp

    def true_negative(self,y_true, y_pred):
        tn = 0
        for yt, yp in zip(y_true, y_pred):
            if yt == 0 and yp == 0:
                tn += 1   
        return tn

    def false_positive(self,y_true, y_pred):
        fp = 0
        for yt, yp in zip(y_true, y_pred):
            if yt == 0 and yp == 1:
                fp += 1 
        return fp

    def false_negative(self,y_true, y_pred):
        fn = 0
        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 0:
                fn += 1
        return fn
    

    def macro_precision(self,y_true, y_pred):

        # find the number of classes
        num_classes = len(self.label)

        # initialize precision to 0
        precision = 0
        
        # loop over all classes
        for class_ in list(self.label):
            
            # all classes except current are considered negative
            temp_true = [1 if p == class_ else 0 for p in y_true]
            temp_pred = [1 if p == class_ else 0 for p in y_pred]
            
            
            # compute true positive for current class
            tp = self.true_positive(temp_true, temp_pred)
            
            # compute false positive for current class
            fp = self.false_positive(temp_true, temp_pred)
            
            
            # compute precision for current class
            temp_precision = tp / (tp + fp)
            # keep adding precision for all classes
            precision += temp_precision
            
        # calculate and return average precision over all classes
        precision /= num_classes
        precision=round(precision, 4)
        return precision
    

    def micro_precision(self,y_true, y_pred):


        # find the number of classes 
        num_classes = len(self.label)
        
        # initialize tp and fp to 0
        tp = 0
        fp = 0
        
        # loop over all classes
        for class_ in list(self.label):
            
            # all classes except current are considered negative
            temp_true = [1 if p == class_ else 0 for p in y_true]
            temp_pred = [1 if p == class_ else 0 for p in y_pred]
            
            # calculate true positive for current class
            # and update overall tp
            tp += self.true_positive(temp_true, temp_pred)
            
            # calculate false positive for current class
            # and update overall tp
            fp += self.false_positive(temp_true, temp_pred)
            
        # calculate and return overall precision
        precision = tp / (tp + fp)
        return precision
    

    def macro_recall(self,y_true, y_pred):

        # find the number of classes
        num_classes = len(self.label)

        # initialize recall to 0
        recall = 0
        
        # loop over all classes
        for class_ in list(self.label):
            
            # all classes except current are considered negative
            temp_true = [1 if p == class_ else 0 for p in y_true]
            temp_pred = [1 if p == class_ else 0 for p in y_pred]
            
            
            # compute true positive for current class
            tp = self.true_positive(temp_true, temp_pred)
            
            # compute false negative for current class
            fn = self.false_negative(temp_true, temp_pred)
            
            
            # compute recall for current class
            temp_recall = tp / (tp + fn + 1e-6)
            
            # keep adding recall for all classes
            recall += temp_recall
            
        # calculate and return average recall over all classes
        recall /= num_classes

        recall=round(recall, 4)
        
        return recall
    

    def micro_recall(self,y_true, y_pred):


        # find the number of classes 
        num_classes = len(self.label)
        
        # initialize tp and fp to 0
        tp = 0
        fn = 0
        
        # loop over all classes
        for class_ in list(self.label):
            
            # all classes except current are considered negative
            temp_true = [1 if p == class_ else 0 for p in y_true]
            temp_pred = [1 if p == class_ else 0 for p in y_pred]
            
            # calculate true positive for current class
            # and update overall tp
            tp += self.true_positive(temp_true, temp_pred)
            
            # calculate false negative for current class
            # and update overall tp
            fn += self.false_negative(temp_true, temp_pred)
            
        # calculate and return overall recall
        recall = tp / (tp + fn)
        return recall
