#Group 2
#CSPB 4502 - Data Mining
#Final Project

#Workflow: AddChangedColumn -> TruncateColumns -> MergeDatasets -> OptimizeClusterCount -> ClassifyData

#Import relevant libaries
import pandas as pd
import numpy as np

#Global counter
first = 0
count = 0

#Import reference csv
originaldata = pd.read_csv("fh_5yrs_modified_truncated.csv")

#Pull symbols column of data
symbols = originaldata["symbol"].to_numpy()

#Find unique symbols
uniquesymbols = list(set(symbols))

#Sort
uniquesymbols.sort()

#Run the following loop for all symbols
for symbol in uniquesymbols:

    #Pull portion of data with entries having a symbol that matches our loops symbol
    symboldf = originaldata[originaldata['symbol']==symbol]

    #Extract the date and higherthanyesterday values and put into a new temporary data frame
    symboldatelist = symboldf["date"].values.tolist()
    symbolhigherlist = symboldf["higherthanyesterday"].values.tolist()
    zippedlist = np.column_stack((symboldatelist,symbolhigherlist))
    tempdf = pd.DataFrame(zippedlist,columns = ['date',symbol])

    #If this is the first loop, create accumulator dataframe
    if (first == 0):
        compositedf = tempdf
        first = 1
    
    #Otherwise, join the temporary dataframe with the accumulator on date
    else:
        compositedf = compositedf.join(tempdf.set_index('date'), on='date')

    count = count + 1
    print(count)

#Transpose the data and fill all NaNs with 0s
compositedf = compositedf.set_index('date').transpose()
compositedf = compositedf.fillna(0)

#Print final dataframe and save into final csv: mergeddata.csv
print(compositedf)
compositedf.to_csv("mergeddata.csv")