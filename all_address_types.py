import argparse

from bip_utils import (
    Bip39SeedGenerator,
    Bip44, Bip44Coins, Bip44Changes,
    Bip49, Bip49Coins,
    Bip84, Bip84Coins,
    Bip86, Bip86Coins,
    Bip32Secp256k1,
    Bip39MnemonicValidator,
    Hash160,
    Base58Encoder,
)
from bip_utils.utils.mnemonic import MnemonicChecksumError

DEFAULT_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

# Originally in 2009, bitcoind (Bitcoin Core) used P2PKH (Pay-to-PubKey-Hash)


def compute_p2pkh_address(pub_key_bytes):
    # Use compressed public key for address generation (standard for modern Bitcoin)
    h160 = Hash160.QuickDigest(pub_key_bytes)
    return Base58Encoder.CheckEncode(b"\x00" + h160)


def main():
    parser = argparse.ArgumentParser(description="Generate Bitcoin addresses from a BIP39 mnemonic.")
    parser.add_argument("mnemonic", nargs="?", default=DEFAULT_MNEMONIC,
                        help="BIP39 mnemonic phrase (12 or 24 words). If omitted, uses a default test phrase.")
    args = parser.parse_args()

    mnemonic = args.mnemonic.strip()

    try:
        Bip39MnemonicValidator().Validate(mnemonic)
    except MnemonicChecksumError:
        raise ValueError("Invalid mnemonic phrase. Please provide a valid BIP39 mnemonic (12 or 24 words).")

    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    print(f"Mnemonic: {mnemonic}\n")
    print("Originally in 2009, bitcoind (Bitcoin Core) used P2PKH (Pay-to-PubKey-Hash)\n")

    bip32_mst = Bip32Secp256k1.FromSeed(seed_bytes)

    original_p2pkh = compute_p2pkh_address(bip32_mst.PublicKey().RawCompressed().ToBytes())
    print(f"{original_p2pkh}  # Original (2009) - P2PKH - m")

    # Electrum uses m/0'/n
    electrum_ext = bip32_mst.ChildKey(0x80000000).ChildKey(0)
    electrum_addr = compute_p2pkh_address(electrum_ext.PublicKey().RawCompressed().ToBytes())
    print(f"{electrum_addr}  # Electrum (2011) - m/0'/0")

    # Bitcoin Core (pre-BIP32, ~2012) - using hardened derivation for all levels
    bitcoin_core_ext = bip32_mst.ChildKey(0x80000000).ChildKey(0x80000000).ChildKey(0x80000000)
    bitcoin_core_addr = compute_p2pkh_address(bitcoin_core_ext.PublicKey().RawCompressed().ToBytes())
    print(f"{bitcoin_core_addr}  # Bitcoin Core (2012) - m/0'/0'/0'")

    # BIP44 addresses
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_addr = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"{bip44_addr.PublicKey().ToAddress()}  # Legacy / Bitcoin Core (BIP44) (2014) - m/44'/0'/0'/0/0")

    # Multibit Classic used m/0'/0/n
    multibit_ext = bip32_mst.ChildKey(0x80000000).ChildKey(0).ChildKey(0)
    multibit_addr = compute_p2pkh_address(multibit_ext.PublicKey().RawCompressed().ToBytes())
    print(f"{multibit_addr}  # MultiBit Classic (2014) - m/0'/0/0")

    # Coinomi, Ledger, and Blockchain.info use m/44'/0'/0' as base path
    # According to bip39 website, first address is at m/44'/0'/0'/0
    # All three share the same derivation path and produce the same address
    bip44_variant_ext = bip32_mst.ChildKey(0x8000002C).ChildKey(0x80000000).ChildKey(0x80000000).ChildKey(0)
    bip44_variant_addr = compute_p2pkh_address(bip44_variant_ext.PublicKey().RawCompressed().ToBytes())
    print(f"{bip44_variant_addr}  # Coinomi (2014), Ledger (2014/2015), Blockchain.info (2015) (BIP44 variant) - m/44'/0'/0'/0")

    bip49_mst = Bip49.FromSeed(seed_bytes, Bip49Coins.BITCOIN)
    bip49_addr = bip49_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"{bip49_addr.PublicKey().ToAddress()}  # Nested SegWit (BIP49) (2016) - m/49'/0'/0'/0/0")

    bip84_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
    bip84_addr = bip84_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"{bip84_addr.PublicKey().ToAddress()}  # Native SegWit (BIP84) (2017) - m/84'/0'/0'/0/0")

    bip86_mst = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)
    bip86_addr = bip86_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"{bip86_addr.PublicKey().ToAddress()}  # Taproot (BIP86) (2021) - m/86'/0'/0'/0/0")


if __name__ == "__main__":
    main()
