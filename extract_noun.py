from concurrent.futures import process
import MeCab

tagger = MeCab.Tagger()
tagger.parse('')


def extract_noun(text):
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        features = node.feature.split(',')
        if features[0] == '名詞':
            nouns.append(node.surface)
        node = node.next
    return nouns
