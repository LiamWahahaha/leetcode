class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mod_3 = 'Fizz'
        mod_5 = 'Buzz'
        ret = []

        for i in range(1, n+1):
            fizz = mod_3 if i % 3 == 0 else ''
            buzz = mod_5 if i % 5 == 0 else ''
            ret.append((lambda x, y: x if y == '' else y)(str(i), fizz+buzz))

        return ret

def main():
    test = Solution()
    print(test.fizzBuzz(15))

if __name__ == '__main__':
    main()
