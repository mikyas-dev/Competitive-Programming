class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lists = []
        for x in range(1,n+1):
            if x%15 == 0:
                lists.append("FizzBuzz")
            elif x%5 == 0:
                lists.append("Buzz")
            elif x%3 == 0:
                lists.append("Fizz")
            else:
                lists.append(str(x))
        return lists
