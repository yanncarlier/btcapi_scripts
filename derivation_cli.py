"""Shared command-line arguments for the individual address derivation scripts."""

from __future__ import annotations

import argparse


DEFAULT_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"


def positive_count(value: str) -> int:
    """Parse an address count that is greater than zero."""
    count = int(value)
    if count < 1:
        raise argparse.ArgumentTypeError("number of addresses must be at least 1")
    return count


def parse_derivation_arguments(description: str) -> tuple[str, int]:
    """Return the optional BIP39 mnemonic and address count supplied by the user."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "mnemonic",
        nargs="?",
        default=DEFAULT_MNEMONIC,
        help="quoted 12- or 24-word BIP39 mnemonic; defaults to the public test mnemonic",
    )
    parser.add_argument(
        "count",
        nargs="?",
        default=1,
        type=positive_count,
        help="number of addresses to derive (default: 1)",
    )
    arguments = parser.parse_args()
    return arguments.mnemonic, arguments.count
