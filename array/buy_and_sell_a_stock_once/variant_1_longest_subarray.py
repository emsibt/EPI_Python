"""
Problem: longest_equal_subarray
Write a program that takes an array of integers and finds the length of a longest subarray
all of whose entries are equal.

Time complexity: O(n)
Space complexity: O(1)

Solution:
Maintain a running streak of consecutive equal values. Increment the streak when
adjacent values match, reset to 1 when they differ, and keep track of the maximum streak seen.
"""

def longest_equal_subarray(arr):
    if not arr:
        return 0
    prev_value, max_len, curr_len = arr[0], 1, 1
    for i in range(1, len(arr)):
        if arr[i] == prev_value:
            curr_len+=1
            max_len = max(max_len, curr_len)
        else:
            curr_len=1
            prev_value = arr[i]
    return max_len
    


def test_longest_equal_subarray():
    test_cases = [
        {
            "input": [],
            "expected": 0,
            "description": "Empty array",
        },
        {
            "input": [1],
            "expected": 1,
            "description": "Only 1 number",
        },
        {
            "input": [1,1,2,3,4,4,4,4,4,5,5,5],
            "expected": 5,
            "description": "same values appears 5 times",
        },
        {
            "input": [1,1,1,4,1,1,1,1,1],
            "expected": 5,
            "description": "same values appears in multiple places - longest is 5",
        }
    ]
    
    print("Testing longest_equal_subarray:")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        arr = test["input"]  # Make a copy to preserve original
        result = longest_equal_subarray(arr)
        passed = result == test["expected"]
        
        print(f"\nTest Case {i}: {test['description']}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print(f"  Status:   {'PASSED' if passed else 'FAILED'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_longest_equal_subarray()
