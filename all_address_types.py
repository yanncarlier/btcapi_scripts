import argparse

from bip_utils import (
    Bip39SeedGenerator,
    Bip44, Bip44Coins, Bip44Changes,
    Bip49, Bip49Coins,
    Bip84, Bip84Coins,
    Bip86, Bip86Coins,
    Bip39MnemonicValidator,
)
from bip_utils.utils.mnemonic import MnemonicChecksumError

DEFAULT_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"


def main():
    parser = argparse.ArgumentParser(description="Generate Bitcoin addresses from a BIP39 mnemonic.")
    parser.add_argument("mnemonic", nargs="?", default=DEFAULT_MNEMONIC,
                        help="BIP39 mnemonic phrase (24 words). If omitted, uses a default test phrase.")
    args = parser.parse_args()

    mnemonic = args.mnemonic.strip()

    try:
        Bip39MnemonicValidator().Validate(mnemonic)
    except MnemonicChecksumError:
        raise ValueError("Invalid mnemonic phrase. Please provide a valid BIP39 mnemonic (12 or 24 words).")

    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    print(f"Mnemonic: {mnemonic}\n")

    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_addr = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Legacy (BIP44):        {bip44_addr.PublicKey().ToAddress()}")

    bip49_mst = Bip49.FromSeed(seed_bytes, Bip49Coins.BITCOIN)
    bip49_addr = bip49_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Nested SegWit (BIP49): {bip49_addr.PublicKey().ToAddress()}")

    bip84_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
    bip84_addr = bip84_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Native SegWit (BIP84): {bip84_addr.PublicKey().ToAddress()}")

    bip86_mst = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)
    bip86_addr = bip86_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Taproot (BIP86):       {bip86_addr.PublicKey().ToAddress()}")

    print("\n--- Network Extensions ---")

    testnet_bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_TESTNET)
    testnet_bip44_addr = testnet_bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Testnet (BIP44):       {testnet_bip44_addr.PublicKey().ToAddress()}")

    regtest_bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_REGTEST)
    regtest_bip44_addr = regtest_bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    print(f"Regtest (BIP44):       {regtest_bip44_addr.PublicKey().ToAddress()}")


if __name__ == "__main__":
    main()
