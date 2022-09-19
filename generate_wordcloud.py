import os
from wordcloud import WordCloud

from config import FONT_PATH


def generate_wordcloud(text):
    wordcloud = WordCloud(
        font_path=FONT_PATH,
        width=800,
        height=600,
        background_color='white',
        max_words=500,
    ).generate(text)
    wordcloud.to_file('wordcloud.png')
