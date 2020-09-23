import collections as ct
#애나그램이란 문자열 재배치로 다른 의미로 변할 수 있는 것을 말한다.
input_text = ["eat","tea","tan","ate","nat","bat"]
#일단 문자열 순서에 상관없이 같은 알파벳이 구성된지 판단하면된다.
anagrams = ct.defaultdict(list)
#key 값이 선언되어 있지 않은 상태에서 append를 실행하면 keyerror가 발생한다.
#이를 방지하기 위해 collections.defaultdict(list)를 선언 후 진행한다.
for word in input_text:
    anagrams[''.join(sorted(word))].append(word)
    print(anagrams)

#word를 sorting 해야한다는 것은 알았지만 dictionaly에 넣어서 풀 수 있다는건 몰랐다.
#단순하게 조건문으로 비교 후 새로운 list에 append할 생각이였는데... 생각해보면 많아지면 기하급수적으로 시간이 걸릴 것 같다.
