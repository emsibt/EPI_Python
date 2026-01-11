"""
Problem: Dutch Flag Partition
Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.

Solution:
Use 3 pointers to partition the array into 3 parts: smaller, equal, larger.
- smaller: all elements less than the pivot
- equal: all elements equal to the pivot
- larger: all elements greater than the pivot

Time complexity: O(n)
Space complexity: O(1)
"""


def dutch_flag_partition(arr: list, pivot_index: int) -> list:
    """
    Partition array around pivot value at given index.
    
    Args:
        arr: List of comparable elements
        pivot_index: Index of the pivot element
        
    Returns:
        The same array (modified in-place) partitioned as [< pivot, == pivot, > pivot]
    """
    if not arr or pivot_index < 0 or pivot_index >= len(arr):
        return arr
    
    pivot = arr[pivot_index]
    # arr [:smaller:equal:larger:]
    smaller, equal, larger = 0, 0, len(arr)
    
    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:  # arr[equal] > pivot
            larger -= 1
            arr[larger], arr[equal] = arr[equal], arr[larger]
    
    return arr


def verify_partition(arr: list, pivot_value: int) -> bool:
    """
    Verify that array is correctly partitioned around pivot value.
    
    Args:
        arr: Partitioned array
        pivot_value: The pivot value used for partitioning
        
    Returns:
        True if correctly partitioned, False otherwise
    """
    if not arr:
        return True
    
    i = 0
    # Check all elements < pivot
    while i < len(arr) and arr[i] < pivot_value:
        i += 1
    
    # Check all elements == pivot
    while i < len(arr) and arr[i] == pivot_value:
        i += 1
    
    # Check all elements > pivot
    while i < len(arr):
        if arr[i] <= pivot_value:
            return False
        i += 1
    
    return True


def test_dutch_flag_partition():
    """Test cases for dutch_flag_partition function."""
    test_cases = [
        {
            "input": [0, 1, 2, 0, 2, 1],
            "pivot_index": 1,
            "pivot_value": 1,
            "description": "Mixed values with pivot in middle"
        },
        {
            "input": [5, 2, 8, 1, 9, 3],
            "pivot_index": 0,
            "pivot_value": 5,
            "description": "Pivot at first index"
        },
        {
            "input": [3, 3, 3, 3, 3],
            "pivot_index": 2,
            "pivot_value": 3,
            "description": "All elements equal to pivot"
        },
        {
            "input": [7, 2, 4, 1, 9, 5, 3],
            "pivot_index": 3,
            "pivot_value": 1,
            "description": "Pivot is minimum value"
        },
        {
            "input": [4, 1, 3, 2, 4, 1, 3, 2],
            "pivot_index": 4,
            "pivot_value": 4,
            "description": "Pivot is maximum value with duplicates"
        }
    ]
    
    print("Testing dutch_flag_partition:")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        arr = test["input"].copy()  # Make a copy to preserve original
        pivot_idx = test["pivot_index"]
        pivot_val = test["pivot_value"]
        
        result = dutch_flag_partition(arr, pivot_idx)
        is_valid = verify_partition(result, pivot_val)
        
        # Count elements in each partition
        less_count = sum(1 for x in result if x < pivot_val)
        equal_count = sum(1 for x in result if x == pivot_val)
        greater_count = sum(1 for x in result if x > pivot_val)
        
        print(f"\nTest Case {i}: {test['description']}")
        print(f"  Input:        {test['input']}")
        print(f"  Pivot Index:  {pivot_idx} (value = {pivot_val})")
        print(f"  Result:       {result}")
        print(f"  Partition:    [{less_count} < {pivot_val}, {equal_count} == {pivot_val}, {greater_count} > {pivot_val}]")
        print(f"  Status:       {'PASSED' if is_valid else 'FAILED'}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_dutch_flag_partition()