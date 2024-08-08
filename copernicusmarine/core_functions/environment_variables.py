import logging
import os

logger = logging.getLogger("copernicus_marine_root_logger")

COPERNICUSMARINE_SERVICE_USERNAME = os.getenv(
    "COPERNICUSMARINE_SERVICE_USERNAME"
) or os.getenv("COPERNICUS_MARINE_SERVICE_USERNAME")
if os.getenv("COPERNICUS_MARINE_SERVICE_USERNAME"):
    logger.warning(
        "COPERNICUS_MARINE_SERVICE_USERNAME is deprecated. "
        "Please use COPERNICUSMARINE_SERVICE_USERNAME instead."
    )
COPERNICUSMARINE_SERVICE_PASSWORD = os.getenv(
    "COPERNICUSMARINE_SERVICE_PASSWORD"
) or os.getenv("COPERNICUS_MARINE_SERVICE_PASSWORD")
if os.getenv("COPERNICUS_MARINE_SERVICE_PASSWORD"):
    logger.warning(
        "COPERNICUS_MARINE_SERVICE_PASSWORD is deprecated. "
        "Please use COPERNICUSMARINE_SERVICE_PASSWORD instead."
    )

COPERNICUSMARINE_CACHE_DIRECTORY = os.getenv(
    "COPERNICUSMARINE_CACHE_DIRECTORY", ""
)

COPERNICUSMARINE_MAX_CONCURRENT_REQUESTS = os.getenv(
    "COPERNICUSMARINE_MAX_CONCURRENT_REQUESTS", "15"
)

COPERNICUSMARINE_GET_CONCURRENT_DOWNLOADS = os.getenv(
    "COPERNICUSMARINE_GET_CONCURRENT_DOWNLOADS", None
)

COPERNICUSMARINE_DISABLE_SSL_CONTEXT = os.getenv(
    "COPERNICUSMARINE_DISABLE_SSL_CONTEXT"
)
COPERNICUSMARINE_TRUST_ENV = os.getenv("COPERNICUSMARINE_TRUST_ENV", "True")

PROXY_HTTPS = os.getenv("HTTPS_PROXY", "")
PROXY_HTTP = os.getenv("HTTP_PROXY", "")

COPERNICUSMARINE_GET_TIMEOUT= os.getenv(
    "COPERNICUSMARINE_GET_TIMEOUT", 30
)