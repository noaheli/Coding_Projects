import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    Problem for a List

    Given a list of integers and a target sum, return all unique pairs of numbers that add up to the target.
    Example:
    Edit
    nums = [2, 7, 4, 1, 5, 3]
    target = 6
    Output: [(2, 4), (1, 5), (3, 3)]
    """
    import numpy as np

    def generate_nums(length, max):
        l = np.random.random_integers(low=1, high=max, size=length)
        find = np.random.randint(low=int(max/2), high=max)
        return (l, find)

    listmax = np.random.randint(low=10, high=100)
    l, find = generate_nums(50, listmax)
    print(f"list: {l}\ntarget: {find}")
    return find, generate_nums, l, listmax, np


@app.cell
def __(find, l):
    #brought in bisect left to streamline finding lowest value closest to the target value
    from bisect import bisect_left
    def find_pairs(l, find):
        l.sort() #n log n
        find_index = bisect_left(l,find) #n
        subarray = l[0:find_index] #1

        print(subarray)

        winlo = 0
        winhi = len(subarray) - 1
        pairs= []
        while winlo < winhi: # O n
            lo=subarray[winlo]
            hi=subarray[winhi]
            sum = lo + hi
            print(f"{lo} + {hi} = {sum}")
            if sum == find:
                pairs.append((lo, hi))
                winlo += 1
            elif sum < find:
                winlo += 1
            else:
                winhi -= 1
        return pairs

    pairs = find_pairs(l.tolist(), find)
    #runtime nlogn
    print(pairs)
    return bisect_left, find_pairs, pairs


if __name__ == "__main__":
    app.run()
