def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Визначаємо кількість різних видів страв
    n = len(items)
    # Створюємо список для зберігання інформації про страви
    item_list = list(items.items())
    
    # Створюємо матрицю dp, де dp[i][w] означає максимальну калорійність, яку можна досягти, використовуючи перші i страв і бюджет w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо матрицю dp
    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначаємо вибрані страви за допомогою зворотного проходу по матриці dp
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_info = item_list[i - 1]
            chosen_items.append(item_name)
            w -= item_info['cost']
    
    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in chosen_items)
    
    return chosen_items, total_calories, total_cost

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:", greedy_result)

dp_result = dynamic_programming(items, budget)
print("Динамічне програмування:", dp_result)
