class aliendict:
    def __init__(self):
        self.dict = set()

    def add_word(self, word):
        self.dict.add(word)

    def can_segment(self, s):
        # length of the string
        n = len(s)

        # initialise the dp array

        dp = [False] * (n + 1)
        dp[0] = True  # base case

        #loop to fill the dp array
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in self.dict:
                    dp[i] = True
                    break
        
        return dp[n]

#reading input
if __name__ == "__main__":
    s = input("enter the string: ").strip()  # string from john
    n = int(input("enter the no of words in the dict: ").strip()) #no of words in the dictionary

# create an alien dictionary obj
aldict = aliendict()

#read and add words to the dictionary
for _ in range(n):
    word = input("add words to the dictionary: ").strip()
    aldict.add_word(word)

# check if the string can be segmented
result = aldict.can_segment(s)

if result:
    print("true")
else:
    print("false")
