import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    
    A = np.array(A)

    # 2D
    if A.ndim != 2:
        return "Please enter a valid 2D list or NumPy array"
    
    
    #dimension of array
    num_rows = A.shape[0]
    num_cols = A.shape[1]
    
    #array to store ranges
    column_range = np.zeros(num_cols)
    
    for col in range(num_cols):
        #  min and max for this column
        col_min = A[0, col]     #takes first value of column
        col_max = A[0, col]
        
        # Find min and max in this column
        for row in range(1, num_rows):
            value = A[row, col]
            if value < col_min:
                col_min = value
            if value > col_max:
                col_max = value
        
        # range for this column
        column_range[col] = col_max - col_min
    
    # bar plot
    plt.figure()
    x_positions = np.arange(num_cols)
    plt.bar(x_positions, column_range)
    plt.xlabel("Column Index")
    plt.ylabel("Range")
    plt.title("Ranges in Array A")


    plt.savefig(filename)
    plt.show()

    return column_range
    
    pass

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [0, 8, 2]
])
ranges = column_range_plot(A)
print("Column ranges: ", ranges)


#Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

#- receives a 2D NumPy array `A`,
#- computes the range (maximum minus minimum) of each column,
#- create a bar plot showing the ranges of all columns,
#- saves the plot as a PDF file,
#- and returns a 1D NumPy array containiing the column ranges.