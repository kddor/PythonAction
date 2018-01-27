'''
题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递
增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含
有该整数。
'''

def listfound(list,target):
    isfound=False
    #选取右上角的数字
    row = 0
    col = len(list[0]) - 1
    while(col>=0 and row<=len(list)-1):
        #如果目标值等于右上角数字，则返回true
        if target==list[row][col]:
            isfound=True
            print("找到了")
            break
        #如果目标值<该数字，则表明目标值在左下角，列-1
        elif target<list[row][col]:
            col-=1
        #目标值>该数字，则剔除该行，行+1
        else:
            row+=1
    return isfound

if __name__ == '__main__':
    list=[[1,2,3],
      [4,5,6],
      [7,8,9],
      [10,11,12]]

found=listfound(list,0)
print(found)


