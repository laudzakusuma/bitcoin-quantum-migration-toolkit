import requests

def get_utxos(address):

    apis = [
        f"https://blockstream.info/api/address/{address}/utxo",
        f"https://mempool.space/api/address/{address}/utxo"
    ]

    for url in apis:
        try:
            r = requests.get(url, timeout=10)

            if r.status_code == 200:
                return r.json()

        except:
            pass

    return None


def summarize_utxos(utxos):

    total = 0

    for u in utxos:
        total += u["value"]

    total_btc = total / 100000000

    return {
        "count": len(utxos),
        "total_btc": total_btc
    }