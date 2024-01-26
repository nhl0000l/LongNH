strs = str(input())

def validParentheses(strs):
    stack = []
    pairs = {"(":")",
            "{":"}",
            "[":"]"
    }
    for i in strs:
        if i in pairs:
            stack.append(i)
        elif len(stack) == 0 or i != pairs[stack.pop()]:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

print(validParentheses(strs))



