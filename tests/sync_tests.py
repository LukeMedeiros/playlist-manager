import unittest
import routes.sync as sync

class SyntTest(unittest.TestCase):

    def test_validate_params_valid_id(self):
        id = "123" 
        streaming_services = "youtube,deezer"
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("valid", result)

    def test_validate_params_invalid_id(self):
        id = None 
        streaming_services = "youtube,deezer"
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("invalid id", result)

    def test_validate_params_empty_id(self):
        id = "" 
        streaming_services = "youtube,deezer"
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("invalid id", result)

    def test_validate_params_valid_services(self):
        id = "123" 
        streaming_services = "youtube"
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("valid", result)

    def test_validate_params_invalid_services(self):
        id = "123" 
        # no spaces are allowed
        not_found = "not found" 
        streaming_services = "youtube," + not_found
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("invalid streaming service: " + not_found, result)

    def test_validate_params_root_service_included(self):
        id = "123" 
        streaming_services = "youtube,spotify"
        root_service = "spotify"
        result = sync.validate_params(id, streaming_services, root_service)
        self.assertEqual("root service cannot be synced", result)



if __name__ == '__main__':
    unittest.main()