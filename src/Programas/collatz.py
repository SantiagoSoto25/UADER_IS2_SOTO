import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def main():
    max_num = 10000
    iterations = []
    starting_numbers = []

    for i in range(1, max_num + 1):
        iterations.append(collatz(i))
        starting_numbers.append(i)

    plt.scatter(iterations, starting_numbers, s=5)
    plt.title('Conjetura de Collatz')
    plt.xlabel('Número de iteraciones para converger')
    plt.ylabel('Número de inicio de la secuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

