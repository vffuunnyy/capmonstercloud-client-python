from capmonstercloudclient.requests.amazon_waf_request_base import AmazonWafRequestBase


class AmazonWafProxylessRequest(AmazonWafRequestBase):
    type: str = "AmazonTaskProxyless"

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "challengeScript": self.challenge_script,
            "captchaScript": self.captcha_script,
            "websiteKey": self.website_key,
            "context": self.context,
            "iv": self.iv,
        }

        if self.cookie_solution is not None:
            task["cookieSolution"] = self.cookie_solution
        return task
