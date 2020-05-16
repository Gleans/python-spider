from DecryptLogin import login
from PIL import Image

lg = login.Login()

# '''定义验证码识别函数'''
# def crackvcFunc(imagepath):
#     # 打开验证码图片
#     img = Image.open(imagepath)
#     # 识别验证码图片
#     result = IdentifyAPI(img)
#     # 返回识别结果(知乎为数字验证码)
#     return result



infos_return, session = lg.weibo(17521300175, 'cfa1996..', 'mobile')


