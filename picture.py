from etool import ManagerQrcode

qr_path = 'qr.png' # 保存路径
ManagerQrcode.generate_english_qrcode(words="http://litterbear.fun/app/", save_path=qr_path) # 生成
