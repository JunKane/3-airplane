# 주제 자유:
#merge 사용해서 flights와 planes 병합한 데이터로
# 각 데이터 변수 최소 하나씩 선택 후 분석할 것
# 날짜 &시간 전처리 코드 들어갈것
#시각화 종류 최소 3개
# 그래프 해석
# 기종별 지연시간간
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nycflights13 import flights, planes
flights.keys()
planes.keys()
planes['year'].unique()

# 기종 별 출발 시간대 별
# 도착 지연시간 출발 지연시간 날짜 전처리

pd.merge()

#스피드 못쓰는값
# tail num merge inner
# 시간, 문자열  전처리는 weekday date

# 비행기 기종 별 시간대별(시간정보 추출) 지연시간 (출발 도착)
# 엔진모델 별 비행거리
# 엔진 개수 별 비행거리
# 월별 비행거리  
flights.head()

flights['weekday'] = flights['date'].dt.day_name()
flights['date'] = pd.to_datetime(flights[['year', 'month', 'day']])

# 엔진개수별 이동거리

flights.keys()
planes.keys()
temp = flights[['tailnum','distance','air_time']]
temp2 = planes[['tailnum','engines','seats']]
merged1 = pd.merge(temp, temp2, how = 'inner')
engdistance = merged1.groupby('engines')['distance'].mean(numeric_only=True).reset_index()
engine1 = engdistance.iloc[:,0]
distance1 = engdistance.iloc[:,1]
plt.bar(engine1, distance1)

# 엔진 1개 2개가 비행거리가 많음 --> 엔진을 적게 사용하는 것이 연료 효율이 높기 때문
# 그럼 1개 2개짜리가 연료 효율이 높은지 확인해보자!
# 연료 효율성 직접적인 연비계산 불가
# 대체 지표: 비행속도, 기체 제작 연도
# 비행 속도가 높을수록 연료가 많이 소모될거라고 생각
# 비행 속도 계산 거리 / 비행시간
# 옛날에 제작된 기체일수록 연료 효율 많이 떨어질 것이라 생각
# 1개 2개인 비행기가 최신 기체가 많은지 확인


# 엔진개수 별 속력
merged1['pspeed'] = merged1['distance']/merged1['air_time']
engspeed = merged1.groupby('engines')['pspeed'].mean(numeric_only=True).reset_index()
engine2 = engspeed.iloc[:,0]
distance2 = engspeed.iloc[:,1]
plt.bar(engine2, distance2)


# 상관계수
flights.keys()
planes['type'].unique()
temp = flights[['tailnum','distance','dep_delay','arr_delay','time_hour']]
temp2 = planes[['tailnum','engines','seats','model','year']]
merged2 = pd.merge(temp, temp2, how = 'inner')