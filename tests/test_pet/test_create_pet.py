import allure
from data import get_pet_endpoints
from src.assertions import Assertions
from src.http_methods import MyRequests
from http import HTTPStatus


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()

    def test_create_pet(self, get_test_name):
        data = """{
            "id": 12999,
            "category": {
                "id": 0,
                "name": "string77777"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 5555,
                    "name": "string"
                }
            ],
            "status": "available"
        }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.CREATED,
            test_name=get_test_name
        )
        print(response.status_code)
