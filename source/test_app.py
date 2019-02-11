from app import app
import unittest


class PageReachability(unittest.TestCase):
    def test_cisco_api_using_responsecode(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory', content_type='html/test')
        self.assertEqual(response.status_code, 200)

    def test_cisco_api_using_response_returned(self):
        test = app.test_client(self)
        response = test.get('/cisco/api/advisory', content_type='html/test')
        self.assertTrue(b'advisories' in response.data)


if __name__ == '__main__':
    unittest.main()
