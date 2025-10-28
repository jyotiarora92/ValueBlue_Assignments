import requests
import pytest


@pytest.fixture()
def base_url():
    #Base URL for all API tests
    return "https://api.restful-api.dev"

@pytest.fixture()
def sample_payload():
    #Default Test Data for object creation
    return  {
   "name": "Apple MacBook Pro 18",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
    
@pytest.fixture()
def create_object(base_url, sample_payload):
    #Create a test object for each test and deletes it after
    response = requests.post(f"{base_url}/objects", json=sample_payload)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    obj = response.json()

    #Provide object to test
    yield obj 

    #Cleanup
    requests.delete(f"{base_url}/objects/{obj['id']}")