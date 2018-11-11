# Kalana Dhanajaya Rathnayake 
# University of Peradeniya 
# Faculty of Engineering 

# Text Classification using Machine Learning


# import  lib 
import pandas as pd 

# import file


class Read_File:

    def __init__(self):
        data = pd.read_csv('trainset.txt', delimiter="\t")
        data.columns = ["class", "title", "date", "body"]
        print(data.class[0])