from email.quoprimime import unquote
import pandas as pd

unique_words = set()

df = pd.read_csv('test.csv')

print(df)

def add_to_set(sent):
    for i in sent.split(" "):
        unique_words.add(i)

df['Sentences'].apply(add_to_set)
print(unique_words)

def convert_to_bags(sent):
    arr = [0] * len(unique_words)
    unique_words_list = list(unique_words)
    for i in sent.split(" "):
        arr[unique_words_list.index(i)] += 1
    return arr

df['BOW'] = df['Sentences'].apply(convert_to_bags)
print(df)