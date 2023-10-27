def main(**kwargs):
   for i in kwargs.items():
       print(i[0], i[1])

if __name__ == '__main__':
   main(x=[1, 2, 3], y=[4, 5, 6], z=[0, 0, 0], w=[-1, -2, -3])