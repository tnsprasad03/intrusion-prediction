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
import pdb


def executeModel(m):
   
   df = pd.read_csv("data/train.tsv", na_values='?',delimiter='\t')
   snip = df['boilerplate']
   snip = snip[:1000]

   X = np.array(snip)

   y = np.array(df['label'])

   print X.shape
   #pdb.set_trace()
   

   sys.exit()
   
   if m == 'lr':
      model  = LogisticRegression(C=1, penalty='l2', tol=0.01)
      scores = cross_validation.cross_val_score(model, X, y, cv=5)
      print "%s -- %s" % (model.__class__, np.mean(scores))

   if m == 'rf':
      model = RandomForestClassifier(verbose=10, n_estimators=1, n_jobs=-1, max_features=None)
      scores = cross_validation.cross_val_score(model, X, target, cv=5)
      print "%s -- %s" % (model.__class__, np.mean(scores))


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
      print "Unable to run Model. Please check options"


if __name__ == "__main__":
   main(sys.argv[1:])
