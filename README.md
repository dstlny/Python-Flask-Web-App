# Python-Flask-Web-App
Most current project. Experimenting with Flask, AJAX, Javascript, Bootstrap, JQuery and many other things. Is coming along nicely.

## Current Features:
- User/Admin login/registration capability
  - Ability to change user password
- Website is responsive in nature.
  - Is simplified and easier to access on smaller devices, uses JQuery accordions to do this.
  - On desktops, products are displayed as 'Cards'.
- Fetches data from MySQL database using Flasks inbuilt MySQL extension, thus this site uses MySQL - i was/is using PHPMyAdmin during development.
  - All passwords are encrypted using Bcrypt, making use of bcrypt's native hashpw() and checkpw() methods.
- JSON is mainy used to communicate between backend and front-end.
  - Making use of AJAX to POST/GET requests from the server.
- Staff page is now implemented
  - This is done entirely on the servers side, as we don't want to trust anybody with the order-data, thus no JSON is sent to or from.
- User-basket has been implemented
  - Includes Total with VAT, without VAT and per-product breakdown.
  - Table selection, is also included.
  - Once the user has ordered, the confirmation button is disabled.
    - Users can remove specific products.

## Installation
- git clone https://github.com/dstlny/Python-Flask-Web-App.git
- cd Python-Flask-Web-App
- pip install -r requirements.txt
  
 ## Some comments
 - SQL data used during development has been dumped to SQL/Python_Flask_Web_App.sql, this gives you an idea of how the database is laid out, and gives you a starting point.
   - Comments embedded within this SQL script tell you the default user/staff password.
   - You will want to change the MySQL configuration inside of App.py to fit your needs.
   
 
 # Please be aware this is still a work-in-progress. This is still being built and will get better with time.
 
 Created: 21/07/19 | Updated: 28/07/19 by Luke Elam (dstlny)
