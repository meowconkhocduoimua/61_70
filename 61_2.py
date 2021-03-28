# Ý tưởng là xóa 2 khoảng trắng thành 1 khoảng trắng

def XoaKhoang(s):
    s = s.strip()
    while "  " in s:
        s = s.replace('  ',' ')
    print(s)

XoaKhoang('*    * Kteam _   _')

