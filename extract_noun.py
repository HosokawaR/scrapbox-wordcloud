import re
import MeCab

tagger = MeCab.Tagger()
tagger.parse('')

stop_words = ['ため', 'とき', 'こと', 'もの']


def clean(text):
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    return text


def extract_noun(text):
    text = clean(text)
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        features = node.feature.split(',')
        if features[0] == '名詞' and features[1] not in [
                '数', '非自立'
        ] and node.surface not in stop_words:
            nouns.append(node.surface)
        node = node.next

    return ' '.join(nouns)
