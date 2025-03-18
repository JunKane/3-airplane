import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

from nycflights13 import flights, planes
flights.info()
planes.info()

#주제 자유
#merge 사용해서 flights 와 plans 병합한 데이터로 
#각 데이터 변수 최소 하나씩 선택후 분석할 것
#날짜 시간 전처리 코드 들어갈것
#시각화 종류 최소 3개 
#배우지 않은 부분도 가능하다면 넣어도 됨


#flights 월, distance

sample = flights[['month','distance','tailnum','dep_delay','arr_delay']]
sample2 = planes[['tailnum','type','model']]
#두 데이터 프레임 합병
data=pd.merge(sample, sample2, how = 'inner')



#월별 비행거리 [12월이 제일 길고, 2월이 제일 짧다.]
pivoted_month=pd.pivot_table(data,
                  index='month',
                  values='distance').reset_index().sort_values(by='distance')
print(pivoted_month)


#상기 내용 그래프#
plt.figure(figsize=(10, 6))
sns.barplot(data=pivoted_month, x='month', y='distance', palette='viridis')

plt.title('Monthly Flight Distance ', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Distance', fontsize=12)
plt.xticks(rotation=45)

plt.yscale('log')
plt.show()




