import allure
from data import get_pet_endpoints
from src.assertions import Assertions
from src.http_methods import MyRequests
from http import HTTPStatus
from src.prepare_data.prepare_pet_data import PrepareData
from src.schemas import CreatePetSchemas
from src.validator import Validator
from generator.pet_generator import PetGenerator


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()
    pet_data = PrepareData()
    pet_generator = PetGenerator()

    def test_create_pet(self, get_test_name):
        # data = self.pet_data.get_pet_json()
        info = next(self.pet_generator.generate_pet(tags_count=2))
        data = self.pet_data.prepare_pet_json(info)
        response = self.request.post(url=self.url.create_pet, data=data)
        # self.assertions.assert_status_code(
        #     response=response,
        #     actual_status_code=HTTPStatus.OK,
        #     test_name=get_test_name
        # )
        # self.validator.validate_response(response=response, model=CreatePetSchemas.create_pet)
        print(response.text)
