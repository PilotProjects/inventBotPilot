# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

#функция записи начала смены в базу данных
def writeToDbChangeTime(operatorname,begindatetime,finishdatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO change_time (begin_datetime, finish_datetime, operator_name) VALUES ('%s','%s','%s')"%(begindatetime, finishdatetime, operatorname))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()



#функция записи партии в базу данных
def writeToDbSetLog(seller,sellerpaper,transport,begindatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO set_log (seller,seller_paper,transport,begin_datetime) VALUES ('%s','%s','%s','%s')"%(seller,sellerpaper,transport,begindatetime))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#функция записи параметров бревна в базу данных
def writeToDbLogs(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO logs (code_name, poroda, D, L, sbeg, kriv, Dmax, scannig_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#функция записи IP адресов трёх датчиков в базу данных
def writeToDbIpAdress(ipAdress1,ipAdress2,ipAdress3):
    baseAdress='192.168.1.'
    fullAdress1=(baseAdress + ipAdress1)
    fullAdress2=(baseAdress + ipAdress2)
    fullAdress3=(baseAdress + ipAdress3)
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO ip_adress (ip_adress1, ip_adress2, ip_adress3) VALUES ('%s','%s','%s')"%(fullAdress1,fullAdress2,fullAdress3))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#функция считывания данных о смене
def readFromDbChangeTime():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM change_time WHERE id = (SELECT max(id) FROM change_time)')
        conn.commit()
        unitChangeTime = cursor.fetchone()
        return(unitChangeTime)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


#функция считывания данных о партии
def readFromDbSetLog():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM set_log WHERE id = (SELECT max(id) FROM set_log)')
        conn.commit()
        unitSetLog = cursor.fetchone()
        return(unitSetLog)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()



#функция считывания данных о бревнах
def readFromDbLogs():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM logs WHERE id = (SELECT max(id) FROM logs)')
        conn.commit()
        unitLogs = cursor.fetchone()
        return(unitLogs)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#функция считывания данных об IP адресах
def readFromDbIpAdress():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ip_adress WHERE id = (SELECT max(id) FROM ip_adress)')
        conn.commit()
        unitIpAdress = cursor.fetchone()
        return(unitIpAdress)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()
