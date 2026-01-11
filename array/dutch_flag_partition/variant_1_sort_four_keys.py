"""
Problem: Sort Four Keys
Given an array A of n objects with keys that takes one of four values (1, 2, 3, 4),
reorder the array so that all objects that have the same key appear together.
Use O(1) additional space and O(n) time.

Solution: Divide into 2 stages
- Stage 1: Move all smallest (1s) to front and all largest (4s) to back (2s and 3s in middle block)
- Stage 2: Sort 2s and 3s in the middle block

Time complexity: O(n)
Space complexity: O(1)
"""


def sort_four_keys(arr: list) -> list:
    """
    Sort an array containing only values 1, 2, 3, 4 in-place.
    
    Args:
        arr: List of integers containing only values 1, 2, 3, 4
        
    Returns:
        The same array (modified in-place) sorted as [1s, 2s, 3s, 4s]
    """
    if not arr:
        return arr
    
    # Stage 1: Separate 1s to front and 4s to back
    low, high, curr = 0, len(arr) - 1, 0
    
    while curr <= high:
        if arr[curr] == 1:
            arr[low], arr[curr] = arr[curr], arr[low]
            low += 1
            curr += 1
        elif arr[curr] == 4:
            arr[high], arr[curr] = arr[curr], arr[high]
            high -= 1
        else:
            curr += 1
    
    # Stage 2: Sort 2s and 3s in the middle block
    mid_low = low
    mid_high = high
    mid_curr = mid_low
    
    while mid_curr <= mid_high:
        if arr[mid_curr] == 2:
            arr[mid_curr], arr[mid_low] = arr[mid_low], arr[mid_curr]
            mid_low += 1
            mid_curr += 1
        else:  # arr[mid_curr] == 3
            mid_curr += 1
    
    return arr


def test_sort_four_keys():
    """Test cases for sort_four_keys function."""
    test_cases = [
        {
            "input": [2, 1, 4, 3, 2, 1, 4, 3],
            "expected": [1, 1, 2, 2, 3, 3, 4, 4],
            "description": "Mixed order with all four values"
        },
        {
            "input": [4, 3, 2, 1],
            "expected": [1, 2, 3, 4],
            "description": "Reverse order"
        },
        {
            "input": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1],
            "description": "All same value (1s)"
        },
        {
            "input": [3, 3, 2, 2, 1, 1, 4, 4],
            "expected": [1, 1, 2, 2, 3, 3, 4, 4],
            "description": "Grouped but wrong order"
        },
        {
            "input": [4, 4, 4, 2, 2, 1, 1, 3, 3],
            "expected": [1, 1, 2, 2, 3, 3, 4, 4, 4],
            "description": "Unbalanced distribution"
        }
    ]
    
    print("Testing sort_four_keys:")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        arr = test["input"].copy()  # Make a copy to preserve original
        result = sort_four_keys(arr)
        passed = result == test["expected"]
        
        print(f"\nTest Case {i}: {test['description']}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print(f"  Status:   {'PASSED' if passed else 'FAILED'}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_sort_four_keys()