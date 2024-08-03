import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    # Словник для підрахунку кількості кожної можливої суми
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        # Кидаємо два кубики
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        
        # Підраховуємо кількість випадків кожної суми
        sum_counts[roll_sum] += 1
    
    # Обчислюємо ймовірності кожної суми
    probabilities = {k: v / num_rolls for k, v in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (метод Монте-Карло)')
    plt.show()

# Симулюємо кидки кубиків
num_rolls = 100000
probabilities = monte_carlo_simulation(num_rolls)

# Виводимо ймовірності у вигляді таблиці
print("Сума\tІмовірність")
for sum_, prob in probabilities.items():
    print(f"{sum_}\t{prob:.2%}")

# Будуємо графік
plot_probabilities(probabilities)
