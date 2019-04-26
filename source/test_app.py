from app import app
import unittest


class PageReachability(unittest.TestCase):
    def test_dummy_api_regular_response_by_status_code(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory', content_type='html/test')
        self.assertEqual(response.status_code, 200)

    def test_dummy_api_regular_response_by_response_date(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory', content_type='html/test')
        self.assertTrue(b'advisories' in response.data)

    def test_dummy_api_all_response_by_status_code(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory/all', content_type='html/test')
        self.assertEqual(response.status_code, 200)

    def test_dummy_api_all_response_by_response_date(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory/all', content_type='html/test')
        self.assertTrue(b'advisories' in response.data)

    def test_dummy_api_no_new_response_by_status_code(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory/nonew', content_type='html/test')
        self.assertEqual(response.status_code, 406)

    def test_dummy_api_no_response_by_response_date(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory/nonew', content_type='html/test')
        self.assertTrue(b'NO_DATA_FOUND' in response.data)


if __name__ == '__main__':
    unittest.main()
