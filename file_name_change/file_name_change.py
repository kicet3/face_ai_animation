import os
import sys
import urllib.request
import json

file_path="E:/AI/crawl/download/man/google"
file_names=os.listdir(file_path)

client_id="클라이언트 아이디" #네이버 파파고 api 사용
client_secret = "클라이언트 시크릿 키" 

for file_name in file_names:
	encText = urllib.parse.quote(str(file_name))
	data = "source=ko&target=en&text=" + encText
	url = "https://openapi.naver.com/v1/papago/n2mt"
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request, data=data.encode("utf-8"))
	rescode = response.getcode()
	if(rescode==200):
		response_body = json.loads(response.read())
		trans_text = response_body['message']['result']['translatedText']
		trans_text = re.sub(r"[^a-zA-Z0-9]","",trans_text)
	else:
		print("Error Code:" + rescode)
	i = 1
	Img_file_path = file_path+'/'+file_name
	Img_file_names = os.listdir(Img_file_path)
	for name in Img_file_names:
		src = os.path.join(Img_file_path,name)
		dst = str(Img_file_path)+"/"+str(trans_text)+" "+str(i)+".jpg"
		i+=1
		os.rename(src,dst)
		