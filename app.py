
'''
메타데이터 항목
1) Cover Image :
2) Video Uri :
3) Song Name :
4) Singer : 
5) Song By :
6) Lyrics By : 
7) Arrangement : 
8) Publish date : 
9) Serial Number : 
10) Introduction :
'''
from flask import Flask,jsonify

app = Flask(__name__)

'''
attr list
'''

COVER_IMAGE = [
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/Qmd9X8pJopGNnkQV6PUTUfv3gsQGPWXBDfjtpt3hySYJwt.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/Qmd9X8pJopGNnkQV6PUTUfv3gsQGPWXBDfjtpt3hySYJwt.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/Qmd9X8pJopGNnkQV6PUTUfv3gsQGPWXBDfjtpt3hySYJwt.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmQuMeuc2aqNFNHZzAN1reneC2dnd2fYvQFMw8qg9ZpKcG.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmQuMeuc2aqNFNHZzAN1reneC2dnd2fYvQFMw8qg9ZpKcG.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmQuMeuc2aqNFNHZzAN1reneC2dnd2fYvQFMw8qg9ZpKcG.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmfPTMshjisYCeGQJxR2GkD7y6ZB7mTKtEc7jsQWcLjn7h.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmfPTMshjisYCeGQJxR2GkD7y6ZB7mTKtEc7jsQWcLjn7h.jpg',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmfPTMshjisYCeGQJxR2GkD7y6ZB7mTKtEc7jsQWcLjn7h.jpg',    
]
VIDEO_URI = [
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
]
PREVIEW_URI = [
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmacnJ6mk2Z36mqDbCo1DsE4SKzMQxPZjcuNfZRPdf6Jnv.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmacnJ6mk2Z36mqDbCo1DsE4SKzMQxPZjcuNfZRPdf6Jnv.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmacnJ6mk2Z36mqDbCo1DsE4SKzMQxPZjcuNfZRPdf6Jnv.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmaZ13JbZokWszrNuohgZrvAC6nEPUtpmPXx574wdAwzcy.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmaZ13JbZokWszrNuohgZrvAC6nEPUtpmPXx574wdAwzcy.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmaZ13JbZokWszrNuohgZrvAC6nEPUtpmPXx574wdAwzcy.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmYRHpyCSoLBwK2s7L4UWdwoJk97nKJEHNaWY1i7hEnyu3.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmYRHpyCSoLBwK2s7L4UWdwoJk97nKJEHNaWY1i7hEnyu3.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmYRHpyCSoLBwK2s7L4UWdwoJk97nKJEHNaWY1i7hEnyu3.mp3',
]
SOURCE_URI = [
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmXGtPsV6GG2zN28srTLhmEAd7Kp8ZUNUspuUv3yLnSKSf.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmXGtPsV6GG2zN28srTLhmEAd7Kp8ZUNUspuUv3yLnSKSf.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmXGtPsV6GG2zN28srTLhmEAd7Kp8ZUNUspuUv3yLnSKSf.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmUesyw5W9TaMu7WkLFTWkjv1swUTXrg8ZrHhkay9aoxjV.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmUesyw5W9TaMu7WkLFTWkjv1swUTXrg8ZrHhkay9aoxjV.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmUesyw5W9TaMu7WkLFTWkjv1swUTXrg8ZrHhkay9aoxjV.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmYiuJTGpGDf1SfMXcfhJvVUxPbrkbVG4W1Nu9GGKqGBHg.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmYiuJTGpGDf1SfMXcfhJvVUxPbrkbVG4W1Nu9GGKqGBHg.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmYiuJTGpGDf1SfMXcfhJvVUxPbrkbVG4W1Nu9GGKqGBHg.mp3',
]
SONG_NAME = [
    'Break',
    'Break',
    'Break',
    'RedMoon',
    'RedMoon',
    'RedMoon',
    'LunaBebop',
    'LunaBebop',
    'LunaBebop',
]
SINGER = [
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
]
SONG_BY = [
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    ]
LYRICS_BY = [
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    ]
ARRANGEMENT = [
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    'OwO',
    ]
PUBLISH_DATE = [
    '2020-02-09',
    '2020-02-09',
    '2020-02-09',
    '2021-03-01',
    '2021-03-01',
    '2021-03-01',
    '2020-12-29',
    '2020-12-29',
    '2020-12-29',
    ]
SERIAL_NUMBER = [
    'AQNFT-M-1-00001',
    'AQNFT-M-1-00002',
    'AQNFT-M-1-00003',
    'AQNFT-M-2-00001',
    'AQNFT-M-2-00002',
    'AQNFT-M-2-00003',
    'AQNFT-M-3-00001',
    'AQNFT-M-3-00002',
    'AQNFT-M-3-00003',
    ]
INTRODUCTION = [
    'We remember the broken pieces of our hearts hurt. I want to throw that moment away like trash, but it stays in my mind forever',
    'We remember the broken pieces of our hearts hurt. I want to throw that moment away like trash, but it stays in my mind forever',
    'We remember the broken pieces of our hearts hurt. I want to throw that moment away like trash, but it stays in my mind forever',
    'There is a moon shining red in time and space, and there is another image of me shining red.',
    'There is a moon shining red in time and space, and there is another image of me shining red.',
    'There is a moon shining red in time and space, and there is another image of me shining red.',
    'Someday you\'ll enjoy jazz played by robots.',
    'Someday you\'ll enjoy jazz played by robots.',
    'Someday you\'ll enjoy jazz played by robots.',
    ]

def _add_attribute(existing, attribute_name, options, token_id):
    trait = {
        'trait_type': attribute_name,
        # MINT 시작은 0부터
        'value': options[token_id]
    }    
    existing.append(trait)

@app.route('/api/<token_id>')
def creature(token_id):  
    try:
        token_id = int(token_id)
    except:
        return jsonify({
            'error' : 'token_id is not integer'
        })

    if token_id >= len(SERIAL_NUMBER) or token_id < 0:
        return jsonify({
            'error' : 'out of token_id range'
        })

    attributes = []
    _add_attribute(attributes, 'cover-image', COVER_IMAGE, token_id)
    _add_attribute(attributes, 'video-uri', VIDEO_URI , token_id)
    _add_attribute(attributes, 'preview-uri', PREVIEW_URI , token_id)
    _add_attribute(attributes, 'source-uri', SOURCE_URI , token_id)
    _add_attribute(attributes, 'song-name', SONG_NAME, token_id)
    _add_attribute(attributes, 'singer', SINGER, token_id)
    _add_attribute(attributes, 'song-by', SONG_BY, token_id)
    _add_attribute(attributes, 'lyrics-by', LYRICS_BY, token_id)
    _add_attribute(attributes, 'arrangement', ARRANGEMENT, token_id)
    _add_attribute(attributes, 'publish-date', PUBLISH_DATE, token_id)
    _add_attribute(attributes, 'serial-number', SERIAL_NUMBER, token_id)
    _add_attribute(attributes, 'introduction', INTRODUCTION, token_id)

    return jsonify({
        'name': SONG_NAME[token_id],
        'description': INTRODUCTION[token_id],
        'image' : COVER_IMAGE[token_id],
        'external_url' : 'https://alphaquark.io',
        'attributes' : attributes
    })

    return jsonify({
if __name__=='__main__':
    app.run(host='0.0.0.0')