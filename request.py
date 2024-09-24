from __future__ import annotations
from typing import *
import httpx
from httpx import Proxy
from loguru import logger

from models import Proxies

class BypassRequest:
    def __init__(self):
        ...

    @staticmethod
    def custom_get_request(
            url: str,
            headers: dict | None = None,
            cookies: dict | None | httpx.Cookies = None,
            params: dict | None = None,
            proxies: dict | Proxies | None = None

    ) -> httpx.Response | None:
        """
        :param url: The URL of the resource to send the GET request to.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param cookies: Optional dictionary or RequestsCookieJar object containing cookies to include in the request.
        :param params: Optional dictionary of query parameters to include in the request.
        :return: Response object if the request is successful, None otherwise.
        """
        if proxies is not None:
            if isinstance(proxies, dict):
                proxies = Proxies(**proxies)

            # proxies = {
            #     "http://": f"http://{local_settings.http_proxy}",
            #     "https://": f"http://{local_settings.https_proxy}",
            # }
            proxies = {
                "http://": httpx.HTTPTransport(proxy=f"http://{proxies.http}"),
                "https://": httpx.HTTPTransport(
                    proxy=f"http://{proxies.https}"
                ),
            }
        else:
            proxies = None

        with httpx.Client(mounts=proxies, headers=headers, cookies=cookies) as client:
            for _ in range(3):
                try:
                    r = client.get(url, params=params)
                    return r
                except (
                        httpx.TimeoutException,
                        httpx.NetworkError,
                ):
                    logger.error("request failed")

        return None

    @staticmethod
    def custom_post_request(
            url: str,
            headers: dict | None = None,
            json: dict | None = None,
            data: dict | None = None,
            cookies: dict | None | httpx.Cookies = None,
            params: dict | None = None,
            proxies: dict | Proxies | None = None
    ) -> httpx.Response | None:
        """
        :param proxies:
        :param data:
        :param url: The URL to which the POST request is sent.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param json: Optional dictionary of JSON data to include in the request body.
        :param cookies: Optional dictionary or httpx cookies to include with the request.
        :param params: Optional dictionary of query string parameters to include in the request.
        :return: An `httpx.Response` object if the request is successful, otherwise `None`.
        """
        if proxies is not None:
            if isinstance(proxies, dict):
                proxies = Proxies(**proxies)

            # proxies = {
            #     "http://": f"http://{local_settings.http_proxy}",
            #     "https://": f"http://{local_settings.https_proxy}",
            # }
            proxies = {
                "http://": httpx.HTTPTransport(proxy=f"http://{proxies.http}"),
                "https://": httpx.HTTPTransport(
                    proxy=f"http://{proxies.https}"
                ),
            }
        else:
            proxies = None
        with httpx.Client(mounts=proxies, headers=headers, cookies=cookies) as client:
            for _ in range(3):
                try:
                    r = client.post(url, json=json, data=data, params=params)
                    return r
                except (
                        httpx.TimeoutException,
                        httpx.NetworkError,
                ):
                    logger.error("request failed")
