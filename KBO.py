from bs4 import BeautifulSoup 
import requests
import pandas as pd


url = "https://www.koreabaseball.com/History/Crowd/GraphDaily.aspx" # url
result = requests.get(url) #url request 받기
bs_obj = BeautifulSoup(result.content, "html.parser") # html 읽기

tdata = bs_obj.find("table", {"class":"tData"}) # html파일의 tData 클래스의 이름의 table 태그의
series = tdata.find("tbody") # tbody 태그를
kbdata_spec = series.text  # 읽어서 kbdata_spec에 할당

# 하지만, 위의 데이터는 데이터 프레임의 형태가 아니므로 데이터 형태로 바꿔준다

""" kbdata_spec_df = pd.DataFrame(list(kbdata_spec.items()), columns=['날짜','요일','홈','방문','구장','관중수'])
print(kbdata_spec_df) """