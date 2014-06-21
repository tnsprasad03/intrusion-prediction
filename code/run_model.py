#!/usr/bin/env python
import sys, getopt
import json
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans,MiniBatchKMeans
from math import sqrt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import json
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pdb


def executeModel(m):
   
   df = pd.read_csv("../data/ProcessedData.csv", na_values='?',delimiter=',')
   snip = df
   #snip = df[:12000]
   #pdb.set_trace()

   y = np.array(snip['TypeOfTransaction'])
   y[np.where(y == 'normal.')] = 0 
   y[np.where(y!=0)] = 1 

   snip = snip.drop('TypeOfTransaction',1)
   snip = snip.drop('protocol_type:',1)
   snip = snip.drop('service:',1)
   snip = snip.drop('flag:',1)

   X = np.array(snip)

   #df_test = pd.read_csv("../data/kddtest.data", na_values='?',delimiter=',')
   df_test = pd.read_csv("../data/kdd-realtime.data", na_values='?',delimiter=',')
   tsnip = df_test

   y_t = np.array(tsnip['TypeOfTransaction'])
   y_t[np.where(y_t == 'normal.')] = 0 
   y_t[np.where(y_t!=0)] = 1 


   tsnip = tsnip.drop('TypeOfTransaction',1)
   tsnip = tsnip.drop('protocol_type:',1)
   tsnip = tsnip.drop('service:',1)
   tsnip = tsnip.drop('flag:',1)

   X_t = np.array(tsnip)


   print "X Data train: ",X.shape
   print "Real data set: ",X_t.shape
   

   #sys.exit()
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
   clf = ()

   if m == 'lr':
      print "Running Logistic Regression ..."
      clf  = LogisticRegression(C=1, penalty='l2', tol=0.01)

   if m == 'rf':
      print "Running Random Forest Classifier ..."
      clf = RandomForestClassifier(verbose=10, n_estimators=10, n_jobs=-1, max_features=20)

   if m == 'knn':
      print "Running K-Nearest Neighbors with 5 neighbhors ..."
      clf = KNeighborsClassifier(n_neighbors=5)

   clf = clf.fit(X_train, y_train)
   y_pred = clf.predict(X_test)

   pred_true = sum(y_pred==y_test)
   actual_true = len(y_test)
   print "Prediction Accuracy : %f " %(pred_true * 100.0 /actual_true)

   y_t_pred = clf.predict(X_t)

   t_pred_true = sum(y_t_pred==y_t)
   t_actual_true = len(y_t)
   print "Realtime - Prediction Accuracy : %f " %(t_pred_true * 100.0 /t_actual_true)

def usage():
      print 'run_model.py -m lr/rf ( lr for logistic and rf for random forest)'
def main(argv):
   model = ""

   try:
      opts, args = getopt.getopt(argv,"hm:",["lr"])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-m"):
         model = arg
   print 'Input option is %s' % (model)
   
   if (model):
      executeModel(model)
   else:
      usage()
      print "Unable to run Model. Please check options"


if __name__ == "__main__":
   main(sys.argv[1:])
