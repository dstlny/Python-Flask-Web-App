# Python-Flask-Web-App
Most current project. Experimenting with Flask, AJAX, Javascript, Bootstrap, JQuery and many other things. Is coming along nicely.

## Current Features:
- Responsive login and registration page
- Ability to change user password
- User/Admin login/registration capability
- Responsive home page. 
  - Is simplified and easier to access on smaller devices, and uses JQuery accordions to do this.
  - On desktops, products are displayed as 'Cards'
- Fetches data from MySQL database using Flasks inbuilt MySQL extension.
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
- Menu and overall website aesthetic is responsive.
  
 # Please be aware this is still a work-in-progress. This is still being built and will get better with time.
 
 Created: 21/07/19 | Updated: 23/07/19 by Luke Elam (dstlny)
