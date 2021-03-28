# Viết hàm truyền vào tham số là chuỗi s. Trả về chuỗi s sau khi được xóa các khoảng trắng thừa.
def TachKhoang(s):
    s = s.strip()
    lst = ''
    for i in range(len(s)):
        if s[i]!=' ':
            lst += str(s[i])
        if s[i-1]!=' ' and s[i]==' ':
            lst += str(s[i])

    print(lst)

TachKhoang(' *    * Kteam _   _')