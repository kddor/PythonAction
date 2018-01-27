# coding=utf-8
#author:liuyong
#date:20171207

import random
#将list或set转化为字符串
def list_to_str(L):
    return "".join(L)

# 给定字符串s，剔除字符串中的重复字符
def str_del_dupl(s):
    #s='liuyongadsall'
    if len(s)<2:
        return s
    return list_to_str(set(s)) #利用set进行去重

# 给定字符串s，快速排序
def quick_sort(s):
    L=list(s)
    if len(L) < 2:
        return L
    rand_s = random.choice(L)
    small = [i for i in L if i < rand_s]
    large = [i for i in L if i > rand_s]
    return quick_sort(small)+ [rand_s] + quick_sort(large)

#给定字符串输入，输出去重排序后的字符串及长度
def str_output(input_s,input_len):
    output_str=list_to_str(quick_sort(str_del_dupl(input_s)))
    return output_str

if __name__ == '__main__':
    input_s= 'liuyonghuaweihua'
    input_len=len(input_s)
    print("原始的字符串：",input_s)
    print("输出去重后幷排序的字符串：",str_output(input_s,input_len))