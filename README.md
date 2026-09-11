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

## Usage examples:

Run any script directly with Python:

```bash
python generate_mnemonic.py
++++++++++++++++++++++++++++++++++++++++++++++
BIP39 Mnemonic: tomato vast lemon ride narrow sphere trial when belt member salute faith
++++++++++++++++++++++++++++++++++++++++++++++
BIP39 Seed: 2fd19b4428c91719c653e997d9efc4fbd7350f36665fe1126ec95f943340e093b7fca994e57947abcfe48478b04c0c8b8dccc8b07edca1aef1246ca213119cf8
++++++++++++++++++++++++++++++++++++++++++++++
BIP32 Root Key: xprv9s21ZrQH143K2So96Kcab6t8pSAueGKbdjmx2nrZBXwCgyAnFaDL1eg4TPL8t47m4RTRFJmLdpAwK7PQL6XzKjhzUGUxvhqz9BWc76cXBG5
++++++++++++++++++++++++++++++++++++++++++++++
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
- `P2PKH_addresses.py` — pre-HD era P2PKH (2009 Bitcoin Core)
- `Electrum_addresses.py` — Electrum-style P2PKH
- `BitcoinCoreHD_addresses.py` — Bitcoin Core HD P2PKH
- `MultiBitClassic_addresses.py` — MultiBit Classic-style P2PKH
- `BIP44_external_chain_addresses.py` — BIP44 external chain P2PKH
- `MultiBitHD_addresses.py` — MultiBit HD-style P2PKH
- `BIP44_addresses.py` — BIP44 Legacy P2PKH
- `BIP49_addresses.py` — BIP49 Nested SegWit (P2SH-P2WPKH)
- `BIP84_addresses.py` — BIP84 Native SegWit (P2WPKH)
- `BIP86_addresses.py` — BIP86 Taproot (P2TR)
- `generate_mnemonic.py` — Generate a BIP39 mnemonic phrase
- `brain_wallet.py` — Brain wallet address derivation from a passphrase
- `all_address_types.py` — All address types from same seed

### Chronological Order (Earliest to Latest)
The address generation scripts in chronological order of their standards' introduction:

| # | Script | Derivation Path | Year | Description |
|---|--------|----------------|------|-------------|
| 1 | `P2PKH_addresses.py` | m → P2PKH | 2009 | Original Bitcoin Core (no HD) |
| 2 | `Electrum_addresses.py` | m/0'/0 | ~2011 | Electrum wallet |
| 3 | `BitcoinCoreHD_addresses.py` | m/0'/0'/0' | ~2012 | Early Bitcoin Core HD |
| 4 | `MultiBitClassic_addresses.py` | m/0'/0/0 | ~2013 | MultiBit Classic |
| 5 | `BIP44_addresses.py` | m/44'/0'/0'/0/0 | 2014 | BIP44 Legacy P2PKH |
| 6 | `BIP44_external_chain_addresses.py` | m/44'/0'/0'/0 | 2014 | BIP44 chain-level |
| 7 | `MultiBitHD_addresses.py` | m/0'/0/0' | ~2014 | MultiBit HD |
| 8 | `BIP49_addresses.py` | m/49'/0'/0'/0/0 | 2017 | BIP49 Nested SegWit |
| 9 | `BIP84_addresses.py` | m/84'/0'/0'/0/0 | 2017 | BIP84 Native SegWit |
| 10 | `BIP86_addresses.py` | m/86'/0'/0'/0/0 | 2020 | BIP86 Taproot

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
