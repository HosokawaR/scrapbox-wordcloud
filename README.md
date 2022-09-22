# Scrapbox Wordcloud Generator

## What is ?

A generator that generates a wordcloud from [Scrapbox](https://scrapbox.io/) running on Cloud Function with Cloud Storage.

This use [word_cloud](https://github.com/amueller/word_cloud).

## How to run

Copy `config.py.example` to `config.py`, and fill these value as below.

```py
# config.py

FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'

SCRAPBOX_PROJECT_NAME = 'HosokawaR'

USE_CACHE = False

CLOUD_FONT_PATH = 'https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip'
SAVED_FONT_DIR = '/tmp'
SAVED_FONT_PATH = '/tmp/NotoSansCJKjp-Regular.otf'

BUCKET_NAME = '<GCP Bcuket name>'
BUCKET_FILE_NAME = 'wordcloud.png'
FILENAME = '/tmp/wordcloud.png'
```

You can run this in console or cloud functions.

In Console, you need to use [poetry](https://github.com/python-poetry/poetry).

```bash
$ poetry shell
$ poetry install
$ python3 main.py
```
