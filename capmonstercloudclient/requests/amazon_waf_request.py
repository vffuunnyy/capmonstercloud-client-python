from capmonstercloudclient.requests.amazon_waf_request_base import AmazonWafRequestBase
from capmonstercloudclient.requests.proxy_info import ProxyInfo


class AmazonWafRequest(AmazonWafRequestBase, ProxyInfo):
    type: str = "AmazonTask"

    def get_task_dict(self) -> dict[str, str | int | bool]:
        task = {
            "type": self.type,
            "websiteURL": self.website_url,
            "challengeScript": self.challenge_script,
            "captchaScript": self.captcha_script,
            "websiteKey": self.website_key,
            "context": self.context,
            "iv": self.iv,
            "proxyType": self.proxy_type,
            "proxyAddress": self.proxy_address,
            "proxyPort": self.proxy_port,
            "proxyLogin": self.proxy_login,
            "proxyPassword": self.proxy_password,
        }

        if self.cookie_solution is not None:
            task["cookieSolution"] = self.cookie_solution
        return task
