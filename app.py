from bcrypt import hashpw, gensalt, checkpw
from flask import Flask, render_template, request, json, session, redirect, url_for, escape, jsonify
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'c3518706'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()

@app.route("/product_cat", methods=['POST'])
def getProducts():
    url = '/product_cat'
    from webAppFunctions import webAppFunctions
    json = request.get_json()  # parse as JSON
    return webAppFunctions().printItems(category=json['category'])

@app.route("/")
@app.route("/main")
def main():
    url = '/login'
    return render_template('index.html', url=url)

@app.route('/register')
def showSignUp():
    url = '/signUp'
    return render_template('signup.html', url=url)

@app.route('/logout')
def logout():
    session.clear()
    print('Session cleaned up')
    return json.dumps({'message':'Logged out successfully!','redirect':'/'})

@app.route('/account')
def account_page():
    return render_template('account.html', _mailuid=session['user']['_mailuid'], logged_in=session['user']['_logged_in'], admin=session['user']['_admin'], url='/account', reset_pass_url='/resetPass')

@app.route('/resetPass', methods=['POST'])
def reset_user_pass():
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    _curr = request.form['inputCurrPass'].encode('utf-8')
    _new = request.form['inputNewPass'].encode('utf-8')
    _newCon = request.form['inputNewPassConfirm'].encode('utf-8')
    _hashed_password = hashpw(_new, gensalt()).decode('utf-8')

    if session['user']['_admin'] == True:
        email = session['user']['_mailuid']
        query = f"SELECT Password FROM staff WHERE Email_Address = '{email}';"
        query2 = f"UPDATE staff SET Password='{_hashed_password}' WHERE Email_Address='{email}'"
    else:
        email = session['user']['_mailuid']
        query = f"SELECT Password FROM customer WHERE EmailAddress = '{email}';"
        query2 = f"UPDATE customer SET Password = '{_hashed_password}' WHERE EmailAddress = '{email}'"
    
    try:
        if _curr and _new and _newCon:

            if _curr != _new and _newCon != _curr:

                if _new != _newCon:
                    data = {'error': 'Confirmation password does not match!'}
                    return json.dumps(data)
                elif _new == _newCon:
                    cursor = conn.cursor()
                    cursor.execute(query)
                    records = cursor.fetchone()
                    
                    if records == None:
                        return False
                    else:
                        row = records
                        if not checkpw(_curr, row[0].encode('utf8')):
                            data = {'error': 'Current Password does not match!'}
                            return json.dumps(data)
                        elif checkpw(_curr, row[0].encode('utf8')):
                            cursor.execute(query2)
                            conn.commit()
                            conn.close()
                            cursor.close()
                            data = {'message': 'Password succesfully changed!'}
                            return json.dumps(data)
            else:
                data = {'error': 'New Password cannot be the same as your current password!'}
                return json.dumps(data)
        else:
            data = {'error': 'You must enter data!!'}
            return json.dumps(data)
    except Exception as error:
        print(error)

@app.route('/return_user_details',methods=['POST'])
def get_User_details():
    from webAppFunctions import webAppFunctions
    return webAppFunctions().getUserDetails(session['user']['_mailuid'],session['user']['_admin'])

