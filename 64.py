# Viết hàm xóa các ký tự trùng lặp trong chuỗi. Với tham số truyền vào là chuỗi s.

def XoaLap(s):
    s_xoa =''
    for i in s:
        if s_xoa.count(i)==0:
            s_xoa += i 
    return s_xoa

print(XoaLap('Xin chao Kteam'))