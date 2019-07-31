from app import app as application
from flask import Flask, session, url_for, jsonify
from flaskext.mysql import MySQL

class webAppFunctions():
    mysql = MySQL()
    mysql.init_app(application)

    def returnNextID(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        query = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'ORDERS' and table_schema = 'c3518706';"
        cursor.execute(query)
        records = cursor.fetchone()
        conn.close()
        cursor.close()
        return records[0]

    def printItems(self, category):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        query  = "SELECT * FROM PRODUCT WHERE Product_Cat=%s;"
        cursor.execute(query, (category))
        row_headers=[x[0] for x in  cursor.description]
        output =  cursor.fetchall()
        var_fixed = []
        json_data=[]
        for row in output:
            var_fixed.append(list(map(str, list(row))))
        for result in var_fixed:
            json_data.append(dict(zip(row_headers,result)))
        if json_data != None:
            conn.close()
            cursor.close()  
            return jsonify({category:json_data})

    def getUserDetails(self, email, admin):
        conn = self.mysql.connect()
        
        if session['user']['_admin'] == True:
            cursor = conn.cursor()
            query  = "SELECT Email_Address FROM STAFF WHERE Email_Address=%s;"
            cursor.execute(query, (email))
            records = cursor.fetchone()
            conn.close()
            cursor.close()
            return jsonify({'account_email':records[0]})
        else:
            cursor = conn.cursor()
            query  = "SELECT EmailAddress, User_Forname, User_Surname FROM CUSTOMER WHERE EmailAddress=%s;"
            cursor.execute(query, (email))
            records = cursor.fetchone()
            conn.close()
            cursor.close()
            return jsonify({'user_forename':records[1], 'user_surname':records[2], 'account_email':records[0]})