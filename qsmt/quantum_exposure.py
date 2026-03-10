import requests

def check_public_key_exposure(address):

    url = f"https://mempool.space/api/address/{address}"

    try:
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            return None

        data = r.json()

        spent = data["chain_stats"]["spent_txo_count"]

        if spent > 0:
            return True
        else:
            return False

    except:
        return None