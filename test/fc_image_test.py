import unittest

from pydantic.error_wrappers import ValidationError

from capmonstercloudclient.exceptions import (
    NumbersImagesErrors,
    TaskNotDefinedError,
    UserAgentNotDefinedError,
    ZeroImagesErrors,
)
from capmonstercloudclient.requests import FunCaptchaComplexImageTaskRequest


class RecaptchaImageRequestTest(unittest.TestCase):
    websiteUrlExample = "https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=middle"
    imageUrlsExamples = ["https://i.postimg.cc/s2ZDrHXy/fc1.jpg"]
    metadataExample = {"Task": "Pick the image that is the correct way up"}

    def testImagesTypes(self):
        with self.assertRaises(ValidationError):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64="[]",
            )

        with self.assertRaises(ValidationError):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls="[]",
            )

    def testImagesFilling(self):
        with self.assertRaises(
            ZeroImagesErrors, msg="Empty array imagesUrls must be cause ZeroImagesErrors"
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=[],
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

        with self.assertRaises(
            ZeroImagesErrors, msg="Empty array imagesBase64 must be cause ZeroImagesErrors"
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64=[],
            )

        with self.assertRaises(
            ZeroImagesErrors,
            msg="Both empty arrays imagesBase64 and imagesUrls must be cause ZeroImagesErrors",
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
            )
            request.get_task_dict()

    def testNumbersImages(self):
        with self.assertRaises(
            NumbersImagesErrors, msg="Empty array must be cause ZeroImagesErrors"
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples * 2,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

        with self.assertRaises(
            NumbersImagesErrors, msg="Empty array must be cause ZeroImagesErrors"
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesBase64=["base64image"] * 2,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

    def testAllRequiredFieldsFilling(self):
        required_fields = ["class", "type", "websiteUrl", "metadata", "userAgent"]
        metadata_fields = ["Task"]
        request = FunCaptchaComplexImageTaskRequest(
            websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
            metadata=RecaptchaImageRequestTest.metadataExample,
            imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
        )
        request_dict = request.get_task_dict()
        for i in required_fields:
            self.assertTrue(
                i in list(request_dict.keys()), msg=f"Required field {i} not in {request_dict}"
            )

        metadata_dict = request_dict["metadata"]
        for i in metadata_fields:
            self.assertTrue(
                i in list(metadata_dict.keys()), msg=f"Required field {i} not in {request_dict}"
            )

        self.assertEqual(request_dict["class"], "funcaptcha")
        self.assertEqual(request_dict["type"], "ComplexImageTask")

    def testTaskDefined(self):
        with self.assertRaises(
            TaskNotDefinedError,
            msg='Expect that empty "Task" field will be cause TaskNotDefinedError',
        ):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata={},
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            )

        with self.assertRaises(TaskNotDefinedError):
            request = FunCaptchaComplexImageTaskRequest(
                websiteUrl=RecaptchaImageRequestTest.websiteUrlExample,
                metadata={"dsfsdf": "sdfsdf"},
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.",
            )

    @unittest.skip("Doesnt work right now")
    def testUserAgentWithUrl(self):
        with self.assertRaises(UserAgentNotDefinedError):
            request = FunCaptchaComplexImageTaskRequest(
                metadata=RecaptchaImageRequestTest.metadataExample,
                imagesUrls=RecaptchaImageRequestTest.imageUrlsExamples,
            )
            request.get_task_dict()


if __name__ == "__main__":
    unittest.main()
