## 1. install surprise
!pip install surprise

import os
import csv
import pandas as pd
from surprise import SVDpp
from surprise import Dataset
from surprise import Reader
from surprise import dump
from surprise.model_selection import train_test_split
algo=SVDpp()

## 2. train
re= Reader(line_format='user item rating', sep=',', rating_scale = (1, 5))
file_path = os.path.expanduser('./new_nohead.csv')
data = Dataset.load_from_file(file_path, reader=re)
trainset, testset = train_test_split(data, test_size=.25)

algo = SVDpp(n_factors=100, n_epochs=15)
algo.fit(trainset)


# 3. train model 저장
file_name=os.path.expanduser('./dump')
dump.dump(file_name, algo=algo) # 한번 학습하고 여기는 주석처리
_, algo=dump.load(file_name)

########### test #############
#user=str("A2CX7LUOHB2NDG")
#product=("321732944")
#pred=loaded_algo.predict(user, product)
#print(pred)

# server에서 받은 jasonfile
with open('./testfile.json') as data_file : # open안에 제이슨
    tmp = json.load(data_file)

user=str(tmp["UserId"])
nowarea=str(tmp["area"])


area=pd.read_csv('./area.csv') ## { 상품아이디(학습데이터), area, 상품ID }

#nowarea="C"
#user=str("A2CX7LUOHB2NDG") # usre ID 받아오기
neww=area[area['Area']==nowarea]['productID'].tolist() # 구역 받아오기
predictions=[algo.predict(str(user), str(productID)) for productID in neww] # 예측
######
def sortkey_est(pred):
  return pred.est
predictions.sort(key=sortkey_est, reverse=True)
print(predictions)
top_product_id = [int(pred.iid) for pred in predictions]
print(top_product_id)