import time
import json
import cherrypy


orders = []  # In-memory order storage


class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"message": "Hello World!"}
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_restaurant_menu(self):
        return {
            "menu": [
                {"item": "Pizza", "price": 10.99},
                {"item": "Burger", "price": 8.99},
                {"item": "Salad", "price": 6.99}
            ],
            "currency": "OMR",
            "menu_last_updated_epoch_time": 1775371081
        }
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def place_order(self, client_order):
        incoming_order = {"client_order": client_order}
        print(f"Received order: {incoming_order}")

        # Store the order in-memory
        orders.append(incoming_order)

        return {"status": "success", "message": "Order placed successfully!"}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def check_all_orders(self):
        return {"placed_orders": orders}

cherrypy.quickstart(HelloWorld(), '/', {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
    }
})