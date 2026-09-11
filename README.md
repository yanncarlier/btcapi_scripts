# btc-py-scripts


A collection of Python scripts for Bitcoin address generation using various BIP standards, plus blockchain API lookups.

## Setup

```bash
# Create a virtual environment
uv venv

# Activate the environment
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## Usage

Run any script directly with Python:

```bash
python generate_mnemonic.py
python BIP44_addresses.py
python BIP86_addressess.py
```
To generate addresses from a common BIP39 seed using historical and modern Bitcoin derivation schemes:

```
1BZ9j3F7m4H1RPyeDp5iFwpR31SB6zrs19  # Illustrative: pre-HD era P2PKH (Bitcoin Core 2009 had no mnemonic/HD; shown here as m → P2PKH)
1Q5FHbm75ZYDnHkGgBC2y8cCn8cTrqK37v  # Electrum-style derivation — m/0'/0
16fWWdLokmpctATuim8q5SvAu1GR9prV5m  # Bitcoin Core-style HD derivation — m/0'/0'/0'
1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA  # BIP44 Legacy P2PKH — m/44'/0'/0'/0/0
17871ErDqdevLTLWBH6WzjUc1EKGDQzCMA  # MultiBit Classic-style derivation — m/0'/0/0 (approximate; MultiBit Classic used its own seed format, not BIP39)
13KE6TffArLh4fVM6uoQzvsYq5vwetJcVM  # BIP44 external-chain derivation — m/44'/0'/0'/0 (chain-level; first address normally /0)
1Ecw6WNntSpgRMtMfdeCt72UzsTEbqq6As  # MultiBit HD-style derivation — m/0'/0/0'
37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf  # BIP49 Nested SegWit P2SH-P2WPKH — m/49'/0'/0'/0/0
bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu  # BIP84 Native SegWit P2WPKH — m/84'/0'/0'/0/0
bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr  # BIP86 Taproot P2TR — m/86'/0'/0'/0/0
```
## Scripts

### Address Generation (BIP standards)
- `BIP32_addresses.py` — BIP32 hierarchical deterministic addresses
- `BIP44_addresses.py` — BIP44 legacy (P2PKH) addresses
- `BIP49_addresses.py` — BIP49 nested SegWit (P2SH-P2WPKH) addresses
- `BIP84_addressess.py` — BIP84 native SegWit (Bech32 / P2WPKH) addresses
- `BIP86_addressess.py` — BIP86 Taproot (P2TR) addresses
- `generate_mnemonic.py` — Generate a BIP39 mnemonic phrase
- `brain_wallet.py` — Brain wallet address derivation from a passphrase
- `all_address_types.py` — All address types from same seed (chronological)

### Blockchain API Lookups
- `blockchain.info.py` — Query blockchain.info
- `blockcypher.com.py` — Query blockcypher.com
- `blockstream.info.py` — Query blockstream.info



## Dependencies

Declared in `requirements.in`, pinned in `requirements.txt`:

- `base58` — Base58 encoding
- `bitcoinlib` — Bitcoin transaction/script library
- `cryptography` — Cryptographic primitives
- `mnemonic` — BIP39 mnemonic generation

## Security Notes

- These scripts handle sensitive cryptographic material (mnemonics, private keys, passphrases).
- Never share or commit generated mnemonics, seeds, or private keys.
- Use only for learning, testing, or with keys you control.
