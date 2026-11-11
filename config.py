import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "ORANGEHRM_BASE_URL",
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
)


@dataclass(frozen=True)
class Credentials:
    username: str
    password: str


def get_credentials() -> Credentials:
    username = os.getenv("ORANGEHRM_USERNAME")
    password = os.getenv("ORANGEHRM_PASSWORD")
    if not username or not password:
        raise RuntimeError(
            "Set ORANGEHRM_USERNAME and ORANGEHRM_PASSWORD in the project .env file."
        )
    return Credentials(username=username, password=password)
