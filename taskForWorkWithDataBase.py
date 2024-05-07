import sqlite3
class WorkWithAPerson:
    @staticmethod
    def create_database():
        answer = input("Ви хочете створити нову базу даних? (ТАК/НІ): ").upper()
        if answer == "ТАК":
            name_of_database = input("Введіть назву бази даних: ")
            method_field_1 = input("Введіть назву першого поля для об'єкта БД: ")
            method_field_2 = input("Введіть назву другого поля для об'єкта БД(це поле буде приймати цілі числа): ")
            method_field_3 = input("Введіть назву третього поля для об'єкта БД(це поле буде приймати цілі числа): ")
            Controller.create_database(name_of_database, method_field_1, method_field_2, method_field_3)
        elif answer == "НІ":
            print("Ви вирішили не створювати нову базу даних.")

    @staticmethod
    def manipulate_database():
        answer = input("Ви хочете редагувати існуючу базу даних? (ТАК/НІ): ").upper()
        if answer == "ТАК":
            operation = input("Що б ви хотіли зробити? (Додати/Видалити/Змінити/Отримати інформацію): ").upper()
            if operation == "ДОДАТИ":
                name_of_database = input("Введіть назву вашої БД: ")
                method_field_1 = input("Введіть перше поле для об'єкту БД: ")
                method_field_2 = int(input("Введіть друге поле для об'єкту БД(у цифрах): "))
                method_field_3 = int(input("Введіть третє поле для об'єкту БД(у цифрах): "))
                Controller.add_item_to_database(name_of_database, method_field_1, method_field_2, method_field_3)
            elif operation == "ВИДАЛИТИ":
                name_of_database = input("Введіть назву вашої БД: ")
                item_id = int(input("Введіть ID об'єкта, який ви хочете видалити: "))
                Controller.delete_item_from_database(name_of_database, item_id)
            elif operation == "ЗМІНИТИ":
                name_of_database = input("Введіть назву вашої БД: ")
                item_id = int(input("Введіть ID об'єкта, який ви хочете змінити: "))
                method_field_1 = input("Введіть перше поле для об'єкту БД: ")
                method_field_2 = int(input("Введіть друге поле для об'єкту БД(у цифрах): "))
                method_field_3 = int(input("Введіть третє поле для об'єкту БД(у цифрах): "))
                Controller.change_info_in_database(name_of_database, item_id, method_field_1, method_field_2,
                                                   method_field_3)
            elif operation == "ОТРИМАТИ ІНФОРМАЦІЮ":
                name_of_database = input("Введіть назву вашої БД: ")
                Controller.get_info_from_database(name_of_database)
        elif answer == "НІ":
            print("Ви вирішили не редагувати базу даних.")


class Controller:
    @staticmethod
    def create_database(type_of_database, method_field_1, method_field_2, method_field_3):
        sql_create_database = f'''CREATE TABLE IF NOT EXISTS {type_of_database}(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    {method_field_1} TEXT NOT NULL,
                                    {method_field_2} INTEGER NOT NULL,
                                    {method_field_3} INTEGER NOT NULL
                                );'''
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        cursor.execute(sql_create_database)
        connection.commit()
        connection.close()

    @staticmethod
    def add_item_to_database(type_of_database, method_field_1, method_field_2, method_field_3):
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO {type_of_database}({method_field_1}, {method_field_2}, {method_field_3})
                          VALUES(?, ?, ?)""", (method_field_1, method_field_2, method_field_3))
        connection.commit()
        connection.close()

    @staticmethod
    def delete_item_from_database(type_of_database, item_id):
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM {type_of_database} WHERE id = ?""", (item_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def change_info_in_database(type_of_database, item_id, method_field_1, method_field_2, method_field_3):
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE {type_of_database} SET method_field_1 = ?, 
                          method_field_2 = ?, 
                          method_field_3 = ? 
                          WHERE id = ?""", (method_field_1, method_field_2, method_field_3, item_id))
        connection.commit()
        connection.close()

    @staticmethod
    def get_info_from_database(type_of_database):
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM {type_of_database}")
        for row in result:
            print(row)
        connection.close()

    @staticmethod
    def get_accurate_info_from_database(type_of_database, field, min_val, max_val):
        connection = sqlite3.connect(f"{type_of_database}.sqlite")
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM {type_of_database} WHERE {field} BETWEEN ? AND ?", (min_val, max_val))
        for row in result:
            print(row)
        connection.close()


if __name__ == "__main__":
    try:
        print("Привіт! Це програма для роботи з базами даних.")
        WorkWithAPerson.create_database()
        WorkWithAPerson.manipulate_database()
    except Exception as e:
        print("Виникла помилка:", e)
