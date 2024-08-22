from capmonstercloudclient.requests.amazon_waf_proxyless_request import AmazonWafProxylessRequest
from capmonstercloudclient.requests.amazon_waf_request import AmazonWafRequest
from capmonstercloudclient.requests.base_request import BaseRequest
from capmonstercloudclient.requests.basilisk_custom_task_proxyless_request import (
    BasiliskCustomTaskProxylessRequest,
)
from capmonstercloudclient.requests.basilisk_custom_task_request import BasiliskCustomTaskRequest
from capmonstercloudclient.requests.data_dome_custom_task_request import DataDomeCustomTaskRequest
from capmonstercloudclient.requests.data_dome_custom_task_roxyless_request import (
    DataDomeCustomTaskProxylessRequest,
)
from capmonstercloudclient.requests.funcaptcha_complex_image_task import (
    FunCaptchaComplexImageTaskRequest,
)
from capmonstercloudclient.requests.funcaptcha_proxyless_request import FuncaptchaProxylessRequest
from capmonstercloudclient.requests.funcaptcha_request import FuncaptchaRequest
from capmonstercloudclient.requests.geetest_request import GeetestRequest
from capmonstercloudclient.requests.geetest_roxyless_request import GeetestProxylessRequest
from capmonstercloudclient.requests.hcaptcha_complex_image_task import (
    HcaptchaComplexImageTaskRequest,
)
from capmonstercloudclient.requests.hcaptcha_proxyless_request import HcaptchaProxylessRequest
from capmonstercloudclient.requests.hcaptcha_request import HcaptchaRequest
from capmonstercloudclient.requests.image_to_text_request import ImageToTextRequest
from capmonstercloudclient.requests.recaptcha_complex_image_task import (
    RecaptchaComplexImageTaskRequest,
)
from capmonstercloudclient.requests.recaptcha_v2_enterpise_proxyless_request import (
    RecaptchaV2EnterpriseProxylessRequest,
)
from capmonstercloudclient.requests.recaptcha_v2_enterpise_request import (
    RecaptchaV2EnterpriseRequest,
)
from capmonstercloudclient.requests.recaptcha_v2_proxyless_request import (
    RecaptchaV2ProxylessRequest,
)
from capmonstercloudclient.requests.recaptcha_v2_request import RecaptchaV2Request
from capmonstercloudclient.requests.recaptcha_v3_proxyless_request import (
    RecaptchaV3ProxylessRequest,
)
from capmonstercloudclient.requests.ten_di_custom_task_proxyless_request import (
    TenDiCustomTaskProxylessRequest,
)
from capmonstercloudclient.requests.ten_di_custom_task_request import TenDiCustomTaskRequest
from capmonstercloudclient.requests.turnstile_proxyless_request import TurnstileProxylessRequest
from capmonstercloudclient.requests.turnstile_request import TurnstileRequest


REQUESTS = [
    "RecaptchaV2EnterpriseRequest",
    "RecaptchaV2EnterpriseProxylessRequest",
    "RecaptchaV2ProxylessRequest",
    "RecaptchaV2Request",
    "RecaptchaV3ProxylessRequest",
    "ImageToTextRequest",
    "FuncaptchaProxylessRequest",
    "FuncaptchaRequest",
    "GeetestRequest",
    "GeetestProxylessRequest",
    "HcaptchaProxylessRequest",
    "HcaptchaRequest",
    "DataDomeCustomTaskRequest",
    "DataDomeCustomTaskProxylessRequest",
    "TenDiCustomTaskRequest",
    "TenDiCustomTaskProxylessRequest",
    "BasiliskCustomTaskRequest",
    "BasiliskCustomTaskProxylessRequest",
    "AmazonWafRequest",
    "AmazonWafProxylessRequest",
]

__all__ = [
    "RecaptchaV2EnterpriseRequest",
    "RecaptchaV2EnterpriseProxylessRequest",
    "RecaptchaV2ProxylessRequest",
    "RecaptchaV2Request",
    "RecaptchaV3ProxylessRequest",
    "ImageToTextRequest",
    "FuncaptchaProxylessRequest",
    "FuncaptchaRequest",
    "GeetestRequest",
    "GeetestProxylessRequest",
    "HcaptchaProxylessRequest",
    "HcaptchaRequest",
    "DataDomeCustomTaskRequest",
    "DataDomeCustomTaskProxylessRequest",
    "TenDiCustomTaskRequest",
    "TenDiCustomTaskProxylessRequest",
    "BasiliskCustomTaskRequest",
    "BasiliskCustomTaskProxylessRequest",
    "AmazonWafRequest",
    "AmazonWafProxylessRequest",
    "BaseRequest",
    "RecaptchaComplexImageTaskRequest",
    "HcaptchaComplexImageTaskRequest",
    "FunCaptchaComplexImageTaskRequest",
    "TurnstileRequest",
    "TurnstileProxylessRequest",
    "REQUESTS",
]
