import random


def operation_simple():

    level = "'simple operations with numbers 2-9'"
    task_ok = 0

    for task_n in range(5):

        num_1 = random.randint(2, 9)
        num_2 = random.randint(2, 9)
        sign = random.choice(['+', '-', '*'])
        result = eval(f'{num_1} {sign} {num_2}')

        print(num_1, sign, num_2)
        while True:
            try:
                if result == int(input()):
                    print('Right!')
                    task_ok += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print("Incorrect format.")

    return level, task_ok


def operation_square():

    level = "integral squares of 11-29"
    task_ok = 0

    for task_n in range(5):

        num_1 = random.randint(11, 29)

        print(num_1)
        while True:
            try:
                if int(input()) == num_1 ** 2:
                    print('Right!')
                    task_ok += 1
                else:
                    print('Wrong!')
                break

            except ValueError:
                print("Incorrect format.")

    return level, task_ok


def save_file(level_n, level, task_ok):

    print('What is your name?')
    user_name = input()
    result_file = open('results.txt', 'a', encoding='utf-8')
    result_file.write(f'{user_name}: {task_ok}/5 in level {level_n} ({level}).\n')
    result_file.close()
    print('The results are saved in "results.txt".')


#======================================================


print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9 
2 - integral squares of 11-29 """)

while True:
    try:
        level_n = int(input())
        if 0 < level_n < 3:
            if level_n == 1:
                level, task_ok = operation_simple()
            else:
                level, task_ok = operation_square()
            break
        else:
            print("Incorrect number.")

    except ValueError:
        print("Incorrect format.")

print( f'Your mark is {task_ok}/5.')
print('Would you like to save your result to the file? Enter yes or no.')

while True:
    try:
        if input() in ['yes', 'YES', 'y', 'Yes']:
            save_file(level_n, level, task_ok)
        break
    except ValueError:
        print("Incorrect format.")