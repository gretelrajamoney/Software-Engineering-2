# creates a class called palidrome
class palindrome:
    # creates an empty constructor
    def __init__(self):
        pass
    
    # creates the palindrome checker function
    def palidromecheck(self, input):
        for x in range(0, int(len(input)/2)):
            if input[x] == input[len(input) - x - 1]:
                return True
            else:
                return False
 

    
# take in the users palidrome input
# input = str(input("pls enter your word & I will tell you if it is a palidrome: "))

# result = palidromecheck(input)
    
# if result:
    # print("your word is a palindrome")
# else:
    # print("your word is not a palindrome")

