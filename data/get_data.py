# Only choose poetry with 5 words a sentence, 2 sentences in total

import glob
import json


datas = glob.glob("../TangPoetry/poet.*.json")

for data in datas:
    with open(data, 'r', encoding='utf-8') as f:
        poetry = json.load(f)
        for p in poetry:
            content = p['paragraphs']
            if len(content)==2 and len(content[0])==12 and len(content[1])==12:
                with open('../data/poetry.txt', 'a', encoding='utf-8') as f:
                    f.write("".join(content))
                    f.write('\n')
