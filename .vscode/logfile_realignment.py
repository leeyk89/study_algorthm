"""
1. 리스트 각각의 요소 앞 부분은 식별자이다.
2. 문자로그, 숫자로그 순으로 정렬한다.
3. 문자가 동일한 경우 식별자로 비교한다.
4. 숫자는 입력 순서 그래도 한다.
"""
logs = ["pro1 5 3 2 1,","dec3 t1 t2","pro2 3 4 2 1", "dec1 t4 t5"]

texts,digits = [],[] 
for log in logs :
    if log.split()[1].isdigit():
        digits.append(log)
    else :
        texts.append(log)

texts.sort(key=lambda x:(x.split()[1],x.split()[0]))

print(texts+digits)