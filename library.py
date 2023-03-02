#디렉터리 다루기
#os.path : 경로를 문자열로 다룸
#pathlib : 경로를 객체형으로 다룸, 파일찾기 & 시스템 경로 등 기능이 유용

import os
import pathlib

#현재 디렉토리 확인
print(os.getcwd())
print(pathlib.Path.cwd())

#경로 존재 확인
dir_file = r'C:\Users\admin\Desktop\Training\directory'
print(os.path.exists(dir_file))
print(os.path.exists(pathlib.Path(dir_file)))

#디렉토리 만들기
dir_os = r'C:\Users\admin\Desktop\Training\directory\os'
dir_pathlib = pathlib.Path(r'C:\Users\admin\Desktop\Training\directory\pathlib')

#os
if not os.path.exists(dir_os):
    os.makedirs(dir_os)

#pathlib
dir_pathlib.mkdir(parents=True, exist_ok=True)

#파일명 확인
dir_file = r'C:\Users\admin\Desktop\Training\directory'
print(os.listdir(dir_file))

print(os.listdir(dir_file)[0]) #os
print(pathlib.PurePath(os.listdir(dir_file)[0]).name) #pathlib

#상위 경로명 확인
print(dir_file)

print(os.path.dirname(dir_file)) #os
print(pathlib.PurePath(dir_file).parent) #pathlib

#경로 연결
#os
print(os.path.join(dir_file, 'os'))
print(os.path.join(os.path.dirname(dir_file), 'os')) #상위 경로에 연결

#pathlib
print(pathlib.PurePath(dir_file).joinpath('pathlib'))
print(pathlib.PurePath(dir_file).parent.joinpath('pathlib'))

#확장자 분리
file_path = os.path.basename(os.listdir(dir_file)[0])
print(file_path)

print(os.path.splitext(file_path)) #os
print(pathlib.PurePath(file_path).suffix) #pathlib

#리스트에서 확장자 제거
import re

fp = os.listdir(dir_file)
print(fp)

print([re.sub('.py', '', i) for i in fp])

#-------------------------------------------------------------------------------------------------------------------
#파일 읽기, 저장
#fileinput : 텍스트 파일을 읽고, 쓰고, 저장하는 기능을 더욱 편리하게 사용할 수 있게 해주는 라이브러리
#여러개의 파일을 읽어서 수정할 수 있음
#inpalce editing 기능을 사용하면 open, close보다 더 수정이 간편하고 직관적

import fileinput
import glob
import os

os.getcwd() #현재 경로 확인
os.listdir(os.getcwd()) #디렉토리 확인

dir_os = r'C:\Users\admin\Desktop\Training\directory\sample'

if not os.path.exists(dir_os):
    os.makedirs(dir_os) #디렉토리 생성

path = 'sample/'
print(glob.glob(os.path.join(path, "*.txt"))) #glob : 파일들의 리스트를 뽑을 때 사용

with fileinput.input(glob.glob(os.path.join(path, "*.txt"))) as f:
    for line in f:
        print(line) #파일 여러개 읽기

#첫번째 줄 수정
txt_files = glob.glob(os.path.join(path, "*.txt"))
print(txt_files)

with fileinput.input(txt_files, inplace=True) as f:
    for line in f:
        if f.isfirstline():
            print('첫번째 줄 입니다.', end='\n')
        else:
            print(line, end='')

#검색된 줄 수정
with fileinput.input(txt_files, inplace=True) as f:
    for line in f:
        if line=='첫번째 줄 입니다.\n':
            print('1번째 줄입니다.', end='\n')
        else:
            print(line, end='')

#키워드 포함 라인 수정
with fileinput.input(txt_files, inplace=True) as f:
    for line in f:
        if '14번째' in line:
            print('열네번째 줄 입니다.', end='\n')
        else:
            print(line, end='')

#텍스트 치환
with fileinput.input(txt_files, inplace=True) as f:
    for line in f:
        if '열네번째' in line:
            print(line.replace('열네번째', '14번째'), end='')
        else:
            print(line, end='')

#pickle : 파이썬에서 사용하는 딕셔너리, 리스트, 클래스 등의 자료형을 변환 없이 그대로 파일로 저장하고 이를 불러올 때 사용하는 모듈
import pickle

#객체형 파일 저장
list_data = ['A','B','C'] #리스트 형

with open('list.pkl', 'wb') as f: #파일 저장
    pickle.dump(list_data, f)
with open('list.pkl', 'rb') as f: #파일 읽기
    list_data2 = pickle.load(f)

print(type(list_data2))
print(list_data2)

dic_data = {}
dic_data[1] = {'no': 1, 'subject': '안녕 피클', 'content': '피클은 매우 간단합니다.'} #딕셔너리형

with open('dictionary.pkl', 'wb') as f: #파일 저장
    pickle.dump(dic_data, f)
with open('dictionary.pkl', 'rb') as f: #파일 읽기
    dic_data2 = pickle.load(f)

