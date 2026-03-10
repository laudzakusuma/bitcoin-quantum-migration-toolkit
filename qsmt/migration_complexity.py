def migration_complexity(utxo_count):
    if utxo_count <= 5:
        return "LOW"

    elif utxo_count <= 50:
        return "MEDIUM"

    else:
        return "HIGH"