#Group 2
#CSPB 4502 - Data Mining
#Final Project

#Workflow: AddChangedColumn -> TruncateColumns -> MergeDatasets -> OptimizeClusterCount -> ClassifyData

#Import relevant libaries
import pandas as pd
import numpy as np

#Import reference csv
originaldata = pd.read_csv("fh_5yrs.csv")

#Extract symbol and close columns for analysis
symbols = originaldata["symbol"].to_numpy()
close = originaldata["close"].to_numpy()

#Create an list the length of the data and prefill with 0s
increased = np.zeros(len(symbols))

#For each row, compare the previous row. If the symbol is the same and the close value
#has increased, change the 0 to a 1.
for i in range(1,len(symbols)):
    if symbols[i] == symbols[i-1] and close[i-1] < close[i]:
        increased[i] = 1

#Append to dataframe
originaldata["higherthanyesterday"] = increased

#Export as a csv
originaldata.to_csv("fh_5yrs_modified.csv")