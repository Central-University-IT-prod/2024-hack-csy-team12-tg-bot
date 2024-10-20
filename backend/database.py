import sqlite3 as sq
token = "{{sensitive data}}"

# запуск программы когда кнопка забронировать нажата
with sq.connect("data.db") as con:
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS "user" (
    id CHAT_ID NOT NULL,
    qu QUEUE,
    time 
    )""")





 #когда юзер прошел очередь, т.е его позиция удаляется из очереди   cursor.execute("DROP TABLE IF EXISTS "user"  ")

