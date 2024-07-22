

#l = 'G-8stBV8oUcShOn8pExTllDhw3aPLRW6ljwjXtEoaW6oR7DtluyKMls5qbTPLYXeOzsewcAt5ZOlRX74cwCjewqqqBwY69ZH_zMpCEDzwNBQRAnBrEAl_ij8Hfp4i8eJqDFEBFVR-5SfQM7F-xQNYT08eGdsRjLK1Qq2AVuNy1Tp2wVQ3VtGXirnU1NmZiiUS8Vr1ZYZZbbkCuvls40i1gWdqMmvq9Yl64xTztFNhQDNO8N6wQKL0gC0K--59vLIqZ0FyQH52d63OUqw5m4EohE2Hj7lW_jE9r8SASsIfuIoJ7kCO2gBMfXu6avU-A'
#l = 'h93FB_Yx96wSitFh6ofhxY9KsZ8-2xX5XliFJKL5aPPaJXlOjSgzqBIzI2D4YawTquO4TZaCSYGi3tCGXqtrk8FxNk52JhCsfhcjbFjbMADBHEzzbKxhb6X9Z6LO1joZXTU7Wf1Yn12zYn9Heq-oCljC8GJVVWxBRxWF6QZ8HmONKOgXm-T-zY5MFMHXZUrOiBH_GVZhJWpxmQZ5CBlpIBzdwrJ2h77Nc3RGwY3lJ80oRcNuZRzVdNelyf0cfJPG5I95o9cms7_3-_lIWF4Z6nawvMk0UwEeXMdpN5fA'
import base64
import logging
import time

import requests
R = [188, 174, 178, 234, 171, 147, 70, 82, 76, 72, 192, 132, 60, 17, 30, 127, 184, 233, 48, 105, 38, 232, 240, 21, 47, 252, 41, 229, 209, 213, 71, 40, 63, 152, 156, 88, 51, 141, 139, 145, 133, 2, 160, 191, 11, 100, 10, 78, 253, 151, 42, 166, 92, 22, 185, 140, 164, 91, 194, 175, 239, 217, 177, 75, 19, 225, 94, 107, 125, 138, 242, 31, 182, 150, 15, 24, 226, 29, 80, 116, 168, 118, 28, 1, 186, 220, 158, 79, 59, 244, 119, 9, 189, 161, 74, 130, 221, 56, 216, 241, 212, 26, 218, 170, 85, 165, 153, 69, 238, 93, 255, 142, 3, 159, 215, 67, 33, 249, 53, 176, 77, 254, 222, 25, 115, 101, 148, 16, 13, 237, 197, 5, 58, 157, 135, 248, 223, 61, 198, 211, 110, 44, 54, 111, 52, 227, 4, 46, 205, 7, 219, 136, 14, 87, 114, 64, 104, 50, 39, 203, 81, 196, 43, 163, 173, 109, 108, 187, 102, 195, 37, 235, 65, 190, 113, 149, 143, 8, 27, 155, 207, 134, 123, 224, 129, 245, 62, 66, 172, 122, 126, 12, 162, 214, 90, 247, 251, 124, 201, 236, 117, 183, 73, 95, 89, 246, 181, 179, 83, 228, 193, 99, 6, 45, 112, 32, 154, 128, 230, 131, 206, 243, 57, 84, 146, 0, 35, 96, 250, 137, 36, 208, 103, 34, 68, 204, 231, 144, 120, 98, 202, 49, 210, 23, 200, 18, 86, 55, 121, 20, 199, 97, 167, 180, 169, 106]
N = [20, 234, 159, 167, 230, 233, 58, 255, 158, 36, 210, 254, 133, 166, 59, 63, 209, 177, 184, 155, 85, 235, 94, 1, 242, 87, 228, 232, 191, 3, 69, 178]
O = [183, 174, 108, 16, 131, 159, 250, 5, 239, 110, 193, 202, 153, 137, 251, 176, 119, 150, 47, 204, 97, 237, 1, 71, 177, 42, 88, 218, 166, 82, 87, 94, 14, 195, 69, 127, 215, 240, 225, 197, 238, 142, 123, 44, 219, 50, 190, 29, 181, 186, 169, 98, 139, 185, 152, 13, 141, 76, 6, 157, 200, 132, 182, 49, 20, 116, 136, 43, 155, 194, 101, 231, 162, 242, 151, 213, 53, 60, 26, 134, 211, 56, 28, 223, 107, 161, 199, 15, 229, 61, 96, 41, 66, 158, 254, 21, 165, 253, 103, 89, 3, 168, 40, 246, 81, 95, 58, 31, 172, 78, 99, 45, 148, 187, 222, 124, 55, 203, 235, 64, 68, 149, 180, 35, 113, 207, 118, 111, 91, 38, 247, 214, 7, 212, 209, 189, 241, 18, 115, 173, 25, 236, 121, 249, 75, 57, 216, 10, 175, 112, 234, 164, 70, 206, 198, 255, 140, 230, 12, 32, 83, 46, 245, 0, 62, 227, 72, 191, 156, 138, 248, 114, 220, 90, 84, 170, 128, 19, 24, 122, 146, 80, 39, 37, 8, 34, 22, 11, 93, 130, 63, 154, 244, 160, 144, 79, 23, 133, 92, 54, 102, 210, 65, 67, 27, 196, 201, 106, 143, 52, 74, 100, 217, 179, 48, 233, 126, 117, 184, 226, 85, 171, 167, 86, 2, 147, 17, 135, 228, 252, 105, 30, 192, 129, 178, 120, 36, 145, 51, 163, 77, 205, 73, 4, 188, 125, 232, 33, 243, 109, 224, 104, 208, 221, 59, 9]
A = [204, 53, 135, 197, 39, 73, 58, 160, 79, 24, 12, 83, 180, 250, 101, 60, 206, 30, 10, 227, 36, 95, 161, 16, 135, 150, 235, 116, 242, 116, 165, 171]

