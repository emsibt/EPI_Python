"""
Problem: buy and sell stock once
Write a program that takes an array denoting the daily stock price, and retums the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.

Time complexity: O(n)
Space complexity: O(1)

Solution:
Calculate the profit sell at each day, compare to choose the max_profit, at the same time determine
what is the lowest price.
"""

def buy_and_sell_stock_once(prices):
    if len(prices) < 2:
        return 0
    min_price, max_profit = float('inf'), 0
    for price in prices:
        profit_sell_today = price - min_price
        max_profit = max(max_profit, profit_sell_today)
        min_price = min(min_price, price)
    return max_profit


def test_buy_and_sell_stock_once():
    test_cases = [
        {
            "input": [310, 315, 275, 295, 260, 270, 290, 230, 255, 250],
            "expected": 30,
            "description": "Buy at 260 and sell at 290",
        },
        {
            "input": [310, 210, 110, 10],
            "expected": 0,
            "description": "No profit",
        },
        {
            "input": [210, 210, 210, 210],
            "expected": 0,
            "description": "No profit",
        }
    ]
    
    print("Testing buy_and_sell_stock_once:")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        arr = test["input"]  # Make a copy to preserve original
        result = buy_and_sell_stock_once(arr)
        passed = result == test["expected"]
        
        print(f"\nTest Case {i}: {test['description']}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print(f"  Status:   {'PASSED' if passed else 'FAILED'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_buy_and_sell_stock_once()