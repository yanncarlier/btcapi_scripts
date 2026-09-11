# btc-py-scripts

Educational Python scripts for deriving Bitcoin mainnet addresses from BIP39
mnemonics, generating a mnemonic, experimenting with a brain wallet, and
looking up a fixed address through public blockchain APIs.

> **Warning:** Several scripts print a mnemonic, seed, private key, or WIF to
> standard output. Treat that output as secret. The bundled mnemonic is a
> public test vector and must never receive funds. All derivation scripts
> target Bitcoin mainnet.

## Requirements and setup

- Python 3.10 or newer
- `uv` (recommended) or `pip`

With `uv`:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Or with the Python standard library and `pip`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Dependencies are declared in `requirements.in` and pinned in
`requirements.txt`. Run the examples from the repository root. After setup,
use `.venv/bin/python` or `python` while the virtual environment is active.

## Command-line arguments

Four scripts currently accept command-line arguments:

| Script | Usage | Argument |
| --- | --- | --- |
| `all_address_types.py` | `python all_address_types.py [MNEMONIC]` | Optional, complete BIP39 mnemonic. |
| `net/blockchain.info.py` | `python net/blockchain.info.py ADDRESS` | Required Bitcoin address to query. |
| `net/blockcypher.com.py` | `python net/blockcypher.com.py ADDRESS` | Required Bitcoin address to query. |
| `net/blockstream.info.py` | `python net/blockstream.info.py ADDRESS` | Required Bitcoin address to query. |
| `net/mempool.space.py` | `python net/mempool.space.py ADDRESS` | Required Bitcoin address to query. |

`all_address_types.py` accepts an optional positional argument: a complete,
quoted BIP39 mnemonic:

```text
python all_address_types.py [MNEMONIC]
```

| Argument | Required | Meaning |
| --- | --- | --- |
| `MNEMONIC` | No | A valid 12- or 24-word BIP39 mnemonic. It must be passed as one quoted shell argument. When omitted, the script uses its public test mnemonic. |

Examples:

```bash
# Display the supported argument and built-in help
python all_address_types.py --help

# Use the public test mnemonic (safe only for demonstration)
python all_address_types.py

# Derive addresses from a supplied mnemonic
python all_address_types.py "word1 word2 word3 ... word12"
```

There are no flags for a BIP39 passphrase, account, change chain, address
index, network, or address count. Those values are fixed by the current code.

## Running the scripts

### Derive all supported address types

```bash
python all_address_types.py "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
```

The output contains one address per supported derivation scheme. This command
does not print private keys.

### Individual derivation scripts

The following scripts take **no command-line arguments**. They currently use
the `mnemonic`, `passphrase`, and (where present) `num_addresses` variables at
the top of the source file. To use a different value, edit those variables
locally before executing the script; do not put a real mnemonic in shell
history or commit it to the repository.

| Command | Current derivation/output |
| --- | --- |
| `python P2PKH_addresses.py` | P2PKH from the BIP32 master key (`m`) |
| `python Electrum_addresses.py` | Electrum-style P2PKH (`m/0'/0`) |
| `python BitcoinCoreHD_addresses.py` | Bitcoin Core-style HD P2PKH (`m/0'/0'/0'`) |
| `python MultiBitClassic_addresses.py` | MultiBit Classic-style P2PKH (`m/0'/0/0`; approximate) |
| `python MultiBitHD_addresses.py` | MultiBit HD-style P2PKH (`m/0'/0/0'`) |
| `python BIP44_addresses.py` | BIP44 legacy P2PKH (`m/44'/0'/0'/0/0`) |
| `python BIP44_external_chain_addresses.py` | BIP44 external-chain key (`m/44'/0'/0'/0`) |
| `python BIP49_addresses.py` | BIP49 nested SegWit P2SH-P2WPKH (`m/49'/0'/0'/0/0`) |
| `python BIP84_addresses.py` | BIP84 native SegWit P2WPKH (`m/84'/0'/0'/0/0`) |
| `python BIP86_addresses.py` | BIP86 Taproot P2TR (`m/86'/0'/0'/0/0`) |

These scripts print sensitive seed and key material. `BIP44_external_chain_addresses.py`
derives the chain-level key, not the first receiving address; append `/0` to
the displayed path conceptually for the first external address.

### Generate a new mnemonic

```bash
python generate_mnemonic.py
```

This script takes no arguments. It generates a 12-word English BIP39 mnemonic
using the hard-coded strength of 128 bits, then prints the seed and BIP32 root
key. Change `strength=128` in the source to `256` for a 24-word mnemonic.

### Brain-wallet demonstration

```bash
python brain_wallet.py
```

This script takes no arguments. It hashes the hard-coded `passphrase` in
`brain_wallet.py` with SHA-256 and prints an uncompressed mainnet WIF and
P2PKH address. Brain wallets are vulnerable to guessing and brute-force
attacks; do not use this method to secure Bitcoin.

### Blockchain API lookups

```bash
python net/blockchain.info.py ADDRESS
python net/blockcypher.com.py ADDRESS
python net/blockstream.info.py ADDRESS
python net/mempool.space.py ADDRESS
```

Each lookup script requires one `ADDRESS` positional argument and prints a
single total balance in satoshis. The total includes confirmed and unconfirmed
funds when the provider reports them. For example:

```bash
python net/blockchain.info.py bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr
python net/blockcypher.com.py bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr
python net/blockstream.info.py bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr
python net/mempool.space.py bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr
```

The Mempool Space script uses `GET /api/address/:address`, then calculates the
balance from its confirmed and mempool transaction statistics. All lookup
commands require internet access and depend on the availability and rate limits
of the respective public API.

## Scripts at a glance

| Script | Purpose |
| --- | --- |
| `all_address_types.py` | Print addresses for all supported derivation schemes from one mnemonic; supports `[MNEMONIC]`. |
| `generate_mnemonic.py` | Generate a new BIP39 mnemonic, seed, and BIP32 root key. |
| `brain_wallet.py` | Educational SHA-256 brain-wallet example. |
| `net/blockchain.info.py` | Query the Blockchain.com address-balance endpoint. |
| `net/blockcypher.com.py` | Query the BlockCypher address endpoint. |
| `net/blockstream.info.py` | Query the Blockstream Esplora address endpoint. |
| `net/mempool.space.py` | Query the Mempool Space address-details endpoint. |

The remaining address-derivation scripts are listed in the individual
derivation table above.

## Security notes

- Never use the bundled `abandon ... about` mnemonic for funds; it is public.
- Never share or commit a real mnemonic, seed, private key, WIF, or brain-wallet passphrase.
- Prefer an established wallet and a hardware signer for real funds.
- Verify derivation paths, address type, and network with the wallet you are
  recovering or inspecting before sending funds.
