
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
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmP2RYiu9Y15Xa9gy1zoayCfrnb7cZgu6jeZsejCnmC9xS.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmPgdRfGkKWk1ofEqEopbwdCq1zFbMpvHhUBDkybPFbQXr.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmVMpGbtmHWQW1hogq6Gx7Mipe28Q8whbn4quh9xrycv4m.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmZ954wbGKDnpNE65RNyPCK2dnJsh49UfWVQApGwVASet7.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmSSHz8JMixkUxtrqZRv7zhGPKFghmSx9cpswd2TdHwPv6.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmasRHdjZMYPcWcUiKx8u3WJqpg2LySnLbpBNPAetnKE2n.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmUfFvETTc9BeBBEgo7zzrLGyP3E9Fd6waQVp6wA6qisxK.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmWXSLyEFffhqT9zzS2PBH9V4o1iGUStXs2ko4RLAqt9UQ.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmUa6NoPu3VwWfVTwTtSzchR8xhH7Mg3fkdu9JAt8frjM8.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmVkoXATCg9bfR4UaNETVuqRmW9Acm82Ku3U15oJ2wpVPW.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmUAHwSd3Z6dLzuaDD4CRjtYJF1PvtNwauH5oBbdFfunJ2.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmUYQ2JXoCJ7u1rRs4b7s47kwa4PLs1UDxYfpGLKMYKXLm.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmZ9Q6E1HP7mpUDPWpmhKVTnqaQdSx8JpSBmoAeNzeWjpk.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmTB2GGLkg2feDbbVexYE6FjmN3n5PkWancmPgkVwaoAM6.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmYAX4UwfkGBqUpXTjR3v8QRzhCUpeKd96qKDshP7ixsHe.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmahVtjEkVRuDNFA1PZ6HW9kA11Y16DBmDUQ2DmySi1LHy.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmPe3v9Avkdbbig6d4rwT9SYkVYax3AwPVXcW6MgnsPBZo.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmPhWdmAZPxxj4ajYdtVcb9BktCnUzCzePFSuQhHZWrdLh.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmZJ8y95eJ5iKdWDTANS9yQ8X7k6H9urXtktQHyXytSbuy.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmbJfAA5stLoKJkADbUJxqx7jzRAJG6JVjugRYqKYvs6hp.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmYy6AaPaszVLUfX6o9KyNjBF3SW3eGHbA2exzTwzwiebR.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmT7iQV6p1BcCkodF4Ww8MHYmX94tjnU46CNKFccXQjd2L.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmNa5ZNL4dhXTRhcGnDaXuQwY7zqX1vAVcH9izxq2G15Ee.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmRyqtHUe94Yj5WMrzRrT7KdWczHs1jVYW6MLLByTbBvBv.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmSpVbBXW1HnBN1DdVemjj7WLmMfteDFX1cwj5VgHydNp1.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/Qmdy1jc8ct1NMnKrJNSfTU51QALwZyMoS4ps7zsnDim5mN.png',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/cover/QmU6M2YLicX1ww3vL3nritLsdwyvuxBbu2uBCeX3fV5hnz.png',
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
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
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
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmdBV3Q6ucQuuvDBNQQ9LYmpu71FQEYFBoe1nhhd9Chkfd.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmdBV3Q6ucQuuvDBNQQ9LYmpu71FQEYFBoe1nhhd9Chkfd.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmdBV3Q6ucQuuvDBNQQ9LYmpu71FQEYFBoe1nhhd9Chkfd.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmNkoox7Q2Jt1icSJiTEEeCxCnswv8QvVo3atwJgapLYfD.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmNkoox7Q2Jt1icSJiTEEeCxCnswv8QvVo3atwJgapLYfD.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmNkoox7Q2Jt1icSJiTEEeCxCnswv8QvVo3atwJgapLYfD.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmSDqV5Pfinq72jH8W1F5nRiDqmbr5FMyuMzrYdVBzFpDw.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmSDqV5Pfinq72jH8W1F5nRiDqmbr5FMyuMzrYdVBzFpDw.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmSDqV5Pfinq72jH8W1F5nRiDqmbr5FMyuMzrYdVBzFpDw.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeedpL9D1znDY22ddjmY7jSzbmSh6EQSYyEXnRectvJdP.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeedpL9D1znDY22ddjmY7jSzbmSh6EQSYyEXnRectvJdP.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeedpL9D1znDY22ddjmY7jSzbmSh6EQSYyEXnRectvJdP.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmRUKBeCNeSahjcZhZgm2UXg72ADdaKyKmzPmcFZcfy787.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmRUKBeCNeSahjcZhZgm2UXg72ADdaKyKmzPmcFZcfy787.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmRUKBeCNeSahjcZhZgm2UXg72ADdaKyKmzPmcFZcfy787.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeZmw4ZyCJiEgS7QdQuq2NkNwnu3FTSuiMDpy1gQwa8VD.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeZmw4ZyCJiEgS7QdQuq2NkNwnu3FTSuiMDpy1gQwa8VD.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/preview/QmeZmw4ZyCJiEgS7QdQuq2NkNwnu3FTSuiMDpy1gQwa8VD.mp3',
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
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmbg7RWixQAwHckaoZKS4EqT6N8UFjJ4k8u7jLThqPdAgU.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmbg7RWixQAwHckaoZKS4EqT6N8UFjJ4k8u7jLThqPdAgU.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmbg7RWixQAwHckaoZKS4EqT6N8UFjJ4k8u7jLThqPdAgU.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmd3YXLZcPtPgkHiqFX5UiiDmfRdaBZEdkHBRf7vjDNYK5.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmd3YXLZcPtPgkHiqFX5UiiDmfRdaBZEdkHBRf7vjDNYK5.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/Qmd3YXLZcPtPgkHiqFX5UiiDmfRdaBZEdkHBRf7vjDNYK5.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmZ9muMUeawC3HmsZkGnNFodz4ETYSQYFfvsigTShMDsDC.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmZ9muMUeawC3HmsZkGnNFodz4ETYSQYFfvsigTShMDsDC.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmZ9muMUeawC3HmsZkGnNFodz4ETYSQYFfvsigTShMDsDC.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmNM2LvKF6TDwvvW7fZxyM56aj75KM8b3vu58HY9jPffwz.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmNM2LvKF6TDwvvW7fZxyM56aj75KM8b3vu58HY9jPffwz.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmNM2LvKF6TDwvvW7fZxyM56aj75KM8b3vu58HY9jPffwz.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmaHWieNLaEg7d3ozw82BkFTLDYYyCV6mYxCQYhjWhqv1n.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmaHWieNLaEg7d3ozw82BkFTLDYYyCV6mYxCQYhjWhqv1n.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmaHWieNLaEg7d3ozw82BkFTLDYYyCV6mYxCQYhjWhqv1n.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmQrHEqMxczLQcSFghBQMbHtFBEB3y8Xv93wBZWc3r98rZ.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmQrHEqMxczLQcSFghBQMbHtFBEB3y8Xv93wBZWc3r98rZ.mp3',
    'https://aqt-metadata.s3.ap-northeast-2.amazonaws.com/source/QmQrHEqMxczLQcSFghBQMbHtFBEB3y8Xv93wBZWc3r98rZ.mp3',
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
    'AWPF07209',
    'AWPF07209',
    'AWPF07209',
    'Mark',
    'Mark',
    'Mark',
    'Waitomo361538S1750613E',
    'Waitomo361538S1750613E',
    'Waitomo361538S1750613E',
    'Amalfi',
    'Amalfi',
    'Amalfi',
    'Incubus',
    'Incubus',
    'Incubus',
    'Runway',
    'Runway',
    'Runway',
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
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
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
    'WALL e',
    'WALL e',
    'WALL e',
    '901D',
    '901D',
    '901D',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'germ',
    'germ',
    'germ',
    '901D',
    '901D',
    '901D',
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
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
    'NONE',
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
    'WALL e',
    'WALL e',
    'WALL e',
    '901D',
    '901D',
    '901D',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'PJ',
    'germ',
    'germ',
    'germ',
    '901D',
    '901D',
    '901D',
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
    '2021-04-02',
    '2021-04-02',
    '2021-04-02',
    '2020-03-28',
    '2020-03-28',
    '2020-03-28',
    '2020-12-15',
    '2020-12-15',
    '2020-12-15',
    '2019-08-02',
    '2019-08-02',
    '2019-08-02',
    '2020-10-01',
    '2020-10-01',
    '2020-10-01',
    '2021-01-15',
    '2021-01-15',
    '2021-01-15',
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
    'AQNFT-M-4-00001',
    'AQNFT-M-4-00002',
    'AQNFT-M-4-00003',
    'AQNFT-M-5-00001',
    'AQNFT-M-5-00002',
    'AQNFT-M-5-00003',
    'AQNFT-M-6-00001',
    'AQNFT-M-6-00002',
    'AQNFT-M-6-00003',
    'AQNFT-M-7-00001',
    'AQNFT-M-7-00002',
    'AQNFT-M-7-00003',
    'AQNFT-M-8-00001',
    'AQNFT-M-8-00002',
    'AQNFT-M-8-00003',
    'AQNFT-M-9-00001',
    'AQNFT-M-9-00002',
    'AQNFT-M-9-00003',
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
    'The planet Earth is almost uninhabitable! Noah\'s Ark departs Earth and heads for planet AWPF07209. They have hope!',
    'The planet Earth is almost uninhabitable! Noah\'s Ark departs Earth and heads for planet AWPF07209. They have hope!',
    'The planet Earth is almost uninhabitable! Noah\'s Ark departs Earth and heads for planet AWPF07209. They have hope!',
    'She knows! But that\'s not true!',
    'She knows! But that\'s not true!',
    'She knows! But that\'s not true!',
    'Firefly Cave found by the Maori of New Zealand! Waitomo!',
    'Firefly Cave found by the Maori of New Zealand! Waitomo!',
    'Firefly Cave found by the Maori of New Zealand! Waitomo!',
    'In a car running on the coast of Amalfi, Italy...',
    'In a car running on the coast of Amalfi, Italy...',
    'In a car running on the coast of Amalfi, Italy...',
    'The place that comes out in your dreams every day, the person... Who are you?',
    'The place that comes out in your dreams every day, the person... Who are you?',
    'The place that comes out in your dreams every day, the person... Who are you?',
    'Everyone in the world is excited by the sexy back of the model after walking',
    'Everyone in the world is excited by the sexy back of the model after walking',
    'Everyone in the world is excited by the sexy back of the model after walking',
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
        token_id = int(token_id)-1
    except:
        return jsonify({
            'error' : 'token_id is not integer'
        })

    if token_id > len(SERIAL_NUMBER)-1 or token_id < -1:
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

'''
"description":"Intellectual property backed NFT items powered by Alpha Quark",
"external_url":"https://alphaquark.io",
"image":"ipfs://해시값",
"name":"AlphaQuark NFT"
'''
@app.route('/contract/info')
def contractInfo():
    return jsonify({
        'name': 'AlphaQuark NFT',
        'description': 'Intellectual property backed NFT items powered by Alpha Quark',
        'image' : 'https://ipfs.io/ipfs/QmVUhm56KnARNsuqf2rewR1yAeZEaUuFUaN4h5Ek8xQzAP',
        'external_url' : 'https://alphaquark.io',
        'seller_fee_basis_points': 500, # Indicates a 5% seller fee.
        'fee_recipient': '0xA0346C590Dd9baE8F74E1A8b332ff5184c784A57' # Where seller fees will be paid to.
    })

if __name__=='__main__':
    app.run(host='0.0.0.0')