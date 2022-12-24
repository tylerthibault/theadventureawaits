from flask_app import app
from flask_app.controllers import order_contents_controller, user_controller, routes_controller, product_controller, category_controller, order_controller, address_controller, config_controller

if __name__=="__main__":
    app.run(debug=True)