def subSetBt(c:list[int], k:int):
    p:list[int] = []
    subSetRec(c, len(c)-1, k, p)

def subSetRec(c, i, k, p):
    if k<0:
        return False
    if i == -1:
        if k==0:
            print(p)
            return True
        else:
            return False
    else:
        p.append(c[i])
        return subSetRec(c,i-1,k,p[0:len(p)-1]),subSetRec(c, i-1, k-c[i], p)
#podrian añadirse podas, lo dejo asi como esta en el codigo

subSetBt([4,5,9,3,6],9)