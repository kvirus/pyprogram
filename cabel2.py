import itertools
def finding_closet(ls,target,depth):
    closest = []
    for i in itertools.combinations(ls, depth):

        if sum(i) == target:
            return i
        else:
            closest.append((abs(sum(i) - target), i))
    return min(closest)[1]

x = finding_closet([20,1,1,1,1,1,40,20,5,1,1,1,10,1],20,2)
b=0
print(x)
for i in x:
    b=b+i
print(b)

# g = 1
# while g < 8:
#     y = finding_closet([1,5,5,5,1,1,1,1],20,g)
#     print(y)
#     f = 0
#     for d in y:
#         f = f + d
#     print(f)
#     print('равно',y)
#     g=g+1