@app.route('/signUp',methods=['POST'])
def signUp():
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()

    # read the posted values from the UI
    _firstname = request.form['inputFirstName']
    _secondname = request.form['inputSecondName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = hashpw(_password.encode('utf8'), gensalt())
 
    # validate the received values
    if _firstname and _secondname and _email and _password and _hashed_password:
        cursor.callproc('sp_createUser',(_firstname,_secondname,_email,_hashed_password))
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            data = {'message':'Signed up succesfully!','redirect':'/'}
            return json.dumps(data)
        else:
            data = {'error': 'Email already exists!'}
            return json.dumps(data)
    else:
        return json.dumps({'error':'Required fields have not been populated!'})

@app.route('/login',methods=['POST'])
def loginUser():
    import userUtils
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    user = userUtils.user()

    _email = request.form['inputEmail']
    _password = request.form['inputPassword'].encode('utf8')
   
    if user.checkIfDataNotEmpty(_email,_password) == True:
        
        if user.checkUser(_email, _password) == True or user.checkAdmin(_email, _password) == True:
            session['user'] = json.loads(user.getUserObject())
            print(session['user'])
            return json.dumps({'message':'Successfully logged you in!', 'redirect':'/menu'}) 
        else:
            return json.dumps({'error':'User not recognised or password incorrect!'}) 
        
    else:
        return json.dumps({'error':'Required fields have not been populated!'})

@app.route('/basket',methods=['POST'])
def basket():
    Prod_ID = 0
    Prod_QTY = 0
    Prod_Name = ""
    Prod_Price = 0.00
    client_data = request.get_json()
    Prod_ID = client_data['Product_ID']
    Prod_Name = client_data['Product_Name']
    Prod_Price = client_data['Product_Price']
    Prod_QTY = client_data['Product_QTY']
    
    if not Prod_ID and not Prod_QTY and not Prod_Name and not Prod_Price:
        return redirect(url_for('menu'))
    else:
        if not 'Order' in session:
            session['Order'] = []

        if len(session['Order']) < 4:
            main_order_list = session['Order']
            keys = ['Prod_ID', 'Prod_QTY', 'Prod_Name', 'Total']
            values = [int(Prod_ID),int(Prod_QTY), Prod_Name,round(int(Prod_QTY)*float(Prod_Price),2)]
            main_order_list.append(dict(zip(keys, values)))
            session['Order'] = main_order_list
            return redirect(url_for('menu'))
        else:
            return json.dumps({'error':'You cannot have more than 4 items in your basket at a given time!'})

@app.route('/orders')
def cus_orders():
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Order_ID, Order_Total, Table_No FROM ORDERS WHERE Order_Complete='N'")
    style_string = ""
    
    for row in cursor.fetchall():
        style_string += f"<div class='card' style='border-radius: 15px;'><center><div class='card-body'><h5 class='card-title'>ORDER {row[0]}<br><hr>Table {row[2]}<br><hr>Total (<b>&pound;{round(row[1],2)}</b>)<hr></h5>"
        style_string+=f"<span class='price-new'>{get_items_from_id(row[0])}</span></div></center></div>"

    cursor.close()
    conn.close()
    
    return render_template('orders.html', content=style_string)

def get_items_from_id(id):
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    style_string = ""
    sql = f"SELECT fk1_Product_ID, Quantity FROM ORDER_ITEMS WHERE fk2_Order_ID = {id}"
    print(sql)
    cursor.execute(f"SELECT fk1_Product_ID, Quantity FROM ORDER_ITEMS WHERE fk2_Order_ID = {id}")
    
    for row in cursor.fetchall():
        style_string += f"<p style='line-height: 0.5;'>{row[1]} x {get_product_name(row[0])}</p>"
        return style_string
    cursor.close()
    conn.close()

def get_product_name(id):
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()
    style_string = ""
    sql = f"SELECT Product_Name FROM PRODUCT WHERE Product_ID = {id}"
    print(sql)
    cursor.execute(f"SELECT Product_Name FROM PRODUCT WHERE Product_ID = {id}")
    row = cursor.fetchone()
    return row[0]
    cursor.close()
    conn.close()

@app.route('/finalizeOrder',methods=['POST'])
def final_Order():
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()

    time_stamp = datetime.now()
    client_data = request.get_json()
    Table = client_data['Table']
    ORDER_TOTAL = 0.00

    for i in session['Order']:
        ORDER_TOTAL = ORDER_TOTAL + i['Total']
    
    from webAppFunctions import webAppFunctions
    session['order_id'] = webAppFunctions().returnNextID()

    sql = f"INSERT INTO ORDERS (Order_ID, Order_Total, Table_No, Order_Timestamp, Order_Complete, fk1_User_ID, fk2_Staff_ID) VALUES (NULL,{round(ORDER_TOTAL,2)},{Table},'{time_stamp}', 'N', {session['user']['_userID']}, NULL)"
    cursor.execute(sql)
    conn.commit()

    for i in session['Order']:
        sql = f"INSERT INTO ORDER_ITEMS (Order_Items_ID, Quantity, fk1_Product_ID, fk2_Order_ID) VALUES (NULL,{i['Prod_QTY']},{i['Prod_ID']},{session['order_id']})"
        cursor.execute(sql)
        conn.commit()
    session['Ordered'] = True
    return json.dumps({'message':'Successfully ordered!', 'ID':session['order_id']})

@app.route('/remove_item',methods=['POST'])
def remove_item():
    Index_To_remove = None
    client_data = request.get_json()
    Index_To_remove = client_data.get('Index', None)
    
    if Index_To_remove is not None:
        if not 'Order' in session:
            session['Order'] = []

        del session['Order'][int(Index_To_remove)]
        session.modified = True
        print(f'removed index {Index_To_remove}')
        return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    url = '/menu'
    return render_template('menu.html', url=url)

if __name__ == "__main__":
    app.run(debug=True)