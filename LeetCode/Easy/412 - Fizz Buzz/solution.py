class Solution(object):
    def fizz_buzz(self, n):
        answer=[]
        for val in range(1,n+1):
            if val % 3 == 0 and val % 5 == 0:
                answer.append("FizzBuzz")
            elif val % 3 == 0:
                answer.append("Fizz")
            elif val % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(val))
        return answer

        # Why is this such a crappily formatted question lol