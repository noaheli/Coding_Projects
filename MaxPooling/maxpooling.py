import numpy as np

def max_pooling(input_arr, window, stride):
    #extract all needed variables from initial inputs
    h, l = input_arr.shape
    window_h, window_l = window
    stride_h, stride_l = stride

    #calculate the width of the final matrix to be returned
    # Found this formula online, still not entirely sure why we subtract l - window_l
    # The rest of the formula clicks in my head, but the subtract eludes me still
    # Online justifies it as the "output window must be able to fit into the input",
    # But couldn't it with division?
    # Perhaps not if the stride is set to 1.
    fin_l = (l - window_l) // stride_l + 1
    fin_h = (h - window_h) // stride_h + 1

    #(initialize output matrix)
    output = np.zeros((fin_l, fin_h))

    for i in range(fin_l):
        for j in range(fin_h):
            h_start = i * stride_h
            h_end = h_start + window_h
            l_start = j * stride_l
            l_end = l_start + window_l

            # Take the maximum value in the pooling region
            output[i, j] = np.max(input_arr[h_start:h_end, l_start:l_end])

    return output


input_arr = np.array([
[1,2,3,4,5,6],
[4,3,6,8,9,7],
[3,7,6,3,5,9],
[6,8,0,6,5,3],
[6,8,0,6,4,5],
[8,6,4,8,45,3]
])

window = (2,2)
stride = (2,2)
print(f"Initial input array: \n{input_arr}")
output = max_pooling(input_arr, window, stride)
print(f"Output after max pooling with window size of 2x2, and step size of 2.\n{output}")
