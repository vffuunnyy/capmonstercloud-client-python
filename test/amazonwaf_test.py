import unittest

from pydantic.error_wrappers import ValidationError

from capmonstercloudclient.requests import AmazonWafProxylessRequest


class AmazonWafRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "189123456"
    challengeScriptExample = "challenge_test"
    captchaScriptExample = "123"
    contextExample = "context"
    ivExample = "ivexample_`¬"

    def testCaptchaInputTypes(self):
        with self.assertRaises(ValidationError):
            request = AmazonWafProxylessRequest(website_url=AmazonWafRequestTest.websiteUrlExample)

        with self.assertRaises(ValidationError):
            request = AmazonWafProxylessRequest(
                website_key=AmazonWafRequestTest.websiteKeyExample,
            )
        with self.assertRaises(ValidationError):
            request = AmazonWafProxylessRequest(
                website_url=AmazonWafRequestTest.websiteUrlExample,
                website_key=AmazonWafRequestTest.websiteKeyExample,
                challenge_script=AmazonWafRequestTest.challengeScriptExample,
                captcha_script=int(AmazonWafRequestTest.captchaScriptExample),
                context=AmazonWafRequestTest.contextExample,
                iv=AmazonWafRequestTest.ivExample,
            )

        request = AmazonWafProxylessRequest(
            website_url=AmazonWafRequestTest.websiteUrlExample,
            website_key=AmazonWafRequestTest.websiteKeyExample,
            challenge_script=AmazonWafRequestTest.challengeScriptExample,
            captcha_script=AmazonWafRequestTest.captchaScriptExample,
            context=AmazonWafRequestTest.contextExample,
            iv=AmazonWafRequestTest.ivExample,
        )

    def testAllRequiredFieldsFilling(self):
        required_fields = [
            "websiteURL",
            "type",
            "websiteKey",
            "challengeScript",
            "captchaScript",
            "context",
            "iv",
        ]
        request = AmazonWafProxylessRequest(
            website_url=AmazonWafRequestTest.websiteUrlExample,
            website_key=AmazonWafRequestTest.websiteKeyExample,
            challenge_script=AmazonWafRequestTest.challengeScriptExample,
            captcha_script=AmazonWafRequestTest.captchaScriptExample,
            context=AmazonWafRequestTest.contextExample,
            iv=AmazonWafRequestTest.ivExample,
            cookie_solution=True,
        )
        request_dict = request.get_task_dict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()), msg=f"Required field {i} not in {request_dict}"
            )

        self.assertEqual(request_dict["type"], "AmazonTaskProxyless")


if __name__ == "__main__":
    unittest.main()
