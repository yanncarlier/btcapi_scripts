# btcapi_scripts

### **Primary Standard Address Types (5 Types)**



Output reordered chronologically:



1. Originally in 2009, `bitcoind` (Bitcoin Core) used **P2PKH (Pay-to-PubKey-Hash)** addresses as its standard address format for receiving transactions
2. **Electrum** (2011) – `m/0'/0'/0`
3. **BIP32 Bitcoin** (2012) – `m/44'/0'/0'/0/0`
4. **Legacy / Bitcoin Core (BIP44)** (2014) – `m/44'/0'/0'/0/0`
5. **Multibit** (2014) – `m/0'/0/0`
6. **Nested SegWit (BIP49)** (2016) – `m/49'/0'/0'/0/0`
7. **Native SegWit (BIP84)** (2017) – `m/84'/0'/0'/0/0`
8. **Taproot (BIP86)** (2021) – `m/86'/0'/0'/0/0`



Modern Bitcoin software generates addresses using different script formats from the same master seed by using specific **BIP44/49/84/86/32 derivation paths**:

| **Address Type**    | **Standard Name**      | **Address Prefix** | **Derivation Path Structure** | **Purpose / Features**                                       |
| ------------------- | ---------------------- | ------------------ | ----------------------------- | ------------------------------------------------------------ |
| **P2PKH**           | Legacy                 | `1...`             | `m/44'/0'/0'/0/i`             | Original Bitcoin format (highest fees).                      |
| **P2SH-P2WPKH**     | Nested SegWit          | `3...`             | `m/49'/0'/0'/0/i`             | SegWit wrapped in P2SH for backward compatibility.           |
| **P2WPKH**          | Native SegWit (Bech32) | `bc1q...`          | `m/84'/0'/0'/0/i`             | Lower transaction fees, standard for most wallets today.     |
| **P2TR**            | Taproot (Bech32m)      | `bc1p...`          | `m/86'/0'/0'/0/i`             | Modern privacy, smart contract efficiency, and lowest fee potential. |
| **P2SH** (Multisig) | Pay-to-Script-Hash     | `3...`             | Custom scripts                | Used for multisig or custom script derivations from the same keys. |



### **Network & Variant Extensions**

If you include test networks and non-standard derivations, the same seed also supports:

- **Testnet / Signet / Regtest:** Parallel address structures (`tb1q...`, `tb1p...`, `m...`, `2...`) using the same seed.
- **Custom / Legacy Derivation Paths:** Non-standard paths used by older wallets (e.g., Electrum legacy paths `m/0'/0/i` or custom account indices).
- **Silent Payments (BIP352):** Emerging reusable privacy address formats derived from the master seed.





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
