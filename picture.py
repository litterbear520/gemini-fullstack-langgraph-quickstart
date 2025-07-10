from etool import ManagerQrcode

qr_path = 'qr3.png' # 保存路径
ManagerQrcode.generate_english_qrcode(words="https://litterbear520.github.io/Blog/bloglist", save_path=qr_path) # 生成
