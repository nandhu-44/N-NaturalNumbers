# Python program to add 'n' natural numbers.


def add_n_nautral_numbers(n: int) -> None:
    """
    Add the first 'n' natural numbers.

    Args:
        n (int): The number of natural numbers to add.

    Returns:
        None
    """
    if n < 1:
        print("Invalid input. Please enter a positive number.")
        exit(1)

    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"The sum of first {n} natural numbers is {sum}")

def main() -> None:
    """
    Main function to take input from the user and call the add_n_nautral_numbers function.
    """
    try:
        n = int(input("Enter the value of n : "))
        add_n_nautral_numbers(n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit(1)
    except Exception as e:
        print(f"[{e.__class__.__name__}] : {e.args[0]}")
        exit(1)


if __name__ == "__main__":
    main()
