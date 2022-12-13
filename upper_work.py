def UPPER(text)->str:
    '''function docstring'''
    temp = ''
    ALPHA = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    alpha =[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in text :
        if i in alpha :
            idx = 0
            for j in alpha :
                if i == j :
                    break
                idx+=1
            val = ALPHA[idx]
            temp+=val
            continue
        temp+=i
    return temp
print(UPPER(input('enter a text :')))
exit = input('enter any key to exit :')
