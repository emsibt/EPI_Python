"""
Problem: Sort three keys
Assuming that keys take one of three values, reorder the array so that all objects with the
same key appear together. The order of the subarrays is not important.

Solution:
Move on smallest (1s) to the frond, the largest (3s) to the back, the middle should be 2s

Time complexity: O(n) where n is length of array
Space complexity: O(1) don't create new array
"""


def test_sort_three_keys():
    print("Testing sort_three_keys")
    print("*" * 60)
    testcases = [
        {
            "input": [1, 2, 3, 1, 2, 3],
            "expected": [1, 1, 2, 2, 3, 3],  # [2,2,3,3,1,1] is acceptable
            "description": "Mixed order with all three values",
        },
        {
            "input": [1, 1, 3, 3, 2, 2],
            "expected": [1, 1, 2, 2, 3, 3],
            "description": "Grouped but wrong order ",
        },
        {
            "input": [1, 1, 1, 1, 1, 1],
            "expected": [1, 1, 1, 1, 1, 1],
            "description": "All elements is the same (1s)",
        },
        {
            "input": [2, 2, 3, 1, 1, 3, 3],
            "expected": [1, 1, 2, 2, 3, 3, 3],
            "description": "Unbalanced distribution"
        }
    ]

    for i, t in enumerate(testcases, 1):
        arr = t["input"].copy()
        result = sort_three_keys(arr=arr)
        print(f"\n Test Case {i}: {t['description']}")
        print(f" Input:     {t['input']}")
        print(f" Expected:  {t['expected']}")
        print(f" Ouput:     {result}")
        print(f" Status:    {'PASSED' if result == t['expected'] else 'FAILED'} ")


def sort_three_keys(arr: list):
    if len(arr) < 1:
        return arr
    low, high, curr = 0, len(arr) - 1, 0
    while curr <= high:
        if arr[curr] == 1:
            arr[low], arr[curr] = arr[curr], arr[low]
            low += 1
            curr += 1
        elif arr[curr] == 3:
            arr[high], arr[curr] = arr[curr], arr[high]
            high -= 1
        else:
            curr += 1
    return arr


if __name__ == "__main__":
    test_sort_three_keys()

"""
low = 0, high = 5, curr = 0
arr[curr] = 1
arr = [1,2,3,1,2,3] -> curr++, low++

low = 1, high = 5, curr = 1
arr[curr] = 2
arr = [1,2,3,1,2,3] -> curr++

low = 1, high = 5
"""
