def estimate_fee(inputs, outputs, sat_per_byte=20):
    size = inputs * 148 + outputs * 34 + 10
    fee = size * sat_per_byte

    return fee

def build_consolidation_tx(batch):
    total = sum(u["value"] for u in batch)
    fee = estimate_fee(len(batch), 1)
    output_value = total - (fee/100000000)

    tx = {
        "inputs": batch,
        "outputs": [
            {
                "type": "consolidation",
                "value": output_value
            }
        ]
    }

    return tx

def build_migration_tx(utxo, pqc_address):
    fee = estimate_fee(1,1)
    value = utxo["value"] - (fee/100000000)

    tx = {
        "inputs":[utxo],
        "outputs":[
            {
                "address":pqc_address,
                "value":value
            }
        ]
    }

    return tx

def build_split_tx(total, split_plan, pqc_address):

    outputs = []

    for s in split_plan:
        outputs.append({
            "address":pqc_address,
            "value":s
        })

    tx = {
        "inputs":[{"value":total}],
        "outputs":outputs
    }

    return tx