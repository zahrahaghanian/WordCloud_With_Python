import pandas as pd

import matplotlib.pyplot as plt
from wordcloud import WordCloud
text = "sample text to create wordcloud"
weights = {'sample': 10, 'text': 5, 'create': 8, 'wordcloud': 5}

wordcloud = WordCloud().generate_from_frequencies(weights)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
