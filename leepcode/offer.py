class Solution:
    def replaceSpace(self, s1):
        m=[]
        for i in s1:
            if i!=" ":
                m.append(i)
            else:
                m.append('%20')
        return "".join(m)

if __name__ == "__main__":
    print(Solution().replaceSpace("we are happy"))