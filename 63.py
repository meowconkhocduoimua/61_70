# Viết hàm truyền vào tham số là chuỗi s. Nối các từ của chuỗi s bằng dấu "-" và trả về kết quả cho hàm.

def NoiKhoang(s):
    s = "-".join(s.split())
    print(s)

NoiKhoang('*    * Kteam _   _')