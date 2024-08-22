import asyncio
import base64
import os
import time
import urllib

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaComplexImageTaskRequest


def read_image(
    image_url: str,
):
    image_bytes = urllib.request.urlopen(image_url).read()
    return base64.b64encode(image_bytes).decode("utf-8")


async def solve_captcha_sync(num_requests, client, request):
    return [await client.solve_captcha(request) for _ in range(num_requests)]


async def solve_captcha_async(num_requests, client, request):
    tasks = [asyncio.create_task(client.solve_captcha(request)) for _ in range(num_requests)]
    return await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36."
    metadata = {"Task": "Click on traffic lights", "Grid": "3x3", "TaskDefinition": "/m/015qff"}
    imagesUrls = ["https://i.postimg.cc/yYjg75Kv/payloadtraffic.jpg"]
    imagesBase64 = [read_image(x) for x in imagesUrls]

    options = ClientOptions(api_key=api_key)
    client = CapMonsterClient(options)

    # urls example
    request_with_urls = RecaptchaComplexImageTaskRequest(metadata=metadata, imagesUrls=imagesUrls)
    request_with_b64 = RecaptchaComplexImageTaskRequest(
        metadata=metadata, imagesBase64=imagesBase64
    )

    nums = 3

    print(" Test with urls ".center(120, "#"))

    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums, client, request_with_urls))
    print(
        f"average execution time sync {1 / ((time.time() - sync_start) / nums):0.2f} "
        f"resp/sec\nsolution: {sync_responses[0]}"
    )

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums, client, request_with_urls))
    print(
        f"average execution time async {1 / ((time.time() - async_start) / nums):0.2f} "
        f"resp/sec\nsolution: {async_responses[0]}"
    )

    print(" Test with images base64 ".center(120, "#"))

    # Sync test
    sync_start = time.time()
    sync_responses = asyncio.run(solve_captcha_sync(nums, client, request_with_b64))
    print(
        f"average execution time sync {1 / ((time.time() - sync_start) / nums):0.2f} "
        f"resp/sec\nsolution: {sync_responses[0]}"
    )

    # Async test
    async_start = time.time()
    async_responses = asyncio.run(solve_captcha_async(nums, client, request_with_b64))
    print(
        f"average execution time async {1 / ((time.time() - async_start) / nums):0.2f} "
        f"resp/sec\nsolution: {async_responses[0]}"
    )
