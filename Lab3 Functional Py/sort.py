data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def main():
    result = sorted(data)
    print(result)

    result_with_lambda = lambda i: i in sorted(result)
    print(result_with_lambda)

if __name__ == '__main__':
    main()