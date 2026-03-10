def estimate_migration(utxo_count):
    input_size = 68
    output_size = 43
    base_tx = 10

    tx_size = base_tx + (utxo_count * input_size) + output_size

    fee_rate = 20

    fee_sat = tx_size * fee_rate
    fee_btc = fee_sat / 100000000

    return {
        "tx_size": tx_size,
        "fee_sat": fee_sat,
        "fee_btc": fee_btc
    }