def p(e, t, r):
    n = min(len(e) - t, len(r))
    for o in range(n):
        e[o + t] = e[o + t] ^ r[o]
def getSoundCryptLink(link):
    link = link.replace('_', '/').replace('-', '+')
    # padding
    link += '=' * (4 - len(link) % 4)
    # base64 decode
    link = base64.b64decode(link)
    r = []
    for i in range(len(link) - 16):
        r.append(link[i])
    n = []
    for i in range(16):
        n.append(link[len(link) - 16 + i])
    for i in range(len(r)):
        r[i] = O[r[i]] 
    for i in range(0, len(r), 16):  
        p(r, i, n) 
    for i in range(0, len(r), 32):  
        p(r, i, A)
    #utf8 to unicode
    link = bytes(r).decode('utf-8')
    return link



#getSoundCryptLink(l)

proxies = {
    # 'http': 'http://127.0.0.1:8888',
    # 'https': 'http://127.0.0.1:8888',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    "Referer": 'https://www.ximalaya.com/album/68117318'
}

'''
{
	"ret": 200,
	"data": {
		"uid": 514934198,
		"albumId": 68117318,
		"sort": 0,
		"pageNum": 10,
		"pageSize": 30,
		"tracksAudioPlay": [{
			"index": 271,
			"trackId": 563997335,
			"trackName": "《哈利·波特》第四部 第104集 第三个项目1",
			"trackUrl": "/sound/563997335",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 533,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 272,
			"trackId": 563997534,
			"trackName": "《哈利·波特》第四部 第105集 第三个项目2",
			"trackUrl": "/sound/563997534",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 750,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 273,
			"trackId": 563997689,
			"trackName": "《哈利·波特》第四部 第106集 第三个项目3",
			"trackUrl": "/sound/563997689",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 704,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 274,
			"trackId": 563997840,
			"trackName": "《哈利·波特》第四部 第107集 第三个项目4",
			"trackUrl": "/sound/563997840",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 686,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 275,
			"trackId": 563998014,
			"trackName": "《哈利·波特》第四部 第108集 第三个项目5",
			"trackUrl": "/sound/563998014",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 735,
			"updateTime": "2024-02",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 276,
			"trackId": 563998231,
			"trackName": "《哈利·波特》第四部 第109集 血，肉和骨头",
			"trackUrl": "/sound/563998231",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 896,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 277,
			"trackId": 563998538,
			"trackName": "《哈利·波特》第四部 第110集 食死徒1",
			"trackUrl": "/sound/563998538",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 1237,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 278,
			"trackId": 563998781,
			"trackName": "《哈利·波特》第四部 第111集 食死徒2",
			"trackUrl": "/sound/563998781",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 1164,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 279,
			"trackId": 563998927,
			"trackName": "《哈利·波特》第四部 第112集 闪回咒1",
			"trackUrl": "/sound/563998927",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 701,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 280,
			"trackId": 563999032,
			"trackName": "《哈利·波特》第四部 第113集 闪回咒2",
			"trackUrl": "/sound/563999032",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 590,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 281,
			"trackId": 563999255,
			"trackName": "《哈利·波特》第四部 第114集 吐真剂1",
			"trackUrl": "/sound/563999255",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 953,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 282,
			"trackId": 563999453,
			"trackName": "《哈利·波特》第四部 第115集 吐真剂2",
			"trackUrl": "/sound/563999453",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 799,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 283,
			"trackId": 563999771,
			"trackName": "《哈利·波特》第四部 第116集 吐真剂3",
			"trackUrl": "/sound/563999771",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 1191,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 284,
			"trackId": 563999974,
			"trackName": "《哈利·波特》第四部 第117集 分道扬镳1",
			"trackUrl": "/sound/563999974",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 907,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 285,
			"trackId": 564000126,
			"trackName": "《哈利·波特》第四部 第118集 分道扬镳2",
			"trackUrl": "/sound/564000126",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 691,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 286,
			"trackId": 564000326,
			"trackName": "《哈利·波特》第四部 第119集 分道扬镳3",
			"trackUrl": "/sound/564000326",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 855,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 287,
			"trackId": 564000507,
			"trackName": "《哈利·波特》第四部 第120集 分道扬镳4",
			"trackUrl": "/sound/564000507",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 750,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 288,
			"trackId": 564000689,
			"trackName": "《哈利·波特》第四部 第121集 开始1",
			"trackUrl": "/sound/564000689",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 829,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 289,
			"trackId": 564000979,
			"trackName": "《哈利·波特》第四部 第122集 开始2",
			"trackUrl": "/sound/564000979",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 912,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 290,
			"trackId": 564001236,
			"trackName": "《哈利·波特》第四部 第123集 开始3",
			"trackUrl": "/sound/564001236",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 860,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 291,
			"trackId": 577592546,
			"trackName": "《哈利·波特》第五部 第1集 达力遭遇摄魂怪1",
			"trackUrl": "/sound/577592546",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 688,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 292,
			"trackId": 577592671,
			"trackName": "《哈利·波特》第五部 第2集 达力遭遇摄魂怪2",
			"trackUrl": "/sound/577592671",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 696,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 293,
			"trackId": 577592771,
			"trackName": "《哈利·波特》第五部 第3集 达力遭遇摄魂怪3",
			"trackUrl": "/sound/577592771",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 695,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 294,
			"trackId": 577593188,
			"trackName": "《哈利·波特》第五部 第4集 达力遭遇摄魂怪4",
			"trackUrl": "/sound/577593188",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 667,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 295,
			"trackId": 577593382,
			"trackName": "《哈利·波特》第五部 第5集 一群猫头鹰1",
			"trackUrl": "/sound/577593382",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 640,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 296,
			"trackId": 577593536,
			"trackName": "《哈利·波特》第五部 第6集 一群猫头鹰2",
			"trackUrl": "/sound/577593536",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 588,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 297,
			"trackId": 577593677,
			"trackName": "《哈利·波特》第五部 第7集 一群猫头鹰3",
			"trackUrl": "/sound/577593677",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 634,
			"updateTime": "2024-03",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 298,
			"trackId": 577595010,
			"trackName": "《哈利·波特》第五部 第8集 一群猫头鹰4",
			"trackUrl": "/sound/577595010",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 605,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 299,
			"trackId": 577604975,
			"trackName": "《哈利·波特》第五部 第9集 一群猫头鹰5",
			"trackUrl": "/sound/577604975",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 606,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}, {
			"index": 300,
			"trackId": 577605089,
			"trackName": "《哈利·波特》第五部 第10集 先遣警卫1",
			"trackUrl": "/sound/577605089",
			"trackCoverPath": "storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg",
			"albumId": 68117318,
			"albumName": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
			"albumUrl": "/album/68117318",
			"anchorId": 332505348,
			"duration": 649,
			"updateTime": "2024-01",
			"createTime": "2022-10",
			"isLike": false,
			"isCopyright": true
		}],
		"hasMore": true,
		"albumRecordSort": 0
	}
}
'''
def getPlayList(id):
    trackList = []
    startPage = 1
    while True:
        playUrl = 'https://www.ximalaya.com/revision/play/v1/show?id={}&num={}&sort=0&size=30&ptype=0'.format(id, startPage)
        logging.info('getPlayList startPage: %d', startPage)
        response = requests.get(playUrl, cookies=cookies, proxies=proxies,headers=headers, verify=False)               
        for i in response.json()['data']['tracksAudioPlay']:
            trackList.append({
                'trackId': i['trackId'],
                'trackName': i['trackName'],
                'trackUrl': i['trackUrl'],
                'index': i['index'],
            })
        if response.json()['data']['hasMore']:
            startPage += 1
        else:
            break
    return trackList

