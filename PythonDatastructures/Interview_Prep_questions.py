import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    Problem:
    Given a sorted array of integers nums and a target value target, find the starting and ending position of target. If target is not found, return [-1, -1].
    You must solve this in O(log n) time complexity.
    """
    import numpy as np
    def generate_inputs(size=100):
        high=np.random.randint(30)
        nums = np.random.random_integers(size=size, low=0, high=high)
        target = np.random.randint(high) - 1
        nums.tolist()
        nums.sort()
        return (nums, target)
        
    nums, target = generate_inputs(size=500)

    print(nums)
    print(target)
    return generate_inputs, np, nums, target


@app.cell
def __(nums, target):

    def sliding_window(nums, target):
        hi = len(nums) - 1
        lo = 0
        xret = -1
        yret = -1
        while lo < hi:
            if nums[lo] != target:
                lo+=1
            else:
                xret = lo
            if nums[hi] != target:
                hi-=1
            else:
                yret = hi
            if xret != -1 and yret != -1:
                break
        return (xret, yret)

    print(sliding_window(nums, target))
    return (sliding_window,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
