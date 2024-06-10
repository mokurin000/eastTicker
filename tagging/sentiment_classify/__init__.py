from cachier import cachier
import requests

PER_SEC = 5


@cachier()
def sentiment_classify(access_token: str, text: str) -> dict[str, int | float]:
    resp = requests.post(
        "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify",
        json={
            "text": text,
        },
        params={
            "access_token": access_token,
            "charset": "UTF-8",
        },
        timeout=10,
    )
    if not resp.ok:
        return None

    data = resp.json()["items"][0]

    return {
        "sentiment": data["sentiment"],
        "confidence": data["confidence"],
        "positive_prob": data["positive_prob"],
        "negative_prob": data["negative_prob"],
    }
