# Viết hàm trả về từ có độ dài lớn nhất trong chuỗi s. Với tham số truyền vào là chuỗi s. 
# Nếu có nhiều từ có độ dài bằng nhau thì trả về từ có thứ tự nhỏ hơn (sắp xếp theo bảng chữ cái).

def SoSanhTu(s):
    s = sorted(s.split(),key= len)
    print(s)
    return s[-1]

print(SoSanhTu('Kteam --xin-- chao'))
