import requests
import json

# Get Data

# def get_data(id=None):
#     URL = "http://127.0.0.1:8000/student/"
#     data={}
#     if id is not None:
#         data={"id":id}
#     json_data=json.dumps(data)
#     r=requests.get(url=URL, data=json_data)
#     print(r)
#     data=r.json()
#     print(data)
# get_data()

# def post_data():
#     URL = "http://127.0.0.1:8000/student/"


#     data = {
#         "id":5,
#         "name":"Meera",
#         "roll":105,
#         "city":"Dubai"
#     }

#     headers={'content-type':'application/json'}

#     json_data=json.dumps(data)
#     r = requests.post(url=URL, headers=headers, data=json_data)
#     data=r.json()
#     print(data)
# post_data()

# def update_data():
#     URL = "http://127.0.0.1:8000/getstudent/"

#     data = {
#         "id":5,
#         "name":"Meera",
#         "roll":105,
#         "city":"Copenhagen"
#     }

#     headers={'content-type':'application/json'}

#     json_data=json.dumps(data)
#     r = requests.put(url=URL, headers=headers, data=json_data)
#     data=r.json()
#     print(data)
# update_data()


# def delete_data():
#     URL = "http://127.0.0.1:8000/getstudent/"
#     data = {"id":6}
#     headers={'content-type':'application/json'}
#     json_data=json.dumps(data)
#     r = requests.delete(url=URL, headers=headers, data=json_data)
#     data=r.json()
#     print(data)
# delete_data()