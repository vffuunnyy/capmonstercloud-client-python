import asyncio
import os
import unittest

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import GeetestProxylessRequest


def solve(client: CapMonsterClient, request: GeetestProxylessRequest):
    return asyncio.run(client.solve_captcha(request))


class GeeTestIntegrationTest(unittest.TestCase):
    api_key = os.getenv("API_KEY")
    client_options = ClientOptions(api_key=api_key)
    cap_monster_client = CapMonsterClient(options=client_options)

    def test_check_response_outputs(self):
        required_keys = ["captcha_id", "lot_number", "pass_token", "gen_time", "captcha_output"]
        geetest_request = GeetestProxylessRequest(
            websiteUrl="https://faucetpay.io/account/login",
            gt="4eb8b0c2b27f3365b9244d9da81638c6",
            version=4,
            initParameters={"riskType ": "slide"},
        )
        response = solve(self.cap_monster_client, geetest_request)
        for key in required_keys:
            self.assertTrue(
                key in list(response.keys()),
                msg=f'Required captcha output key "{key}" doesnt include to response.',
            )


if __name__ == "__main__":
    unittest.main()
