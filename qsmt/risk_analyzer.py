def fragmentation_score(utxo_count):

    if utxo_count < 10:
        return "LOW"

    elif utxo_count < 50:
        return "MEDIUM"

    else:
        return "HIGH"