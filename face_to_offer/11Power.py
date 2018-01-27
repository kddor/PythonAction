class Solution:
    def Power(self, base, exponent):
        m=1.0
        if exponent==0:
            return 1.0
        elif exponent > 0:
            for i in range(1,exponent+1):
                m=base*m
            return m
        else:
            for i in range(1,-exponent+1):
                m=base*m
            return 1.0/m

if __name__ == '__main__':
    S=Solution()
    #print(m)
    print(S.Power(3,-2))

