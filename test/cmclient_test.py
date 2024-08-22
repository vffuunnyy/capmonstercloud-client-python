import asyncio
import os
import unittest

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.exceptions import UnknownRequestInstanceError
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest


api_key = os.getenv("API_KEY")


class InstanceRequestTest(unittest.IsolatedAsyncioTestCase):
    def testSuccessResponse(self):
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        request = RecaptchaV2ProxylessRequest(
            websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
            websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
        )
        # Success
        response_1 = asyncio.run(client.solve_captcha(request))
        self.assertTrue(isinstance(response_1, dict))

    def testFailedInstanceRequest(self):
        options = ClientOptions(api_key=api_key)
        client = CapMonsterClient(options=options)
        # Failed
        with self.assertRaises(
            UnknownRequestInstanceError,
            msg="Unknown instance of request must call <UnknownRequestInstanceError>.",
        ):
            asyncio.run(client.solve_captcha("hmmm"))


if __name__ == "__main__":
    unittest.main()
