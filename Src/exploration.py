import os
import pandas as pd 

#y_train = pd.read_csv("../Data/Y_train_CVw08PX.csv)

filename_ytrain = os.path.join(os.path.dirname(__file__), "../Data/Y_train_CVw08PX.csv")
filename_Xtrain = os.path.join(os.path.dirname(__file__), "../Data/X_train_update.csv")
filename_Xtest = os.path.join(os.path.dirname(__file__), "../Data/X_test_update.csv")


print(filename_ytrain)
y_train = pd.read_csv(filename_ytrain)
print(y_train.shape)
X_train = pd.read_csv(filename_Xtrain)
print(X_train.shape)
X_test = pd.read_csv(filename_Xtest)
print(X_test.shape)

