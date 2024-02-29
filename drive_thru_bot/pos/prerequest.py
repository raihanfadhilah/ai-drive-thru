import os
import datetime
import hashlib
import base64
from pytz import timezone  # type: ignore


# Convert variables
def get_env_var(variable):
    return os.getenv(variable)


# Unique Key generation based on the current date
def unique_key(date):
    nonce = date.astimezone(timezone("UTC")).isoformat(timespec="seconds") + ".000Z"
    return get_env_var("BSP_SECRET_KEY") + nonce


# Signable content creation
def signable_content(method, url, content_type, content_md5, organization):
    request_path = url.replace(r"^https?:\/\/[^\/]+\/", "/", 1)
    return "\n".join(
        filter(None, [method, request_path, content_type, content_md5, organization])
    )


# Adjust calculateSignature to return both date and signature
def calculate_signature():
    date = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )
    key = unique_key(datetime.datetime.now(datetime.timezone.utc))
    organization = get_env_var("BSP_ORGANIZATION")
    # Example request details
    method = "POST"
    url = "/order/3/orders/1"
    content_type = "application/json"
    content_md5 = None

    sc = signable_content(method, url, content_type, content_md5, organization)
    signature = base64.b64encode(
        hashlib.sha512(sc.encode("utf-8") + key.encode("utf-8")).digest()
    ).decode("utf-8")
    return {"date": date, "signature": signature}


# Update generateAccessKey to use the modified calculateSignature
def generate_date_and_access_key():
    result = calculate_signature()
    date = result["date"]
    signature = result["signature"]
    shared_key = get_env_var("BSP_SHARED_KEY")
    access_key = f"AccessKey {shared_key}:{signature}"
    print("Generated BSP Access Key:", access_key)

    # For appending to .env file, you'd need to handle file operations directly in Python
    # This example does not include the file append logic directly but it's straightforward with open()

    return access_key, date


# This example assumes the existence of an environment with proper variables and timezone handling with pytz.
# Adjustments might be needed based on your specific environment and requirements.
