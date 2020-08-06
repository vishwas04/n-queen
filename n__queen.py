n=int(input("n="))
count=1

def poss(lis):
    l = len(lis)
    res = []
    for i in range(0, n):
        res.append((i, l))
    zz = [(i, i) for i in range(1, n+1)]
    for i in lis:
        for j in zz:
            nw = (i[0] - j[0], i[1] - j[1])
            ws = (i[0] + j[0], i[1] - j[1])
            se = (i[0] + j[0], i[1] + j[1])
            en = (i[0] - j[0], i[1] + j[1])
            if nw in res:
                res.remove(nw)
            if ws in res:
                res.remove(ws)
            if se in res:
                res.remove(se)
            if en in res:
                res.remove(en)

        for k in res:
            if k[0] == i[0]:
                res.remove(k)
    return res
sol=[]
x=1
while 1:

    while len(poss(sol)) != 0 :
        sol.append(poss(sol)[0])


    if  len(sol) != n:
        temp=sol[-1]
        sol.remove(temp)

        while temp == poss(sol)[-1]:

            if len(sol) !=0:
                temp=sol[-1]
                sol.remove(temp)
            else:
                exit()

        ind = poss(sol).index(temp) + 1
        sol.append(poss(sol)[ind])

    if len(sol)==n:
        print("sol no.=",count)
        count=count+1
        a=[[' ' for i in range(0,n) ] for j in range (0,n)]
        for i in sol:
            a[i[0]][i[1]]='q'
        for i in a :
            print(i)
        print("\n\n\n")

        temp = sol[-1]
        sol.remove(temp)

        while temp == poss(sol)[-1] :
            if len(sol) != 0:
                temp = sol[-1]
                sol.remove(temp)

        ind = poss(sol).index(temp) + 1
        sol.append(poss(sol)[ind])
