import json
from functions import get_json_data
from src.prepare_data.prepare_basic_data import BaseTestData
from data.pet_data_class import PetDataClass
from src.schemas.pet_request_schema import PetRequestSchema


class PrepareData(BaseTestData):
    # def get_pet_json(self):
    #     json_data = get_json_data("pet_data.json")
    #     return json.dumps(json_data)

    def prepare_pet_json(self, info: PetDataClass, key=None):
        # data = {
        #     "id": info.uid,
        #     "name": info.name,
        #     "category": info.category,
        #     "photoUrls": info.photo_urls,
        #     "tags": info.tags,
        #     "status": info.status
        #
        #
        # }
        # if key is not None:
        #     data.pop(key, None)
        # return self.format_data_as_json(data)
        data = PetRequestSchema(
            id=info.uid,
            name=info.name,
            category=info.category,
            photoUrls=info.photo_urls,
            tags=info.tags,
            status=info.status

        )
        self.attach_request(data)
        return data.model_dump_json(

        )

# data = """{
#             "id": 1289999,
#             "category": {
#                 "id": 0,
#                 "name": "string77777"
#             },
#             "name": "doggie",
#             "photoUrls": [
#                 "string"
#             ],
#             "tags": [
#                 {
#                     "id": 5555,
#                     "name": "string"
#                 }
#             ],
#             "status": "available"
#         }"""
