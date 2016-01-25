import pandas as pd 
from pandas import DataFrame
#from  pandas.DataFrame import iterrows
import sklearn
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

match,TP,TN,FP,FN,pos,neg = 0,0,0,0,0,0,0
sample = pd.read_csv('real_data.csv',sep='\t',keep_default_na=False, na_values=[""])
sample_df = pd.DataFrame(sample)
print (sample_df.head())
if next(sample_df.iterrows())[1][2]=='Negative':
    print "Hello"
print len(sample_df)

for ind,row in sample_df.iterrows():
    if row[2] == 'Negative':
        neg+=1
    else:
        pos+=1
print pos,neg

print '------------------'

sample_df_train, sample_df_test = sklearn.cross_validation.train_test_split(sample_df, train_size=0.7)


clst = sklearn.cluster.KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)
clst.fit(sample_df_train[['Polarity','Gravity']])

le = preprocessing.LabelEncoder()
le.fit(sample_df_test['Sense'])
list(le.classes_)
class_label =  le.transform(sample_df_test['Sense'])#array([1,0])
print 'class Label after transforming is:\n',class_label



result = clst.predict(sample_df_test[['Polarity','Gravity']])
print result
for i in range(len(class_label)):
     if class_label[i] == result[i]:
        match+=1
        if result[i] == 1:
            TP+=1
        else:
            TN+=1
     else:
         if class_label[i] == 0:
            FP+=1
         else:
            FN+=1
         continue
print match,len(class_label),len(result),TP,TN,FP,FN
print "Accuracy is: ",(match/float(len(class_label)))*100
P = TP/(float(FP)+float(TP))
R = TP/(float(FN)+float(TP))
print " Precision is: ",P
print "Recall is: ",R
print "F-Measure is : ",(2*(P*R)/(P+R))
