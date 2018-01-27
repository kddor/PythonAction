def StrReplace(str):
    if len(str)==0:
        return ""
    newstr=[]
    for i in str:
        if i ==" ":
            newstr.append("%20")
        else:
            newstr.append(i)
    return "".join(newstr)

if __name__ == '__main__':
    str="we are happy"
    newstr=StrReplace(str)
    print(newstr)


