#유효한 펠린드롬 예제
input_text1 = '1abc:ba11abc:ba11abc:ba11abc:ba11abc:ba11abc:ba1'
input_text2 = '1abc:ba11abc:ba11abc:ba11abc:ba11abc:ba11abc:ba1'
input_text3 = '1abc:ba11abc:ba11abc:ba11abc:ba11abc:ba11abc:ba1'


#list를 활용함
def checkPalindrome(input_text)->bool:
    strs = []
    for char in input_text:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.pop(0) != strs.pop():
            return False    
    return True

print('check result = {0}'.format(checkPalindrome(input_text1)))
#----------------------------------------------------------------------

import collections as cts
# #deque를 활용함
def isPalindrome(s:str)->bool:
    strs:Deque = cts.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False    
    return True

print('check result = {0}'.format(isPalindrome(input_text2)))
#리스트의 pop(0)는 O(n)인데 반해, 데크의 popleft()는 O(1)이기 때문에 각각을 n번 반복한다고 했을때
#리스트 구현 O(n2)/ 데크 O(n)이라는 큰 차이가 발생한다.

#----------------------------------------------------------------------

import re

def isPalindrome2(s:str)->bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s==s[::-1]

print('check result = {0}'.format(isPalindrome2(input_text3)))

#[::-1] 사용하면 문자가 역으로 뒤집힌다.