'''
{
	"ret": 0,
	"trackInfo": {
		"trackId": 563981409,
		"title": "《哈利·波特》第四部 第72集 丽塔·斯基特的独家新闻1",
		"type": 0,
		"categoryId": 1001,
		"intro": "",
		"headSkip": 0,
		"tailSkip": 0,
		"paidType": 0,
		"processState": 2,
		"createdAt": 1664078400000,
		"coverSmall": "http://imagev2.xmcdn.com/storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg!op_type=3&columns=100&rows=100",
		"coverMiddle": "http://imagev2.xmcdn.com/storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg!op_type=3&columns=180&rows=180",
		"coverLarge": "http://imagev2.xmcdn.com/storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg!op_type=3&columns=1000&rows=1000",
		"videoCover": "",
		"uid": 332505348,
		"nickname": "哈利·波特官方账号",
		"isLike": false,
		"isPublic": true,
		"likes": 1303,
		"comments": 1126,
		"shares": 70,
		"userSource": 1,
		"status": 1,
		"duration": 483,
		"sampleDuration": 0,
		"isPaid": true,
		"isFree": false,
		"isAuthorized": true,
		"authorizedType": 1,
		"isVipFree": true,
		"isVideo": false,
		"isDraft": false,
		"isRichAudio": false,
		"isAntiLeech": true,
		"vipFirstStatus": 0,
		"ximiFirstStatus": 0,
		"hqNeedVip": true,
		"permissionSource": "105",
		"playUrlList": [{
			"huaweiSound": false,
			"type": "M4A_64",
			"fileSize": 3918645,
			"sampleSize": 800295,
			"url": "02RW7bzoFwkSI8qyNXbV45--aHpkNjRTXtdVLV7-fDoUGiQpY3DzoRIJk3eq3eWZ9xLSZWk4cHCi3fgUZ3u-uI6xGykfROIJKqaTLZ16eTCOIBA4-xxEXXV1BImdY8ZRF-JyAXjdmCuzVE7gp-X0Ib5_uJs5rFY8-tWIbpcQ91dMQDSSuguA2WYJL5hHZdWZZqSQLqvjEUJxRdCV5HMjniNkyZwfVmN-c_4DIlhIpTxZ5iCCL6xLxdcI3lGLgRm8_mgkcMZEUmb307IiKGXAQjQkCbNS4QESKSJiYbfC",
			"qualityLevel": 1,
			"uploadId": 28965191680,
			"width": 0,
			"height": 0,
			"version": 1
		}, {
			"huaweiSound": false,
			"type": "MP3_64",
			"fileSize": 3871390,
			"sampleSize": 737280,
			"url": "IyhXNGTfkiASI8qyNfYe5_7JDAG8IECnXtdVLV5ReQWzMGtwhOBEbRIJk3eqZbIeakW96hbMu8Ci3cAUZ0Es7TNeiXCjNykg61mT1sIAfCszpadKatbzXjwKBImlIjZKxuW63edq1DmkkU7gp5sarSskIS4DOf-iLurvyMGfSla3AfI7d_9wsrPmyxfVi4Qe7lAElyvi__ZxRdCV5CNEedMoThGjaJq6c_4DIlhVhGiBPZoVy9LSWNcI3lGL7Ccnt_RrKeA3BKb307IiKN3br_w-VyXNgQESKSJiYlNb",
			"qualityLevel": 1,
			"uploadId": 28965191680,
			"width": 0,
			"height": 0,
			"version": 1
		}, {
			"huaweiSound": false,
			"type": "M4A_24",
			"fileSize": 1498662,
			"sampleSize": 350396,
			"url": "chOIa-ftLmsSI8qyNXZbZ78lYmp3zqsBXtdVLV7-dhAsSiajTidhaRIJk3eq3cinRPpzgVKs-Vii3e9G70FgjiGsjaMvC_ZrV2qTXKV6V80hCsqEL4IzCHULBEBJlUUjYXL2n_Mop7yzVE7gp-WB6sXvP_VXQlkAGIcOdPgrMbNLsOo3abQlOiruQCIIZesotIj11j-Df49xRdCV5HNY9ScT5OAvEcGEc_4DIlhIjjXjHFGOHzgrwNcI3lGLezFv0F0mTmsLWGP307IiKGV6jQKqSuKrkAESKSJiYS2z",
			"qualityLevel": 0,
			"uploadId": 28965191680,
			"width": 0,
			"height": 0,
			"version": 1
		}, {
			"huaweiSound": false,
			"type": "MP3_32",
			"fileSize": 1935822,
			"sampleSize": 376832,
			"url": "RNc66JoIAlQSI8qyNfZfxVNLwlg2AMEbXtdVLV5RJPNd6rpTRXESQxIJk3eqZa0Tcic0j81Ip-2i3WfTl-wMk0-PzFMnempUI8OTmNsA7gBP5D7J1A0PRHXVBEBIxpme2g5r-iSL-VukkU7gp5tOCuGFmYJLSZaaMCaCbjK3nKBFl7G9vdu2cxJRQMTb3ct1JIWpCNdlhzhxRdCV5CPUILDXsf0n9quKc_4DIlhVIgtFBH0cT_hesNcI3lGLn5wdmnG6J1Z6dG_307IiKN0_qPV1kpx55AESKSJiYhHA",
			"qualityLevel": 0,
			"uploadId": 28965191680,
			"width": 0,
			"height": 0,
			"version": 1
		}],
		"childAlbumInWhiteList": false,
		"isEnjoying": false,
		"offlineVisibleType": 0,
		"permissionExpireTime": 1722182399000,
		"hasShqAuthorized": false,
		"isXimiUhqTrack": false,
		"isXimiUhqAuthorized": false,
		"playtimes": 432992
	},
	"albumInfo": {
		"albumId": 68117318,
		"title": "《哈利·波特》1-7部精品中文有声书全集| J.K.罗琳原著，光合积木演播",
		"coverLarge": "http://imagev2.xmcdn.com/storages/49fd-audiofreehighqps/4E/3D/GMCoOSUGYgOfAAuNoAFbSAX-.jpeg!op_type=3&columns=290&rows=290&magick=png",
		"saleScope": 0,
		"ageLevel": 0,
		"freeListenStatus": 0,
		"albumType": 0,
		"status": 1,
		"offlineType": 0,
		"isPaid": true,
		"isPodcastAlbum": false,
		"isAutoBuy": false
	},
	"version": 0,
	"hasAlbumRealFinished": true
}
'''
def getTrackInfo(id):
    trackUrl = 'https://www.ximalaya.com/mobile-playpage/track/v3/baseInfo/{}?device=www2&trackId={}&trackQualityLevel=1'.format(int(time.time() * 1000),id)
    response = requests.get(trackUrl,cookies=cookies, proxies=proxies,headers=headers, verify=False)
    return response.json()['trackInfo']

