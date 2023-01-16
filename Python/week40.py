# Pascal triangle app

def pascal_triangle(level: int, numbers):
    if level == 1:
        return [1]
    new_list: list = []
    for n in range(len(numbers)+1):
        try:
            if n == 0:
                new_list.append(1)
            else:
                new_list.append(numbers[n] + numbers[n - 1])
        except IndexError:
            new_list.append(1)
    return new_list


def main():
    levels: int = int(input("How many levels do you want? "))
    numbers = [1]
    for level in range(1, levels + 1):
        numbers = pascal_triangle(level, numbers)
        print(f"{level}\t{numbers}")


if __name__ == '__main__':
    main()
