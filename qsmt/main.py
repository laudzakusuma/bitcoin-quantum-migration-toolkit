import sys
from scanner import get_utxos, summarize_utxos
from risk_analyzer import fragmentation_score
from quantum_exposure import check_public_key_exposure
from migration_estimator import estimate_migration
from migration_complexity import migration_complexity
from migration_engine import build_migration_plan
from pqc_wallet import generate_pqc_keypair, generate_pqc_address

def scan(address):

    utxos = get_utxos(address)

    if utxos is None:
        print("Failed to fetch UTXO")
        return

    summary = summarize_utxos(utxos)

    risk = fragmentation_score(summary["count"])

    print("\nQSMT Wallet Scan")
    print("-------------------")

    print("Address:", address)
    print("UTXO Count:", summary["count"])
    print("Total BTC:", summary["total_btc"])
    print("Fragmentation Risk:", risk)

    exposed = check_public_key_exposure(address)

    if exposed is None:
        exposure_status = "UNKNOWN"
    elif exposed:
        exposure_status = "YES"
    else:
        exposure_status = "NO"

    print("Public Key Exposure:", exposure_status)

    migration = estimate_migration(summary["count"])

    print("\nMigration Estimate")
    print("Estimated TX Size:", migration["tx_size"], "bytes")
    print("Estimated Fee:", migration["fee_sat"], "sat")
    print("Estimated Fee in BTC:", migration["fee_btc"])

    complexity = migration_complexity(summary["count"])
    print("\nMigration Complexity:", complexity)

    plan = build_migration_plan(utxos)

    print("UTXO Count:", plan["utxo_count"])
    print("Consolidation TX:", plan["consolidation_txs"])
    print("Total BTC:", plan["total_btc"])

    print("\nSplit Plan:")

    for s in plan["split_plan"]:
        print("-", format(s, ".8f"), "BTC")

    priv, pub = generate_pqc_keypair()
    pqc_address = generate_pqc_address(pub)

    print("\nGenerated PQC Wallet")

    print("Public Key:", pub[:30],"...")
    print("Address:", pqc_address)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python main.py <bitcoin_address>")
        exit()

    address = sys.argv[1]

    scan(address)