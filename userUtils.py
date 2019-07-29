from bcrypt import hashpw, gensalt, checkpw
from app import app
from flask import Flask, session, url_for, jsonify
from flaskext.mysql import MySQL

class user():
    _mailuid = ""
    _pass = u""
    _confirm_pass = ""
    _logged_in = False
    _userName = ""
    _firstName = ""
    _secondName = ""
    _userID = 0
    _admin = False
    this_dict = dict()
    mysql = MySQL()
    mysql.init_app(app)

    def setUser(self, user):
        self._userName = user
    
    def setUserFirstName(self, user):
        self._firstName = user
    
    def setUserSecondName(self,user):
        self._secondName = user
    
    def getUserFirstName(self):
        return self._firstName
    
    def getUserSecondName(self):
        return self._secondName
    
    def getUser(self):
        return self._userName

    def setEmail(self,user):
        self._mailuid = user
    
    def getEmail(self):
        return self._mailuid
    
    def setID(self,user):
        self._userID = user
    
    def getID(self):
        return self._userID
    
    def setAdmin(self,user):
        self._admin = user
    
    def getAdmin(self):
        return self._admin

    def setPass(self,user):
        self._pass = user
    
    def getPass(self):
        return self._pass
    
    def setConfirmPass(self,user):
        self._confirm_pass = user
    
    def getConfirmPass(self):
        return self._confirm_pass
    
    def setLoggedIn(self,user):
        self._logged_in = user

    def getUserObject(self):
        self.this_dict['_mailuid'] = self._mailuid
        self.this_dict['_logged_in'] = self._logged_in
        self.this_dict['_userID'] = self._userID
        self.this_dict['_admin'] = self._admin
        return jsonify(self.this_dict)
    
    def checkIfDataNotEmpty(self, email, password):
        if not email and not password:
            return jsonify({'error':'Login fields cannot be empty!'})
        elif not email:
            return jsonify({'error':'Please enter an email!'})
        elif not password:
            return jsonify({'error':'Please enter a password!'})
        else:
            return True

    def checkUser(self, user, password):
        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()

        if self.cursor.execute("SELECT EmailAddress, User_ID, Password FROM CUSTOMER WHERE EmailAddress=%s", (user)):

            records = self.cursor.fetchone()

            if records == None:
                return False
            else:
                row = records

                if not checkpw(password, row[2].encode('utf8')):
                    return False
                elif checkpw(password, row[2].encode('utf8')):
                    self.setLoggedIn(True)
                    self.setUser(row[0])
                    self.setEmail(row[0])
                    self.setID(row[1])
                    self.setAdmin(False)
                    return True       
        else:
            return jsonify({'error':'SQL Error occured!'})  
    
    def checkAdmin(self, user, password):
        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()

        if self.cursor.execute("SELECT Email_Address, Staff_ID, Password FROM STAFF WHERE Email_Address=%s", (user)):

            records = self.cursor.fetchone()

            if records == None:
                return False
            else:

                row = records

                if not checkpw(password, row[2].encode('utf8')):
                    return False
                elif checkpw(password, row[2].encode('utf8')):
                    self.setLoggedIn(True)
                    self.setUser(row[0])
                    self.setEmail(row[0])
                    self.setID(row[1])
                    self.setAdmin(True)
                    return True      
        else:
            return jsonify({'error':'SQL Error occured!'})  