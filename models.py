from __future__ import annotations
from typing import *
from pydantic.dataclasses import dataclass, Field


@dataclass
class Proxies:
    http: str
    https: str

    def __post_init__(self):
        if "//" in self.http:
            self.http = self.http.split("//")[1]

        if "//" in self.https:
            self.https = self.https.split("//")[1]


