def SoSanhTu(s):
    TuDaiNhat = ''
    for i in s.split():
        if len(TuDaiNhat) < len(i) or (len(TuDaiNhat) == len(i) and i< TuDaiNhat):
            TuDaiNhat = i
    return TuDaiNhat
    

print(SoSanhTu('Kteam --xin-- chaooo'))
