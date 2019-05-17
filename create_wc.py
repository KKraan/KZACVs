import pickle
import csv
from wordcloud import WordCloud
from io import BytesIO
from collections import Counter

with open('result/expertise.pickle', 'rb') as handle:
    b = pickle.load(handle)


with open('result/expertise.csv') as csv_file:
    text = ''
    for row in csv.reader(csv_file):
        text += str(row)

rows = text.split('", "')
cols = []
test = []
for row in rows:
    col = row.replace("'","").replace("[","").replace("]","").replace('"','')
    col = col.split(',')
    cols.append(col)
    test.extend(col)

wc = WordCloud(
    background_color="white",
    # width=700,
    # height=500,
    width=500,
    height=350,
    colormap="Dark2"
    # max_words=50,
    #max_font_size=30
    )
wc.generate_from_frequencies(frequencies=Counter(test))
wc.to_file("result/exp.png")
print(Counter(test))
