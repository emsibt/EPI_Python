"""
Problem:
Given an array A of n objects with Boolean-valued keys, reorder the array so that objects
that have the key false appear first. Use O(1) additional space and O(n) time.

Time complexity: O(n)
Space complexity: O(1)

Solution:
Move all the false key to the front
"""


def test_sort_boolean_keys():
    testcases = [
        {
            "input": [True, False, True, False],
            "expected": [False, False, True, True],
            "description": "Mixed True False values",
        },
        {
            "input": [True, True, True, True],
            "expected": [True, True, True, True],
            "description": "All True values",
        },
        {
            "input": [True, True, False, False],
            "expected": [False, False, True, True],
            "description": "Grouped but incorrect position",
        },
        {
            "input": [False, True, False, True],
            "expected": [False, False, True, True],
            "description": "False True False True pattern",
        },
    ]

    for i, t in enumerate(testcases, 1):
        arr = t["input"].copy()  # create new array
        result = sort_boolean_keys(arr=arr)
        is_pass = True if t["expected"] == result else False

        print(f"Testcases {i}: {t['description']}")
        print(f" Input: {t['input']}")
        print(f" Expected: {t['expected']}")
        print(f" Ouput: {result}")
        print(f" Status: {'PASSED' if is_pass else 'FAILED'}")


def sort_boolean_keys(arr: list):
    low, curr, high = 0, 0, len(arr) - 1
    while curr <= high:
        if arr[curr] == False:
            arr[low], arr[curr] = arr[curr], arr[low]
            low += 1
            curr += 1  # Only increment curr when we've processed a False
        else:
            arr[high], arr[curr] = arr[curr], arr[high]
            high -= 1
            # Don't increment curr here - we need to check what was swapped from high
    return arr


if __name__ == "__main__":
    test_sort_boolean_keys()
