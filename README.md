# ximalaya
一个批量下载指定专辑下的所有音频文件的工具
## 使用方法
- 专辑ID -> 图片中的26343345
  ![图片](https://github.com/user-attachments/assets/23b0a9a3-5c38-4da3-90ea-3a8df3ffa915)
- 获取Cookie
  先登录网站，然后按f12弹出开发者窗口，操作如图
  ![图片](https://github.com/user-attachments/assets/6e173b2d-ace3-4e27-af51-621ff8131a3c)
- 替换掉代码里的album和cookies
```python
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
```
- 运行main.py,会在当前目录下保存音频文件
