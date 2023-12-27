from tools              import *
from flask              import Flask, request
from flask_swagger_ui   import get_swaggerui_blueprint

app = Flask(__name__)

# ---------------- Swagger ----------------------------------------------------------------------------------
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(  SWAGGER_URL,
                                                API_URL,
                                                config={'app_name': "Test application"})
app.register_blueprint(swaggerui_blueprint)

# ------------------------ application area ------------------------
@app.route('/',methods=['POST', 'GET'])
def index():
    return 'Running OK!!!!'

# ----------------------- Broker --------------------------------
@app.route('/brokerInfo/insert',methods=['POST'])
def brokerInfoInsert():
    content     = request.get_json()
    username    = content['username']
    firstName   = content['firstName']
    lastName    = content['lastName']
    brach       = content['brach']
    phone       = content['phone']
    email       = content['email']
    password    = content['password']
    
    if duplicate_email(email):
        return {'responses': 'This email was used'}
    else:
        adding_data = { "username":     username, 
                        "firstName":    firstName,
                        "lastName":     lastName,
                        "brach":        brach,
                        "phone":        phone, 
                        "email":        email,
                        "password":     password}
        broker_id   = insert_data("broker_info", adding_data)
        return {'broker_id': broker_id}

@app.route('/brokerInfo/<broker_id>',methods=['GET'])
def brokerInfo(broker_id):
    broker_data = query_data_by_id("broker_info", f'{broker_id}')
    basket_data = query_data("car_info", "broker_id", broker_id)
    basket_data_need = []
    for basket in basket_data:
        info = {'basket_id':    str(basket['_id']),
                'brand':        basket['brand'],
                'status':       basket['status']}
        basket_data_need.append(info)
    data        = { "username":     broker_data['username'], 
                    "firstName":    broker_data['firstName'],
                    "lastName":     broker_data['lastName'],
                    "brach":        broker_data['brach'],
                    "phone":        broker_data['phone'], 
                    "email":        broker_data['email'],
                    "baskets":      basket_data_need}    
    return data

@app.route('/brokerInfo/update',methods=['POST'])
def brokerInfoUpdate():
    content     = request.get_json()
    email       = content['email']
    colname     = content['colname']
    change_data = content['change_data']
    update_data("broker_info", "email", email, colname, change_data)
    return {'responses': f"Broker's {colname} was updated"}

@app.route('/brokerDelete/<broker_id>',methods=['GET'])
def brokerDelete(broker_id):
    delete_data_by_id("broker_info", f'{broker_id}') 
    busket = update_data("car_info", "broker_id", broker_id, 'status', 'inactive')
    return {'responses': f'This broker was deleted and {busket} busket(s) are inactive'}

# ----------------------- Car --------------------------------
@app.route('/carInfo/insert',methods=['POST'])
def carInfoInsert():
    content         = request.get_json()
    brand           = content['brand']
    model           = content['model']
    year            = content['year']
    coluer          = content['coluer']
    mileage         = content['mileage']
    price           = content['price']
    images          = content['image_url']
    status          = content['status']
    broker_mail     = content['broker_mail']
    
    if duplicate_email(broker_mail):
        broker_data = query_data("broker_info", 'email', broker_mail)
        broker_id   = str(broker_data[0]['_id'])
        adding_data = { "brand":        brand, 
                        "model":        model,
                        "year":         year,
                        "coluer":       coluer,
                        "mileage":      mileage, 
                        "price":        price,
                        "images":       images,
                        "status":       status,
                        "broker_id":    broker_id}
        busket_id   = insert_data("car_info", adding_data)
        return {'busket_id': busket_id}
    else:
        return {'responses': 'Email invalid'}

@app.route('/carInfo/<basket_id>',methods=['GET'])
def carInfo(basket_id):
    basket_data = query_data_by_id("car_info", f'{basket_id}')
    data        = { "brand":    basket_data['brand'], 
                    "model":    basket_data['model'],
                    "year":     basket_data['year'],
                    "coluer":   basket_data['coluer'],
                    "mileage":  basket_data['mileage'], 
                    "price":    basket_data['price'],
                    "images":   basket_data['images'],
                    "status":   basket_data['status']}    
    return data

@app.route('/carInfo/update',methods=['POST'])
def carInfoUpdate():
    content     = request.get_json()
    basket_id   = content['basket_id']
    colname     = content['colname']
    change_data = content['change_data']
    update_data("car_info", "_id", ObjectId(basket_id), colname, change_data)
    return {'responses': f"Car's {colname} was updated"}

@app.route('/carDelete/<basket_id>',methods=['GET'])
def CarDelete(basket_id):
    delete_data_by_id("car_info", f'{basket_id}') 
    return {'responses': f'This basket was deleted '}

# --------------- listing ---------------------------------
@app.route('/showBasket',methods=['GET'])
def showBasket():
    basket_data = query_data("car_info")
    basket_data_need = []
    for basket in basket_data:
        info = {'basket_id':    str(basket['_id']),
                'brand':        basket['brand'],
                'status':       basket['status']}
        basket_data_need.append(info)
    return {'responses': basket_data_need}

## ------------------------ main ------------------------
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
    


