import requests

updated_payload = {
   "name": "Test Object3",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}


def test_create_object(create_object):
    response = create_object
    assert "id" in response
    assert response["name"] == "Apple MacBook Pro 18"

def test_get_object(base_url, create_object):
    #Get All Objects
    new_response = requests.get(f"{base_url}/objects")
    assert new_response.status_code == 200
    data = new_response.json()
    #print("Total Number of objects: ", len(data))
    #print("Retrived Data: ", data)

def test_update_object(base_url, create_object):
    object_id = create_object["id"]
    #Update Object
    new_response = requests.put(f"{base_url}/objects/{object_id}", json=updated_payload)
    #print("Updated Object: ", new_response.text)
    assert new_response.status_code == 200
    updated_data = new_response.json()
    assert updated_data["name"] == "Test Object3"

def test_delete_object(base_url, create_object):
    object_id = create_object["id"]
    #Delete Object by ID
    new_response =  requests.delete(f"{base_url}/objects/{object_id}")
    #print("Delete Response:", new_response.text)
    assert new_response.status_code == 200
    #Get object and check status code is 404
    get_response = requests.get(f"{base_url}/objects/{object_id}")
    #print("Get after Delete:", get_response.text)
    assert get_response.status_code == 404