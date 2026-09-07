from bip_utils import (
    Bip39SeedGenerator,
    Bip44, Bip44Coins, Bip44Changes,
    Bip49, Bip49Coins,
    Bip84, Bip84Coins,
    Bip86, Bip86Coins
)

mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Legacy (BIP44)
bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
bip44_addr = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
print(f"Legacy (BIP44):        {bip44_addr.PublicKey().ToAddress()}")

# Nested SegWit (BIP49)
bip49_mst = Bip49.FromSeed(seed_bytes, Bip49Coins.BITCOIN)
bip49_addr = bip49_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
print(f"Nested SegWit (BIP49): {bip49_addr.PublicKey().ToAddress()}")

# Native SegWit (BIP84)
bip84_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
bip84_addr = bip84_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
print(f"Native SegWit (BIP84): {bip84_addr.PublicKey().ToAddress()}")

# Taproot (BIP86)
bip86_mst = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)
bip86_addr = bip86_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
print(f"Taproot (BIP86):       {bip86_addr.PublicKey().ToAddress()}")