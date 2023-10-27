def main(**kwargs):
   for i, j in kwargs.items():
       print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
   main(x=[1, 2, 3], y=[4, 5, 6], z=[0, 0, 0], w=[-1, -2, -3])