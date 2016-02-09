# Notes

## What are we trying to predict?

Whether someone makes more than $50,000 per year or not.

## What attributes are we using?

We are only using continuous attributes. Based on the writeup found [here](https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names), they are:

* age
* fnlwgt
* education-num
* capital-gain
* capital-loss
* hours-per-week

## What about examples that are missing continuous attributes?

We are dropping examples that are missing continuous attributes.

## What is our method of training?

We are using [stochastic gradient](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) descent to train our SVM.

## Did you remove unknowns or reformat the data?

I removed unknowns and cleaned up the data using clean.py.

## Is there a website for this dataset?

https://archive.ics.uci.edu/ml/datasets/Adult 