from libs5.naver_api_caller import get1000Resutl
import json

# for num in range(1, 202, 100):
#     print(caller.call('강남역 맛집', num))

#  1
list = []
result = get1000Resutl("강남역 맛집")
result2 = get1000Resutl("강남역 찻집")
list += result + result2
print(len(list))

# 파일저장 / w+ = 읽기 또는 쓰기 모드, 파일이 없으면 새로만든다.
file = open('./gangnam.json', "w+")
file.write(json.dumps(list))

# 2
# list2 = []
# for li in map(get1000Resutl, ['강남역 맛집', '강남역 찻집']):
#     list2 += li
#
# print(len(list2))
