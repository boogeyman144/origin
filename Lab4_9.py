from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(f"сегодня {dt.today().date()}.\nдень недели - {dt.today().isoweekday()}.")
    i = int(input('введите количество дней: '))
    today = dt.today()
    result = today + td(days=i)
    print(f"через {i} дней будет {result.date()}.\nдень недели - {result.isoweekday()}.")
if __name__ == '__main__':
    main()