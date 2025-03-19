import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#flights 데이터 
from nycflights13 import flights, planes, weather

# 같은 기상 상황에 따라 비행기 지연시간 비교 temp, dep_delay, arr_delay
# 비행기 기종에 따라 다른 점 찾기 (최신인지, 엔진, 노선별)

## 1. 바람 세기, 출발 지연시간 비교
tem = weather[['time_hour','wind_speed']]
pt = flights[['time_hour','dep_delay']]

# 두 데이터프레임을 time_hour을 기준으로 병합
tempt = pd.merge(tem,pt,how = 'inner')

#데이터프레임의 인덱스를 초기화하여 기본 인덱스로
teempt = tempt.reset_index()

#동일한 바람세기 기준으로 데이터를 묶어 출발지연시간의 평균 
grouped = tempt.groupby('wind_speed')['dep_delay'].mean()

#그룹화 없이 그리기
plt.scatter(x = teempt['wind_speed'],y =teempt['dep_delay'])

#바람세기 구간 설정
bins = np.arange(0, teempt['wind_speed'].max() + 5, 5)

#구간화
teempt['wind_bin'] = pd.cut(teempt['wind_speed'], bins=bins, right=False)

teempt["wind_category"] = pd.cut(teempt['wind_speed'], bins=[0, 5, 10, 15, 20, 30, 50], 
                             labels=["0-5", "5-10", "10-15", "15-20", "20-30", "30+"])

#구간 지정 기준으로 그룹화
grouped = teempt.groupby('wind_bin')['dep_delay'].mean()

#데이터프레임으로 변환
df_grouped = grouped.to_frame().reset_index()

# 열 이름 지정
df_grouped.columns = ['wind_bin', 'dep_delay']  

# 구간을 문자열로 변환
df_grouped['wind_bin_str'] = df_grouped['wind_bin'].astype(str)

# 막대그래프 그리기 (Matplotlib)
plt.bar(df_grouped['wind_bin_str'], df_grouped['dep_delay'])
plt.xlabel("Wind Bin (String)")
plt.ylabel("Dep Delay")
plt.title("Wind Bin vs Dep Delay")
plt.xticks(rotation=45)  # 라벨이 겹치지 않도록 회전
plt.tight_layout()
plt.show()



## 2. 바람 세기, 도착 지연시간 비교
arr = weather[['time_hour','wind_speed']]
ival = flights[['time_hour','arr_delay']]

# 두 데이터프레임을 time_hour을 기준으로 병합
arrival = pd.merge(arr,ival,how = 'inner')

#데이터프레임의 인덱스를 초기화하여 기본 인덱스로
arival = arrival.reset_index()

#동일한 바람세기 기준으로 데이터를 묶어 도착착지연시간의 평균 
arv = arival.groupby('wind_speed')['arr_delay'].mean()

#데이터프레임으로 변환
aarv =arv.to_frame().reset_index()

#바람세기 구간 설정
bins = np.arange(0, aarv['wind_speed'].max() + 5, 5)

#구간화
aarv['wind_bin'] = pd.cut(aarv['wind_speed'], bins=bins, right=False)

#구간 지정 기준으로 그룹화
arvgroup = aarv.groupby('wind_bin')['arr_delay'].mean()

#데이터프레임으로 변환
arvgroup = arvgroup.to_frame().reset_index()

# 열 이름 지정
arvgroup.columns = ['wind_bin', 'arr_delay'] 

# 구간을 문자열로 변환
arvgroup['wind_bin_str'] = arvgroup['wind_bin'].astype(str)

# 막대그래프 그리기 (Matplotlib)
plt.bar(arvgroup['wind_bin_str'],arvgroup['arr_delay'], color='skyblue', alpha=0.7, edgecolor='black')
plt.xlabel("Wind Bin (String)")
plt.ylabel("Arr Delay")
plt.title("Wind Bin vs Arr Delay")
plt.xticks(rotation=45)  # 라벨이 겹치지 않도록 회전
plt.tight_layout()
plt.show()

#막대 두개 합치기

import numpy as np
import matplotlib.pyplot as plt

labels = df_grouped['wind_bin_str']          # x축 라벨
val1 = df_grouped['dep_delay']
val2 = arvgroup['arr_delay']

x = np.arange(len(labels))    # x축 좌표
width = 0.4                   # 막대 너비

plt.bar(x - width/2, val1, width=width, label='dep_delay')
plt.bar(x + width/2, val2, width=width, label='arr_delay')

plt.xticks(x, labels,rotation = 45)         # x축 위치에 labels 표시
plt.legend()
plt.tight_layout()
plt.show()


# 바람세기는 하루 총 평균 바람세기인가?
# 바람세기가 30~ 35일때 도착지연과 출발지연이 가장 높게 나타나고
# 오히려 35를 넘으면 적게 나타나는 걸로 보여 지연이 되다못해 결항되는 것으로 예측됩니다.
# 바람세기가 0에서 25까지 출발 지연은 큰 차이가 없는 것으로 보이며 