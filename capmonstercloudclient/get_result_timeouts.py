from dataclasses import dataclass


@dataclass
class GetResultTimeouts:
    first_request_delay: int | float
    first_request_no_cache_delay: int | float
    requests_interval: int | float
    timeout: int | float


def get_recaptcha_v2_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)


def get_recaptcha_v2_enterprise_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)


def get_recaptcha_v3_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)


def get_image2_text_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(0.35, 0, 0.2, 10)


def get_funcaptcha_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 1, 80)


def get_hcaptcha_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)


def get_geetest_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)


def get_turnstile_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)


def get_datadome_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 0, 1, 80)


def get_ten_di_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)


def get_basilisk_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 100)


def get_amazon_waf_timeouts() -> GetResultTimeouts:
    return GetResultTimeouts(1, 10, 3, 180)
