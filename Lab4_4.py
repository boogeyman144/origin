def main(x, *args):
    one = x
    two = sum(args)
    three = int(len(args))
    print(f"one = {one}\ntwo = {two}\nthree = {three}")
    return x - sum(args)/int(len(args))
if __name__ == '__main__':
    result = main(23, 0, 2, 1, -4, -10, 6, 0, 11)
    print(f"result = {result}")