def threshold(dailyGains, goal):
    total = 0
    days = 0

    for gain in dailyGains:
        total += gain
        days += 1
        if total >= goal:
            return days
    return "Goal not achievable"


daily_gains = [5, 3, 8, 2, 9, 1]
profit_goal = int(input("Enter your goal: "))

result = threshold(daily_gains, profit_goal)
print(f"The minimum number of days to reach the goal is: {result}")
