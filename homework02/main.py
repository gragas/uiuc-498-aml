import os
import numpy as np

def main():
    # Specify the type of each example
    _dtype = np.dtype([('age', 'int'),
                       ('fnlwgt', 'int'),
                       ('education-num', 'int'),
                       ('capital-gain', 'int'),
                       ('capital-loss', 'int'),
                       ('hours-per-week', 'int'),
                       ('income', np.str_, 1),])
    # Load the cleaned data into a numpy array
    data = np.loadtxt(open(os.path.join("data", "clean.data")), delimiter=", ", dtype=_dtype)
    

if __name__ == "__main__":
    main()
