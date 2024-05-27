import requests

# response = requests.post(
#
#     url="https://petstore.swagger.io/v2/pet",
#
#     headers={
#         "api_key": "special-key"
#     },
#
#     json={
#         "id": 222,
#         "category": {
#             "id": 0,
#             "name": "string"
#         },
#         "name": "Bimba",
#         "photoUrls": [
#             "string"
#         ],
#         "tags": [
#             {
#                 "id": 0,
#                 "name": "dog"
#             }
#         ],
#         "status": "available"
#
#
#     }
#
# )
#
# print(response.json())

# get_pet_by_id = requests.get(
#     url="https://petstore.swagger.io/v2/pet/222",
#     headers={
#         "api_key": "special-key"
#     },
#
# )
#
# print(get_pet_by_id.json())

upload_img = requests.post(
    url="https://petstore.swagger.io/v2/pet/222/uploadImage",
    headers={
        "api_key": "special-key"
    },
    files={
        "file": ("images.jpg", open("images.jpg", "rb"),"image/jpeg")
    }

)
print(upload_img.status_code)
print(upload_img.json())