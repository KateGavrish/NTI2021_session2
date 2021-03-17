from data import db_session


# подключение к существующей бд или создание новой
def main():
    name_db = 'project'
    db_session.global_init(f"db/{name_db}.sqlite")


if __name__ == '__main__':
    main()