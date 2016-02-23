import os
import sys
import numpy as np
from sklearn import svm
from sklearn import naive_bayes
from sklearn import ensemble
from pyflann import *

def main():
    names = list()
    attributes = list()
    with open(os.path.join("data", "pubfig_attributes.txt"), "r") as data_file:
        for line in data_file.readlines()[2:]:
            elems = line.split()
            names.append(elems[0] + elems[1])
            attributes.append([float(_) for _ in elems[3:]])
    testset = list()
    with open(os.path.join("data", "pubfig_kaggle_1.txt"), "r") as data_file:
        for line in data_file.readlines()[2:]:
            elems = line.split()
            attributes.append([float(_) for _ in elems[:74]])
            attributes.append([float(_) for _ in elems[74:]])
    flann = FLANN()
    predictions = list()
    result, dists = flann.nn(dataset, testset, 2, algorithm="kmeans", branching=32, iterations=7, checks=16)
    for index in range(0, len(result), 2):
        predictions.append("1" if names[index] == names[index+1] else "0")
    print("Id,Prediction")
    print("\n".join(["{},{}".format(i, p) for i, p in predictions]))
    print()

if __name__ == "__main__":
    main()
