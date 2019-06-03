"""
create source dataset from source_data.txt and source_label.txt
"""
from data import read_corpus
import os

data_path = './data'
f_source_data = os.path.join(data_path, 'source_data.txt') 
f_source_label = os.path.join(data_path, 'source_label.txt')
# with open(f_source_data, 'r') as f_sd, open(f_source_label, 'r') as f_sl:
data = read_corpus(f_source_data, f_source_label)
print(data[:3])
print(len(data[0][0]), len(data[0][1]))
print(len(data[1][0]), len(data[1][1]))
print(len(data[2][0]), len(data[2][1]))
    
