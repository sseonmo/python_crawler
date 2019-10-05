#  w+ : 읽기 또는 쓰기, 파일이 없으면 생성
file = open('./hello.csv', 'w+')
file.write('hello'+'\n')
file.write('bye'+'\n')