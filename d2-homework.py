#Для получения переменных из окружения, импортируем модуль os, 
#потом импортируем код, необходимый для запуска Bottle приложения, 
#а после этого импортируем вещи, необходимые для интеграции с Sentry.
#При инициализации sentry_sdk передаём строку dsn, получая её значение из переменной окружения SENTRY_DSN.

import os
from bottle import Bottle, request  
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  
  
sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])  
  
app = Bottle()  

@app.route('/success') 
def success():
    return    

@app.route('/fail') 
def fail():    
    raise RuntimeError("There is an error!")
    
app.run(host='localhost', port=8080)