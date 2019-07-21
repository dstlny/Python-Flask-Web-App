from bcrypt import hashpw, gensalt, checkpw
from app import app as application
from flask import Flask, render_template, request, json, session, redirect, url_for, escape, jsonify
from flaskext.mysql import MySQL

class webAppFunctions():
    mysql = MySQL()
    mysql.init_app(application)
    product_dict = {}

    def returnNextID(self):
        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()
        query = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'ORDERS' and table_schema = 'c3518706';"
        self.cursor.execute(query)
        records = self.cursor.fetchone()
        return records[0]
        self.conn.close()

    def printItems(self, category):
        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()
        query  = f"SELECT * FROM PRODUCT WHERE Product_Cat = '{category}';"
        self.cursor.execute(query)
        row_headers=[x[0] for x in  self.cursor.description]
        output =  self.cursor.fetchall()
        var_fixed = []
        json_data=[]
        for row in output:
            var_fixed.append(list(map(str, list(row))))
        for result in var_fixed:
            json_data.append(dict(zip(row_headers,result)))
        if json_data != None:  
            return json.dumps({category:json_data})

    def getUserDetails(self, email, admin):
        self.conn = self.mysql.connect()
        
        if admin == True:
            self.cursor = self.conn.cursor()
            query  = f"SELECT Email_Address FROM STAFF WHERE Email_Address = '{email}';"
            self.cursor.execute(query)
            records = self.cursor.fetchone()
            return json.dumps({'account_email':records[0]})
        else:
            self.cursor = self.conn.cursor()
            query  = f"SELECT EmailAddress, User_Forname, User_Surname FROM CUSTOMER WHERE EmailAddress = '{email}';"
            self.cursor.execute(query)
            records = self.cursor.fetchone()
            return json.dumps({'user_forename':records[1], 'user_surname':records[2], 'account_email':records[0]})

        self.conn.close()
            

        


            





        