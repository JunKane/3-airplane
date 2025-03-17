import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

from nycflights13 import flights, planes
flights.info()
planes.info()

planes.describe()
planes['speed'].describe()
planes['type'].unique()

# 비행기 기종 별 시간대별(시간정보 추출) 지연시간 (출발 도착)
# 엔진모델 별 비행거리
# 엔진 개수 별 비행거리


# 월별 비행거리 [x]

temp = flights[['tailnum','dep_delay','arr_delay']]
temp2 = planes[['tailnum','type','model']]
pd.merge(temp, temp2, how = 'inner')




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





#기종별 비행거리

pivoted_model=pd.pivot_table(data,
                  index=['model','tailnum'],   
                  values='distance').reset_index()
print(pivoted_model)


plt.figure(figsize=(12, 6))
sns.barplot(data=pivoted_model, x="model", y="distance", hue="tailnum", dodge=True, palette="Blues")

plt.title("Flight Distance by Model and Tail Number", fontsize=14)
plt.xlabel("Aircraft Model", fontsize=12)
plt.ylabel("Distance", fontsize=12)
plt.xticks(rotation=45)

plt.legend(title="Tail Number", bbox_to_anchor=(1, 1), loc="upper left")  # 범례 조정
plt.show()


#주제 자유
#merge 사용해서 flights 와 plans 병합한 데이터로 
#각 데이터 변수 최소 하나씩 선택후 분석할 것
#날짜 시간 전처리 코드 들어갈것
#시각화 종류 최소 3개 
#배우지 않은 부분도 가능하다면 넣어도 됨


sample = flights[['month','distance','tailnum','dep_delay','arr_delay']]
sample2 = planes[['tailnum','type','model']]
#두 데이터 프레임 합병
data=pd.merge(sample, sample2, how = 'inner')





#flights 히트맵
int_flights=flights.select_dtypes(include=['float64', 'int64'])
int_flights.corr()



# 
plt.figure(figsize=(10,8))
sns.heatmap(int_flights.corr(), 
            annot=True, #히트맵 사각형에 계수값 포함 한다는 의미
            cmap="coolwarm",
            fmt=".2f",linewidths=0.5)
            # " .2f"소수점 2자리까지

plt.title("Heatmap of Feature merged")       
plt.show()



#planes 히트맵
int_planes=planes.select_dtypes(include=['float64', 'int64'])
int_planes.corr()



# 
plt.figure(figsize=(6,5))
sns.heatmap(int_planes.corr(), 
            annot=True, #히트맵 사각형에 계수값 포함 한다는 의미
            cmap="coolwarm",
            fmt=".2f",linewidths=0.5)
            # " .2f"소수점 2자리까지
plt.title("Heatmap of Feature merged")       
plt.show()



pd.factorize(data)


data.info()

int_data=data.select_dtypes(include=['float64', 'int64'])
int_data.corr()

data.shape


# 히트맵 그리기
plt.figure(figsize=(20,12))
sns.heatmap(int_data.corr().corr(), 
            annot=True, #히트맵 사각형에 계수값 포함 한다는 의미
            cmap="coolwarm",
            fmt=".2f",linewidths=0.5)
            # " .2f"소수점 2자리까지
plt.title("Heatmap of Feature merged")       
plt.show()


# object 타입 컬럼 선택
object_columns = data.select_dtypes(include=['object']).columns

for col in object_columns:
    try:
        data[col] = pd.to_numeric(data[col], errors='coerce')  # 숫자로 변환 시도
        if data[col].isna().any():  # NaN이 존재하면 문자열 값이 있었음
            unique_sorted_values = sorted(data[col].dropna().unique())  # 정렬된 유니크 값
            mapping = {val: idx for idx, val in enumerate(unique_sorted_values)}  # 매핑 생성
            data[col] = data[col].map(mapping)  # 변환 적용
    except:
        data[col] = pd.factorize(data[col])[0]  # 예외 발생 시 기본 인코딩 적용

        data.dtypes