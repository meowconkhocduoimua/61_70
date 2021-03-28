# Hàm trả về số lượng ký tự nguyên âm và chuỗi s với các ký tự nguyên âm thay thế bằng ký tự "$".

def NguyenAm(s):
    SoLuong = 0
    for i in ['u','e','o','a','i','U','E','O','A','I']:
        SoLuong += s.count(i)
        s = s.replace(i,'$')
    return SoLuong,s

print(NguyenAm('Xin chao KTEAM'))
