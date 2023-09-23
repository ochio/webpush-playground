from pywebpush import webpush, WebPushException
from dotenv import load_dotenv
import os

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
KEYS_p256dh = os.getenv("KEYS_p256dh")
KEYS_AUTH = os.getenv("KEYS_AUTH")
VAPID_PRIVATE_KEY = os.getenv("VAPID_PRIVATE_KEY")


def main():
    try:
        webpush(
            subscription_info={
                "endpoint": ENDPOINT,
                "expirationTime": None,
                "keys": {
                    "p256dh": KEYS_p256dh,
                    "auth": KEYS_AUTH,
                },
            },
            data="Mary had a little lamb, with a nice mint jelly",
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims={
                "sub": "mailto:test@example.com",
            },
        )
    except WebPushException as ex:
        print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
        # Mozilla returns additional information in the body of the response.
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print(
                "Remote service replied with a {}:{}, {}",
                extra.code,
                extra.errno,
                extra.message,
            )


if __name__ == "__main__":
    main()
