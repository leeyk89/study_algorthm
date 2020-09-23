import collections as clt
import re
input_text =  'my heart hit, Hello world and fill so Good, my life is good, good-bey'
banned = ['good']
words = [word for word in re.sub(r'[^\w]',' ',input_text).lower().split() if word not in banned]
counts = clt.Counter(words)
print(counts)
#most_common 가장 흔한 단어를 추출하는 함수
print(counts.most_common(1)[0][0])