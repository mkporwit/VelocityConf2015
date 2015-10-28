import unittest
import urllib

#URL_TO_TEST = 'https://example.com/'
URL_TO_TEST = 'http://www.porwit.com/'

class TestSecurityHeaders(unittest.TestCase):
    """
    Tests for security headers based on the recommendations
    from https://securityheaders.com/
    """
    def setUp(self):
        self.response = urllib.urlopen(URL_TO_TEST)

    def test_valid_response(self):
        self.assertEqual(self.response.code, 200)

    def test_for_a_content_security_policy(self):
        self.assertTrue('content-security-policy' in self.response.headers.keys())

    def test_for_a_strict_transport_security_policy(self):
        self.assertTrue('strict-transport-security' in self.response.headers.keys())

    def test_not_revealing_powered_by_technology(self):
        self.assertFalse('x-powered-by' in self.response.headers.keys())

    def test_not_revealing_server_technology(self):
        self.assertFalse('server' in self.response.headers.keys())

    def test_not_allowing_anyone_to_load_content(self):
        header = self.response.headers.get('access-control-allow-origin')
        self.assertNotEqual(header, '*')

    def test_for_a_sensible_xss_policy(self):
        header = self.response.headers.get('x-xss-protection')
        self.assertEqual(header, '1; mode=block')

    def test_for_clickjacking_protection(self):
        header = self.response.headers.get('x-frame-options')
        self.assertEqual(header, 'SAMEORIGIN')

    def test_for_mime_guessing_disabled(self):
        header = self.response.headers.get('x-content-type-options')
        self.assertEqual(header, 'nosniff')

    def test_preventing_cross_domain_loading(self):
        header = self.response.headers.get('x-permitted-cross-domain-policies')
        self.assertEqual(header, 'master-only')


if __name__ == '__main__':
    unittest.main()
