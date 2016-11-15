#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
from random import randint


urls = (
    '/getTemperatura', 'Temperatura',
    '/setTemperatura', 'Temperatura',
)

app = web.application(urls, globals())
temperatura = 0

class Temperatura:        
    temperatura = 0

    def GET(self):
        return str(Temperatura.temperatura)

    def POST(self):
        Temperatura.temperatura = randint(0,45)
    
if __name__ == "__main__":
    app.run()
