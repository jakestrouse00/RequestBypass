from __future__ import annotations
from typing import *
import httpx
from httpx import Proxy
from loguru import logger
import hrequests
from models import Proxies
import requests
from requests.exceptions import *
from hrequests.cookies import RequestsCookieJar


class BypassRequest:
    def __init__(self):
        ...

    @staticmethod
    def get(
            url: str,
            headers: dict | None = None,
            cookies: dict | None | RequestsCookieJar = None,
            params: dict | None = None,
            proxy: str | Proxies | None = None,
            retries: int = 3,
            nowait: bool = False

    ) -> requests.Response | None:
        """
        :param nowait:
        :param url: The URL to send the GET request to.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param cookies: Optional dictionary or RequestsCookieJar object containing cookies.
        :param params: Optional dictionary of query string parameters to append to the URL.
        :param proxy: Optional proxy configuration string or Proxies object.
        :param retries: Number of times to retry the request in case of certain types of failures.
        :return: Response object if the request is successful; None otherwise.
        """
        if proxy is not None:
            if isinstance(proxy, Proxies):
                proxy = proxy.http

            proxy = f"http://{proxy}"
        with hrequests.chrome.Session(headers=headers, proxy=proxy, cookies=cookies) as session:

            for _ in range(retries):
                try:
                    r = session.get(url, params=params, nohup=nowait)
                    return r
                except (Timeout,
                        ReadTimeout,
                        ConnectTimeout,
                        ChunkedEncodingError,
                        ConnectionError):
                    logger.error("request failed")

        return None

    @staticmethod
    def post(
            url: str,
            headers: dict | None = None,
            json: dict | None = None,
            data: dict | None = None,
            cookies: dict | None | RequestsCookieJar = None,
            params: dict | None = None,
            proxy: str | Proxies | None = None,
            retries: int = 3,
            nowait: bool = False

    ) -> requests.Response | None:
        """
        :param nowait:
        :param url: The endpoint URL for the POST request.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param json: Optional dictionary of JSON data to send in the body of the request.
        :param data: Optional dictionary of form data to send in the body of the request.
        :param cookies: Optional dictionary or RequestsCookieJar of cookies to send with the request.
        :param params: Optional dictionary of URL query string parameters.
        :param proxy: Optional string or Proxies object defining the proxy server to use for the request.
        :param retries: Optional integer defining the number of times to retry the request in case of errors. Default is 3.
        :return: A requests.Response object if the request succeeds, or None if all retry attempts fail.
        """
        if proxy is not None:
            if isinstance(proxy, Proxies):
                proxy = proxy.http

            proxy = f"http://{proxy}"
        with hrequests.chrome.Session(headers=headers, proxy=proxy, cookies=cookies) as session:

            for _ in range(retries):
                try:
                    r = session.post(url, params=params, json=json, data=data, nohup=nowait)
                    return r
                except (Timeout,
                        ReadTimeout,
                        ConnectTimeout,
                        ChunkedEncodingError,
                        ConnectionError):
                    logger.error("request failed")

        return None

    @staticmethod
    def put(
            url: str,
            headers: dict | None = None,
            json: dict | None = None,
            data: dict | None = None,
            cookies: dict | None | RequestsCookieJar = None,
            params: dict | None = None,
            proxy: str | Proxies | None = None,
            retries: int = 3,
            nowait: bool = False

    ) -> requests.Response | None:
        """
        :param nowait:
        :param url: The endpoint URL for the PUT request.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param json: Optional dictionary of JSON data to send in the body of the request.
        :param data: Optional dictionary of form data to send in the body of the request.
        :param cookies: Optional dictionary or RequestsCookieJar of cookies to send with the request.
        :param params: Optional dictionary of URL query string parameters.
        :param proxy: Optional string or Proxies object defining the proxy server to use for the request.
        :param retries: Optional integer defining the number of times to retry the request in case of errors. Default is 3.
        :return: A requests.Response object if the request succeeds, or None if all retry attempts fail.
        """
        if proxy is not None:
            if isinstance(proxy, Proxies):
                proxy = proxy.http

            proxy = f"http://{proxy}"
        with hrequests.chrome.Session(headers=headers, proxy=proxy, cookies=cookies) as session:

            for _ in range(retries):
                try:
                    r = session.put(url, params=params, json=json, data=data, nohup=nowait)
                    return r
                except (Timeout,
                        ReadTimeout,
                        ConnectTimeout,
                        ChunkedEncodingError,
                        ConnectionError):
                    logger.error("request failed")

        return None

    @staticmethod
    def delete(
            url: str,
            headers: dict | None = None,
            cookies: dict | None | RequestsCookieJar = None,
            params: dict | None = None,
            proxy: str | Proxies | None = None,
            retries: int = 3,
            nowait: bool = False

    ) -> requests.Response | None:
        """
        :param nowait:
        :param url: The endpoint URL for the DELETE request.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param cookies: Optional dictionary or RequestsCookieJar of cookies to send with the request.
        :param params: Optional dictionary of URL query string parameters.
        :param proxy: Optional string or Proxies object defining the proxy server to use for the request.
        :param retries: Optional integer defining the number of times to retry the request in case of errors. Default is 3.
        :return: A requests.Response object if the request succeeds, or None if all retry attempts fail.
        """
        if proxy is not None:
            if isinstance(proxy, Proxies):
                proxy = proxy.http

            proxy = f"http://{proxy}"
        with hrequests.chrome.Session(headers=headers, proxy=proxy, cookies=cookies) as session:

            for _ in range(retries):
                try:
                    r = session.delete(url, params=params, nohup=nowait)
                    return r
                except (Timeout,
                        ReadTimeout,
                        ConnectTimeout,
                        ChunkedEncodingError,
                        ConnectionError):
                    logger.error("request failed")

        return None

    @staticmethod
    def options(
            url: str,
            headers: dict | None = None,
            cookies: dict | None | RequestsCookieJar = None,
            params: dict | None = None,
            proxy: str | Proxies | None = None,
            retries: int = 3,
            nowait: bool = False

    ) -> requests.Response | None:
        """
        :param nowait:
        :param url: The endpoint URL for the OPTIONS request.
        :param headers: Optional dictionary of HTTP headers to send with the request.
        :param cookies: Optional dictionary or RequestsCookieJar of cookies to send with the request.
        :param params: Optional dictionary of URL query string parameters.
        :param proxy: Optional string or Proxies object defining the proxy server to use for the request.
        :param retries: Optional integer defining the number of times to retry the request in case of errors. Default is 3.
        :return: A requests.Response object if the request succeeds, or None if all retry attempts fail.
        """
        if proxy is not None:
            if isinstance(proxy, Proxies):
                proxy = proxy.http

            proxy = f"http://{proxy}"
        with hrequests.chrome.Session(headers=headers, proxy=proxy, cookies=cookies) as session:

            for _ in range(retries):
                try:
                    r = session.options(url, params=params, nohup=nowait)
                    return r
                except (Timeout,
                        ReadTimeout,
                        ConnectTimeout,
                        ChunkedEncodingError,
                        ConnectionError):
                    logger.error("request failed")

        return None
