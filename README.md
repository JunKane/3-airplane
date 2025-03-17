# 3-airplane

import pandas as pd
import numpy as np


#flights 데이터 
from nycflights13 import flights,planes
flights.info()
flights
planes.info()
planes

# 주제 자유
# merge 사용해서 flights 와 planes 병합한 데이터로
# 각 데이터 변수 최소 하나씩 선택 후 분석할 것.
# 날짜 시간 전처리 코드 들어갈 것 -> time_hour 사용
# 문자열 전처리 코드 들어갈 것 
# 시각화 종류 최소 3가지 (배우지 않은 것도 할 수 있으면 넣어도 됨)
 
#엔진 개수별 비행거리 
import pandas as pd
import numpy as np

temp = flights[['tailnum','distance','time_hour']]
temp2 = planes[['tailnum','model','seats','manufacturer']]


flight = pd.merge(temp, temp2, how = 'inner')
flight
#엔진 모델별로  비행거리가 어떻게 달라지나 
import seaborn as sns
import matplotlib.pyplot as plt
x= flight['manufacturer']
y =flight['time_hour']

plt.bar(x,y)
plt.plot(x,y,'ro')

import seaborn as sns
import matplotlib.pyplot as plt
# 상자그림(Box Plot) 그리기
plt.figure(figsize=(8,5))
sns.boxplot(x= flight['engines'], 
            y =flight['distance'], 
            palette="Pastel1")
plt.xlabel("engines")
plt.ylabel("distance")
plt.title("boxplot")
plt.xticks(rotation=30)
plt.show()

#엔진모델별 비행거리 비교
import seaborn as sns
import matplotlib.pyplot as plt

flight.sort_values(by='distance',ascending=True)

plt.plot()

flight.groupby('distance')['model']

p=flight.groupby(['distance','model']).size().reset_index(name='count')

sns.barplot(x='distance', y='count', hue='model', data=p)
plt.xlabel("비행거리")
plt.ylabel("항공편 건수")
plt.title("엔진 모델별 비행거리 분포")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
# 상자그림(Box Plot) 그리기
plt.figure(figsize=(6,5))
plt.scatter(x=flight['seats'],
y=flight['distance'])
seatdistance = flight.groupby('seats')['distance'].mean(numeric_only=True).reset_index()
seatdistance

plt.plot(flight['seats'],flight['seats'],'r--', flight['distance'],flight['distance'],'g')

plt.plot(seatdistance['seats'],flight['distance'],'r--')

flights
planes
temp = flights[['tailnum','distance']]
temp2 = planes[['tailnum','engines']]
merged1 = pd.merge(temp, temp2, how = 'inner')
engdistance = merged1.groupby('engines')['distance'].mean(numeric_only=True).reset_index()
engdistance
engine1 = engdistance.iloc[:,0]
distance1 = engdistance.iloc[:,1]
plt.bar(engine1, distance1)


import seaborn as sns
import matplotlib.pyplot as plt
# 상관행렬 계산
flight
corr_matrix = flight[['distance','seats']].corr()
corr_matrix
corr_matrix = flight[['']]

# 히트맵 그리기
plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()

flights
planes

temp = flights[['tailnum','distance','time_hour']]
temp2 = planes[['tailnum','model','seats','year','engines','speed']]

flight = pd.merge(temp, temp2, how = 'inner')

corr_matrix = flight[['engines','distance']].corr()
corr_matrix

