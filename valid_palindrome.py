phrase = str(input("Enter your phrase: "))

def validPalindrome(phrase):
    phrase = phrase.lower()
    stack = []
    for i in phrase:
        if i.isalpha():
            stack.append(i)
    return stack

new = validPalindrome(phrase)
new1 = validPalindrome(phrase)
new1.reverse()

if new == new1:
    print("True")
else:
    print("False")


