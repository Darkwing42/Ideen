#!/usr/bin/env python
import mysql.connector
from mysql.connector import errorcode

class MySqlConnection:

    def __init__(self):
        """Bei der Erstellung der Klasse wird somit die Verbindug zur Datenbank hergestellt"""
        try:
            self.cnx = mysql.connector.connect(user = "test", passwd = "tunnel2345", host = "192.168.2.103", database = "lims")
            self.cursor = self.cnx.cursor()
            print("Connection to Database .....")
        except mysql.connector.Error as err:
            print("ERROR MESSAGE " + str(err.msg))


    def RunCommand(self, cmd):
        """Gibt den Befehl an die Datenbank weiter und holt auch die Daten ein die gebraucht werden. """
        print("RUNNING COMMAND " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print("ERROR MESSAGE " + str(err.msg))
            print("WITH " + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg


    def CheckUserLogin(self, username, password):
        cmd = ("SELECT * FROM user;")
        results = self.RunCommand(cmd)
        for col in results:
            if username == col[0]:
                if password == col[1]:
                    return True
                    print("Username found, login in....")
            else:
                return False



    #def __del__(self):
    #    """Wenn die Instanz der Klasse zerstört wird, werden die Daten
    #    in die Datenbank gespeicher """
    #    self.cnx.commit()
    #    self.cursor.close()
    #    self.cnx.close()


#username = input("Username \n")
#password = input("Password \n")

#r = MySqlConnection()
#r.CheckUserLogin(username, password)