def downloadTrack(index, trackInfo):
    playUrl = trackInfo['playUrlList'][0]['url']
    trackName = trackInfo['title']
    decodeUrl = getSoundCryptLink(playUrl)
    logging.info('Downloading track: %d_%s %s' % (index,trackName, decodeUrl))
    response = requests.get(decodeUrl, cookies=cookies, proxies=proxies,headers=headers, verify=False)
    with open('{}_{}.m4a'.format(index, trackName), 'wb') as f:
        f.write(response.content)
    return trackName

# 点开一本书，url：https://www.ximalaya.com/album/68117318，后面的ID就是album
album = 68117318
#print(getTrackInfo(563981409))
# 先登录账号，然后在浏览器按f12获取cookie，填入下面的cookie中
# 带cookie 请求
cookies = {
    '_xmLog': '',
    'wfp': '',
    '1&remember_me': 'y',
    '1&_token': '',
    'web_login': '',
    'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '',
    'xm-page-viewid': '',
    'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070': '',
    'HMACCOUNT': '',
    'impl': '',
    'x_xmly_traffic': ''    
}
if __name__ == '__main__':
    # 设置log到文件中
    logging.basicConfig(level=logging.INFO, filename='ximalaya_{}.log'.format(time.time()), filemode='w', format='%(asctime)s - %(levelname)s: %(message)s')
    trackList = getPlayList(album)
    for track in trackList:
        # if track['index'] >= 250 or track['index'] < 73:
        #     continue
        logging.info('Downloading track: [%d]%s %d' % (track['index'], track['trackName'], track['trackId']))
        try:
            trackInfo = getTrackInfo(track['trackId'])
            downloadTrack(track['index'],trackInfo)
            logging.info('Download track success: [%d]%s %d' % (track['index'], track['trackName'], track['trackId']))
        except Exception as e:
            logging.error('Download track error: [%d]%s %d' % (track['index'], track['trackName'], track['trackId']))
            logging.error(e)
            continue