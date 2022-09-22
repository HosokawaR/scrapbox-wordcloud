import requests
import zipfile
import io
from wordcloud import WordCloud

from config import CLOUD_FONT_PATH, SAVED_FONT_PATH, SAVED_FONT_DIR, FILENAME


def download_font():
    print('Downloading font...')
    url = CLOUD_FONT_PATH
    res = requests.get(url)
    zip = zipfile.ZipFile(io.BytesIO(res.content))
    zip.extractall(path=SAVED_FONT_DIR)


def generate_wordcloud(text):
    download_font()

    wordcloud = WordCloud(
        font_path=SAVED_FONT_PATH,
        width=1600,
        height=1200,
        background_color='white',
        max_words=500,
    ).generate(text)
    wordcloud.to_file(FILENAME)

    return wordcloud.to_image()