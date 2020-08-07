def check_palindrome(number):
    num = number
    reversed_num = 0

    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    return number == reversed_num


def largest_palindrome(n):
    upper_limit = 0

    for i in range(1, n + 1):
        upper_limit = upper_limit * 10
        upper_limit = upper_limit + 9

    lower_limit = 1 + upper_limit // 10

    max_product = 0

    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if product < max_product:
                break

            if check_palindrome(product) and product > max_product:
                max_product = product

    return max_product


if __name__ == "__main__":
    n = int(input('Enter the digit: '))
    print(largest_palindrome(n))
