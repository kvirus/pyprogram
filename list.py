buht = {'1':100,'2':200,'3':300} #Вводим количество бухт и остатки метража
print(buht)
buht1 ={}
cut =[20,90,6,8,2,12,20,40,10,50,14,65,30,90] #Количество нужных кусоков
#buht1 = buht['1'] -50 - 20
print(cut)
i=0
for cuts in cut:
    if buht['1'] >= cuts:
        buht['1'] = buht['1'] - cuts
        print("куски в первой бухте:", cuts,cut)
    else:
        continue
    cut[i] = 0
    i = i + 1
print('остаток в бухте',buht['1'])
print('остаток после первой бухты', cut)

b=0
for i in cut:
    if buht['2'] >= i:
        buht['2'] = buht['2'] - i
        if i!=0:
            print("куски во второй бухте:", i)
        cut[b] = 0
        b = b + 1
    else:
        continue
print('остаток в бухте',buht['2'])
print('остаток после второй бухты',cut)

c=0
for cuts in cut:
    if buht['3'] >= cuts:
        buht['3'] = buht['3'] - cuts
        if cuts != 0:
            print("куски в тетей бухте:", cuts)
        cut[c] = 0
        c = c + 1
    else:
        continue
print('остаток в бухте',buht['3'])
print('остаток после третей бухты',cut)