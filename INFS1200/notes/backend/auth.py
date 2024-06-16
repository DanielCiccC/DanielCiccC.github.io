import os
from typing import Final, Any
import logging

import datetime
import jwt
from flask import request

JWT_AUDIENCE: Final[str] = "MechanicAssist"
JWT_ISSUER: Final[str] = "MechanicAssist"
JWT_EXPIRY_SECONDS: Final[int] = 8 * 60 * 60

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_request_jwt() -> dict[str, Any]:
    auth_header = request.headers.get("Authorization")

    if auth_header is None:
        logger.info("Not jwt found on request.")
        return False

    token_encoded = auth_header[len("Bearer ") :]
    token: dict[str, Any] = jwt.decode(
        token_encoded,
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"],
        audience=JWT_AUDIENCE,
        issuer=JWT_ISSUER,
        verify=True,
    )

    return token


def valid_jwt() -> bool:

    token: dict[str, Any] = get_request_jwt()

    nbf_datetime = datetime.datetime.fromtimestamp(token["nbf"])
    exp_datetime = datetime.datetime.fromtimestamp(token["exp"])

    if not nbf_datetime < datetime.datetime.now():
        logger.info("jwt used before nbf time.")
        return False

    if not exp_datetime > datetime.datetime.now():
        logger.info("jwt used after exp time.")
        return False

    return True
