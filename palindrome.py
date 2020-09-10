#유효한 펠린드롬 예제
input_text = '1abc:ba1'

def check_palindrome(input_text)->bool:
    strs = []
    for char in input_text:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False    
    return True

print('check result = {0}'.format(check_palindrome(input_text)))

#pop()을 이렇게 사용할지 몰랐음...신기하네...
                