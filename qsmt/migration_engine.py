def batch_utxos(utxos, batch_size=20):
    batches = []

    for i in range(0, len(utxos), batch_size):
        batches.append(utxos[i:i+batch_size])

    return batches


def calculate_total(utxos):

    total_sats = sum(u["value"] for u in utxos)

    total_btc = total_sats / 100000000

    return total_btc

def plan_split(total_btc):

    if total_btc < 0.00001:
        return [round(total_btc,8)]

    template = [
    0.00005,
    0.00002,
    0.00001,
    0.000005,
    0.000002
]

    outputs = []
    remaining = total_btc

    for t in template:
        if remaining > t:
            outputs.append(t)
            remaining -= t

    if remaining > 0:
        outputs.append(round(remaining, 8))

    return outputs


def build_migration_plan(utxos):

    batches = batch_utxos(utxos)

    total = calculate_total(utxos)

    split_outputs = plan_split(total)

    return {
        "utxo_count": len(utxos),
        "consolidation_txs": len(batches),
        "total_btc": total,
        "split_plan": split_outputs
    }