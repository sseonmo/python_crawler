import requests

# Home > SKINCARE > CleansersFace > Wash
# url = 'http://jolse.com/category/face-wash/1011/'
url = "http://jolse.com/category/wash/56/"

result = requests.get(url)
print(result)       # 403 권한없음.. 젠장
