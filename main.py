# -*- coding:utf8 -*-
from suds.client import Client
import json

if __name__ == "__main__":
    # client = Client("http://%s:%s/?wsdl" % ('127.0.0.1','8080'))
    client = Client("http://127.0.0.1:8080/?wsdl")

    print(client)

    result = client.service.make_project(u"ABC")
    print(result)


    person = client.factory.create("Person")
    person.name = "John"
    person.age = "18"

    Person2 = client.service.make_project_comlex(u"qjh")
    print(Person2)


    myJson = json.dumps({'a': 'qjh', 'b': 7}, sort_keys=True, indent=4, separators=(',', ':'))
    client.service.make_project_Json(myJson)
