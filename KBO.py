from bs4 import BeautifulSoup 
import requests
import pandas as pd


url = "https://www.koreabaseball.com/History/Crowd/GraphDaily.aspx" # url
result = requests.get(url) #url request 받기
bs_obj = BeautifulSoup(result.content, "html.parser") # html 읽기

tdata = bs_obj.find("table", {"class":"tData"}) # html파일의 tData 클래스의 이름의 table 태그의
series = tdata.find("tbody") # tbody 태그를
kbdata_spec = series.text  # 읽어서 kbdata_spec에 할당

def to_int(raw):
    kbdata_spec = raw.split("(")[0].replace('\n','').replace(',','')
    return int(kbdata_spec)

print(kbdata_spec)