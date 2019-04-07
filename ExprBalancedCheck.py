def balanced_check(expr):
    stack = []
    if len(expr)%2 != 0:
        return False
    if(len(expr) ) == 0:
        return False
    else:
        openParen = [ '(','[','{' ]
        matchingPair = [('{','}'),('(',')'),('[',']')]
        for paren in expr:
            if paren in openParen:
                stack.append(paren)
            else:
                open = stack.pop()
                if (open,paren) not in matchingPair:
                    return False
        return True

print("False conditions :")
print(balanced_check(']'))
print(balanced_check('([)'))
print(balanced_check('([{})'))
print(balanced_check(''))

print("True conditions :")
print(balanced_check('[]'))
print(balanced_check('()'))
print(balanced_check('[]'))
print(balanced_check('{}'))
print(balanced_check('([{}])'))
