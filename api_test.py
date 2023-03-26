import unittest, requests, os

class api_test(unittest.TestCase):
    get_uri = os.environ.get("KUBE_URI")
    uri = f"http://{get_uri}:5000/liatrio"


    def test_response(self):
        response = requests.get(self.uri)
        self.assertEqual(response.status_code, 200)
        print('#####################################################')
        print("Test 1 is successful. Receiving back 200 codes.")
        print('#####################################################\n')

    def test_len(self):
        response = requests.get(self.uri)
        self.assertEqual(len(response.json()), 2)
        print('#####################################################')
        print("Test 2 is successful. Identified 2 values in json.")
        print('#####################################################')
        print(response.json())
        print('####################################################')

if __name__ == "__main__":
    test = api_test()

    test.test_response()
    test.test_len()