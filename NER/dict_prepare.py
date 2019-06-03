"""
create a vocabulary from source data, and write it to "word2id.pkl".
"""
import os
import collections
import pickle

def word_count(file_path):
    """
    word frequency count
    """
    word_freq = collections.defaultdict(int)
    with open(file_path) as f:
        for l in f:
            for w in l.strip().split():  
                word_freq[w] += 1
    return word_freq
    #return word_freq.items()  # return a list

def build_dict(file_path, min_word_freq=1):
    """
    build a dict from a given file
    """
    word_freq = word_count(file_path)
    word_freq = filter(lambda x: x[1] > min_word_freq, word_freq.items()) # filter将词频数量低于指定值的单词删除。
    word_freq_sorted = sorted(word_freq, key=lambda x: (-x[1], x[0]))
    words, _ = list(zip(*word_freq_sorted))
    word_idx = dict(zip(words, range(len(words))))
    word_idx['<UNK>'] = len(words) #unk表示unknown，未知单词
    return word_idx

def to_pkl(data, file_path):
    """
    write data to a .pkl file
    """
    with open(file_path,'wb') as f:
        pickle.dump(data, f)

def read_dictionary(vocab_path):
    """

    :param vocab_path:
    :return:
    """
    vocab_path = os.path.join(vocab_path)
    with open(vocab_path, 'rb') as fr:
        word2id = pickle.load(fr)
    print('vocab_size:', len(word2id))
    return word2id

data_path = './data'
f_source_data = os.path.join(data_path, 'source_data.txt') 

word2id = build_dict(f_source_data)
to_pkl(word2id, os.path.join(data_path, 'word2id.pkl'))
print('dict size:', len(word2id))
word2id = read_dictionary(os.path.join(data_path, 'word2id.pkl'))
print(word2id[:2])