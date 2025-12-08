import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    
    signal = np.array(signal)

    if signal.ndim != 1:
        return "Please enter a valid 1D NumPy array"
    
    n = len(signal)
    
    turning_point = []
    
    for i in range(1, n-1):
        left_slope = signal[i] - signal[i-1]     # direction before
        right_slope = signal[i+1] - signal[i]    # direction after

        # direction changes if slopes have opposite signs
        if left_slope * right_slope < 0:
            turning_point.append(i)
    
    turning_point = np.array(turning_point)
    
    plt.figure()
    plt.plot(signal, marker = "o")
    plt.scatter(turning_point, signal[turning_point], s = 80, marker = "X")
    plt.title("Turning points in Signal")
    plt.xlabel("Index")    
    plt.ylabel("Value")
    
    plt.savefig(filename)
    plt.show()
    
    return turning_point
    

signal = np.array([1,4,5,8,6,8,5,9])
print(detect_turning_points(signal))

#Write a function `detect_turning_points(signal, filename="turning_points.pdf")` that:

#- receives a 1D NumPy array representing a signal
#- identifies all indices where the direction of the signal changes  
#  (i.e., where the discrete difference changes sign),
#- plots the signal and mark these turning points,
#- saves the figure as a PDF file,
#- and returns a NumPy array containing the indices of the detected points