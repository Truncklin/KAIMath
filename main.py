from task1 import task1
from task2 import task2
from task3 import task3

def main():
    print("Выберите задание (1-3):")
    print("1 - Графическое отделение корней")
    print("2 - Метод половинного деления")
    print("3 - График + уточнение корня")
    
    choice = input("Введите номер задания: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    else:
        print("Неверный выбор. Введите число от 1 до 3.")

if __name__ == "__main__":
    main()