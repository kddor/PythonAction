
#@param:n 鸡蛋个数
#@param:k 楼层数
def eggDroppingRecursion(n,k):
    #如果楼层数为0或者1，则返回k值
    if k==0 or k==1:
        return k
    #如果鸡蛋个数为1，则返回k值
    if n==1:
        return k

    min = 65535
    res = 0

    #考虑从第一层到第k层扔下鸡蛋的所有情况的最小结果
    for i in range(1,k+1):
        res=max(eggDroppingRecursion(n-1,i-1),eggDroppingRecursion(n,k-i))
        if (res<min):
            min=res
    return min+1


if __name__ == '__main__':
    print(eggDroppingRecursion(2,10))
