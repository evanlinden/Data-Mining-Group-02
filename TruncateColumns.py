#Group 2
#CSPB 4502 - Data Mining
#Final Project

#Workflow: AddChangedColumn -> TruncateColumns -> MergeDatasets -> OptimizeClusterCount -> ClassifyData

#Import relevant libaries
import csv
import pandas as pd
import numpy as np

#Import reference csv
originaldata = pd.read_csv("fh_5yrs_modified.csv")

#Drop non-relevant columns to make file faster
originaldata.drop("Unnamed: 0",1, inplace=True)
originaldata.drop("volume",1, inplace=True)
originaldata.drop("open",1, inplace=True)
originaldata.drop("high",1, inplace=True)
originaldata.drop("low",1, inplace=True)
originaldata.drop("close",1, inplace=True)
originaldata.drop("adjclose",1, inplace=True)

#Export as a csv
originaldata.to_csv("fh_5yrs_modified_truncated.csv")