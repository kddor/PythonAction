# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        new_array=[]
        for i in array:
            if i%2==1:
                new_array.append(i)
        for j in array:
            if j%2==0:
                new_array.append(j)
        return new_array


if __name__ == '__main__':
    array = [1, 4, 3, 2, 5, 7]
    S=Solution()
    new_array=S.reOrderArray(array)
    print(new_array)
