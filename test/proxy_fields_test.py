import unittest

from capmonstercloudclient.requests.proxy_info import ProxyInfo


FIELDS = ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]


class ProxyFieldsTest(unittest.TestCase):
    proxyPort: int = 8000
    proxyType: str = "https"
    proxyAddress: str = "proxyAddress"
    proxyLogin: str = "proxyLogin"
    proxyPassword: str = "proxyPassword"

    def testFields(self):
        p = ProxyInfo(
            proxy_type=ProxyFieldsTest.proxyType,
            proxy_address=ProxyFieldsTest.proxyAddress,
            proxy_port=ProxyFieldsTest.proxyPort,
            proxy_login=ProxyFieldsTest.proxyLogin,
            proxy_password=ProxyFieldsTest.proxyPassword,
        )
        d = p.model_dump()
        for field in FIELDS:
            self.assertTrue(field in d, msg=f'Expected that "{field}" will be in {list(d.keys())}')


if __name__ == "__main__":
    unittest.main()