print(type(dic_data2))
print(dic_data2)

#-------------------------------------------------------------------------------------------------------------------
#파일 찾기, 복사, 이동
#glob : 패턴을 이용하여 파일을 검색할 때 사용하는 모듈

import glob
import os

os.getcwd() #현재 디렉토리 확인

for filename in glob.glob("*.py"):
    print(filename) #py 파일 찾기 - 현재 경로

for filename in glob.glob("**/*.txt"):
    print(filename) #txt 파일 찾기 - 하위 경로

for filename in glob.glob("**/*.txt", recursive = True):
    print(filename) #현재와 하위 경로 모두 포함

#파일명 글자수로 찾기
for filename in glob.glob("????.*", recursive=True):
    print(filename) #글자수 4

for filename in glob.glob("??????????.*", recursive=True):
    print(filename)

#문자열 포함 파일명 찾기
for filename in glob.glob("**/[a-z][a-z][a-z][a-z].*", recursive=True):
    print(filename)

for filename in glob.glob("**/새파일*.*", recursive=True):
    print(filename)

#fnmatch : glob과 동일하게 특정한 패턴을 따르는 파일명을 찾아주는 모듈
#파일명 매칭 여부를 True,False 형태로 반환하기 때문에 os.listdir() 함수와 함께 사용

import fnmatch
import os

#파일명이 '새'로 시작 & 확장자는 '.txt' & 확장자를 제외한 파일 길이는 4 & 파일명의 마지막 문자는 숫자
for filename in os.listdir('./sample'):
    if fnmatch.fnmatch(filename, '새??[0-9].txt'):
        print(filename)

#shutil : 파일을 복사하거나 이동할 때 사용하는 내장 모듈
#copy, copy2 : 파일 복사
#movw : 파일 이동, 확장자 변경

import shutil
shutil.copy("./sample/새파일1.txt", "./sample/새파일1_복사본.txt") #파일 복사하기
shutil.copy2("./sample/새파일1.txt", "./sample/새파일1_복사본_meta.txt") #메타데이터 복사하기

shutil.move("./sample/새파일1_복사본.txt", "./sample/새파일1_복사본.py") #확장자 바꾸기
shutil.move("./sample/새파일1_복사본.py", "./sample/새파일1_복사본.txt")

shutil.move("./sample/새파일1_복사본.txt", "새파일1_복사본.txt") #파일 이동하기 (sample -> 현재 디렉토리)
shutil.move("./sample/새파일1_복사본_meta.txt", "새파일1_복사본_meta.txt")

#-------------------------------------------------------------------------------------------------------------------
#파일 압축
#무손실 압축 : 데이터 손실이 전혀 없는 압축
#손실 압축 : 사람이 눈치채지 못할 수준의 정보만 버리고 압축하는 방법

#zlib : 데이터를 압축하거나 해제할 때 사용하는 모듈
import zlib
data = "Life is too short, You need python." * 10000 #대용량 문자열 데이터 (350,000 byte)
print(len(data))

compress_data = zlib.compress(data.encode(encoding='utf-8')) #유니코드로 인코딩 후 압축
print(len(compress_data))
print(compress_data)

print(f'zlib : {round(len(data) / len(compress_data),2)}') #압축률

org_data = zlib.decompress(compress_data).decode('utf-8')
print(len(org_data)) #압축 해제

#gzip : 파일을 압축하거나 해제할 때 사용하는 모듈
#내부적으로 zlib 알고리즘을 사용
import gzip
data = data = "Life is too short, You need python." * 10000 #대용량 문자열 데이터
with open('org_data.txt', 'w') as f:
    f.write(data) #원본 데이터 저장

with gzip.open('compressed.txt.gz','wb') as f:
    f.write(data.encode('utf-8')) #gzip 압축
with gzip.open('compressed.txt.gz', 'rb') as f:
    org_data = f.read().decode('utf-8') #gzip 압축 해제
print(org_data)

#zipfile : 여러개 파일을 zip 확장자로 합쳐서 압축할 때 사용하는 모듈
import zipfile
with zipfile.ZipFile('./sample/새파일.zip', 'w') as myzip:
    myzip.write('./sample/새파일1.txt')
    myzip.write('./sample/새파일2.txt')
    myzip.write('./sample/새파일3.txt') #파일 합치기

with zipfile.ZipFile('./sample/새파일.zip') as myzip:
    myzip.extractall() #압축 해제하기

#tarfile : tartfile은 여러개 파일을 tar 확장자로 합쳐서 압축할 때 사용하는 모듈
import tarfile

with tarfile.open('./sample/새파일.tar', 'w') as mytar:
    mytar.add('./sample/새파일1.txt')
    mytar.add('./sample/새파일2.txt')
    mytar.add('./sample/새파일3.txt')

with tarfile.open('./sample/새파일.tar') as mytar:
    mytar.extractall()