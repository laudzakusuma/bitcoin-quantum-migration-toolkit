# Quantum Safe Migration Toolkit (QSMT)

Quantum Safe Migration Toolkit adalah alat analisis untuk mengevaluasi kesiapan wallet Bitcoin terhadap migrasi kriptografi post-quantum.

Toolkit ini menganalisis beberapa faktor penting seperti:

- UTXO fragmentation
- Public key exposure
- Migration cost estimation
- Migration complexity

Tujuannya adalah membantu memahami tantangan migrasi dari ECDSA menuju algoritma Post-Quantum Cryptography (PQC) pada jaringan Bitcoin.

## Features

1. Wallet scanner
2. UTXO fragmentation analysis
3. Public key exposure detection
4. Migration cost estimation
5. Migration complexity analysis

## Installation

Clone repository:

git clone https://github.com/username/bitcoin-quantum-migration-toolkit.git

Install dependency:

pip install -r requirements.txt

## Usage

python qsmt/main.py <bitcoin_address>

Example:

python qsmt/main.py bc1p3ysqxdc887ywqv2dfxslp0a4xcvq9uplu4yaa29e6ydpxn34a7sqv4t4dq