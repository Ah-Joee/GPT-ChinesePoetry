# Only choose poetry with 5 words a sentence, 2 sentences in total

# -*- conding:utf-8 -*-
import glob
import json

datas = glob.glob("./TangPoetry/poet*json")

for data in datas:

    # 載入文件
    with open(data, 'r', encoding='utf-8') as load:
        poetry = json.load(load)
        # 取每一首詩的內容
        for p in poetry:
            # 只取五言絕句
            content = p['paragraphs']
            if len(content)==2 and len(content[0])==12 and len(content[1])==12:
                with open('./data/ChinesePoetry/ChinesePoetry.txt', 'a', encoding='utf-8') as f:
                    f.write("".join(p['paragraphs']))
                    f.write('\n')
