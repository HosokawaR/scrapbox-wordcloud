import pickle
from os import path

from fetch_contents import fetch_from_scrapbox
from extract_noun import extract_noun
from generate_wordcloud import generate_wordcloud
from save_to_storage import save_file
from config import USE_CACHE


# Cloud Functions calls this function with two arguments 
# So we need to define two arguments to avoid calling errors
def generate_scrapbox_wordcloud(data, context):
    if USE_CACHE and path.exists('page_contents.pickle'):
        print('Loading from pickle.')
        with open('page_contents.pickle', 'rb') as f:
            page_contents = pickle.load(f)
    else:
        print('Fetching contents from Scrapbox.')
        page_contents = fetch_from_scrapbox()
        if USE_CACHE:
            with open('page_contents.pickle', 'wb') as f:
                pickle.dump(page_contents, f)

    nouns = extract_noun(page_contents)
    generate_wordcloud(nouns)
    save_file()

    return 'Done!'


if __name__ == "__main__":
    generate_scrapbox_wordcloud({}, {})
