from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("words1.csv")

words = df['word'].tolist()
weights = df['weight'].tolist()

weights_dict = dict(zip(words, weights))

wordcloud = WordCloud().generate_from_frequencies(weights_dict)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
