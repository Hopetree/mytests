# -*- coding: utf-8 -*-
import emoji
import requests
import json

def get_data():
    url = 'http://emoji.muan.co/javascripts/emojilib/emojis.json'
    html = requests.get(url).text
    data = json.loads(html)
    return data

def main():
    lis_b = []
    lis_a = []
    data = get_data()
    for key in data:
        text = ':{}:'.format(key)
        emo = emoji.emojize(text,use_aliases=True)
        if key != emo:
            lis_b.append(text)
            lis_a.append(emo)
    print(lis_b)
    print(lis_a)




if __name__ == '__main__':
    main()