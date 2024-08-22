import asyncio
import os
import time

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import TurnstileProxylessRequest


async def solve_captcha(
    client: CapMonsterClient, request: TurnstileProxylessRequest, num_requests: int
) -> dict:
    return [await client.solve_captcha(request) for _ in range(num_requests)]


async def solve_captcha_async(
    client: CapMonsterClient, request: TurnstileProxylessRequest, num_requests: int
) -> dict:
    tasks = [asyncio.create_task(client.solve_captcha(request)) for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    num_requests = 3
    api_key = os.getenv("API_KEY")
    client_options = ClientOptions(api_key=api_key)
    client = CapMonsterClient(client_options)

    turnstile_request = TurnstileProxylessRequest(
        websiteURL="http://tsmanaged.zlsupport.com/", websiteKey="0x4AAAAAAABUYP0XeMJF0xoy"
    )

    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha(client, turnstile_request, num_requests))
    print(
        f"average execution time sync {1 / ((time.time() - sync_start) / num_requests):0.2f} "
        f"resp/sec\nsolution: {sync_responses[0]}"
    )

    async_start = time.time()
    sync_responses = asyncio.run(solve_captcha_async(client, turnstile_request, num_requests))
    print(
        f"average execution time async {1 / ((time.time() - async_start) / num_requests):0.2f} "
        f"resp/sec\nsolution: {sync_responses[0]}"
    )
