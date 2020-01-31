# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

#функция записи начала смены в базу данных
def writeToDbJson(location, answer, installator_id, date, photo_1, photo_2, photo_3, photo_4, photo_5):

    try:
        conn = lite.connect('operface/db.sqlite3')
        cursor = conn.cursor()
        sql = "INSERT INTO main_oper_face_installation (id, location, answer, Instalator_id_id, date, photo_1, photo_2, photo_3, photo_4, photo_5) VALUES (NULL ,'%s','%s','%i','%s','%s','%s','%s','%s','%s')"%(location, answer, installator_id, date, photo_1, photo_2, photo_3, photo_4, photo_5)
        cursor.executescript(sql)
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print (lite.Error)
        sys.exit(1)
    finally:

        if conn:

            conn.close()
