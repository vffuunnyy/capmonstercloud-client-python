from enum import StrEnum, unique


@unique
class TextModules(StrEnum):
    amazon_captcha = "amazon"
    botdetect_captcha = "botdetect"
    facebook_captcha = "facebook"
    gmx_captcha = "gmx"
    google_captcha = "google"
    hotmail_captcha = "hotmail"
    mailru_captcha = "mailru"
    ok_captcha = "ok"
    oknew_captcha = "oknew"
    ramblerrus_captcha = "ramblerrus"
    solvemedia_captcha = "solvemedia"
    steam_captcha = "steam"
    vk_captcha = "vk"
    yandex_captcha = "yandex"
    yandexnew_captcha = "yandexnew"
    yandexwave_captcha = "yandexwave"
    universal_captcha = "universal"


@unique
class ProxyTypes(StrEnum):
    http_proxy = "http"
    https_proxy = "https"
    socks4_proxy = "socks4"
    socks5_proxy = "socks5"
