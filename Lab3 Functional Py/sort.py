data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def main():
    result = sorted(data)
    print(result)

    result_with_lambda = sorted(data, key=lambda item: item)
    print(result_with_lambda)

if __name__ == '__main__':
    main()