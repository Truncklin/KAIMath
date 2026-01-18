from task1 import task1
from task2 import task2
from task3 import task3
from task2_1 import task2_1
from task3_1 import task3_1
from task3_2 import task3_2
from task3_3 import task3_3

def main():
    print("Выберите задание (1-3):")
    print("1 - Графическое отделение корней")
    print("2 - Метод половинного деления")
    print("3 - График + уточнение корня")
    print("4 - lab2 - 1")
    print("5 - lab3 - 1")
    print("6 - lab3 - 2")
    print("7 - lab3 - 3")
    
    choice = input("Введите номер задания: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task2_1()
    elif choice == "5":
        task3_1()
    elif choice == "6":
        task3_2()
    elif choice == "7":
        task3_3()
    else:
        print("Неверный выбор. Введите число от 1 до 7.")

if __name__ == "__main__":
    main()