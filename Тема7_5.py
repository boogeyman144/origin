def read_usernames(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            usernames = [line.strip() for line in file]
            return usernames
def main():
    file_name = 'users.txt'
    usernames = read_usernames(file_name)
    if not usernames:
        print("Список пользователей не загружен. Программа завершает работу.")
        return
    num_users = len(usernames)
    print(f"Количество пользователей: {num_users}")
    sorted_usernames = sorted(usernames)
    print("Имена пользователей в алфавитном порядке:")
    for username in sorted_usernames:
        print(username)
if __name__ == "__main__":
    main()
