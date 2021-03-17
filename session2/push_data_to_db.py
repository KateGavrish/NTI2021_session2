from data.comission import Comission

from data import db_session

# подключение к существующей бд или создание новой
def main():
    surn = ['Тарасова', 'Уварова', 'Елисеев', 'Михайлов']
    nam = ['Елена', 'Екатерина', 'Василий', 'Леонид']
    midd = ['Михайловна', 'Васильевна', 'Петрович', 'Кириллович']
    pho = '8 (800) 100-00-01'
    emai = ['tar.e.sgu@yandex.ru', 'uva.e.sgu@yandex.ru', 'eli.v.sgu@yandex.ru', 'mih.l.sgu@yandex.ru']
    name_db = 'project'
    db_session.global_init(f"db/{name_db}.sqlite")
    session = db_session.create_session()
    for i in range(4):
        user = Comission()
        user.login = surn[i] + nam[i][0] + midd[i][0]
        user.password = surn[i] + nam[i] + '123'
        user.name = nam[i]
        user.surname = surn[i]
        user.middle_name = midd[i]
        user.phone = pho
        user.email = emai[i]
        session.add(user)

    session.commit()


if __name__ == '__main__':
    main()
