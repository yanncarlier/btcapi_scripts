# btcapi_scripts

```
python all_address_types.py "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
Mnemonic: abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about

1BZ9j3F7m4H1RPyeDp5iFwpR31SB6zrs19  # Original bitcoind (Bitcoin Core) (2009) used P2PKH (Pay-to-PubKey-Hash) - m
1Q5FHbm75ZYDnHkGgBC2y8cCn8cTrqK37v  # Electrum (2011) - m/0'/0
16fWWdLokmpctATuim8q5SvAu1GR9prV5m  # Bitcoin Core (2012) - m/0'/0'/0'
1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA  # Legacy / Bitcoin Core (BIP44) (2014) - m/44'/0'/0'/0/0
17871ErDqdevLTLWBH6WzjUc1EKGDQzCMA  # MultiBit Classic (2011/2014) - m/0'/0/0
13KE6TffArLh4fVM6uoQzvsYq5vwetJcVM  # Coinomi (2014), Ledger (2014/2015), Blockchain.info (2015) (BIP44 variant) - m/44'/0'/0'/0
1Ecw6WNntSpgRMtMfdeCt72UzsTEbqq6As  # MultiBit HD (2015) - m/0'/0/0'
37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf  # Nested SegWit (BIP49) (2016) - m/49'/0'/0'/0/0
bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu  # Native SegWit (BIP84) (2017) - m/84'/0'/0'/0/0
bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr  # Taproot (BIP86) (2021) - m/86'/0'/0'/0/0

```



A collection of Python scripts for Bitcoin address generation using various BIP standards, plus blockchain API lookups.

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

## Setup

```bash
# Create a virtual environment
uv venv

# Install dependencies
uv pip install -r requirements.txt

# Activate the environment
source .venv/bin/activate
```

## Usage

Run any script directly with Python:

```bash
python generate_mnemonic.py
python BIP44_addresses.py
python BIP86_addressess.py
```

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
