"""Finite exact-arithmetic consistency checks for MF-MATH-2026-01.

These checks support reproducibility of the formulas and figure generator. They
are not a substitute for the general proofs in the manuscript.
"""

from fractions import Fraction
from itertools import product


def odd_term(n: int) -> Fraction:
    return Fraction(8 * n + 17, 4**n)


def even_term(n: int) -> Fraction:
    return Fraction(4 * n + 18, 4**n)


def pair_digits(n: int) -> tuple[int, int, int, int]:
    return (0, 4 * n + 18, 8 * n + 17, 12 * n + 35)


def even_tail(n: int) -> Fraction:
    return Fraction(4 * n + 17, 4**n)


def verify_elementary_identities(limit: int = 10_000) -> None:
    for n in range(1, limit + 1):
        a = odd_term(n)
        b = even_term(n)
        assert a > b > 0
        assert b > odd_term(n + 1)
        assert a + b == Fraction(12 * n + 35, 4**n)
        assert b - even_tail(n) == Fraction(1, 4**n)

        within_error = b / a - Fraction(1, 2)
        transition_error = odd_term(n + 1) / b - Fraction(1, 2)
        assert within_error == Fraction(19, 2 * (8 * n + 17))
        assert transition_error == Fraction(-11, 16 * n + 72)

    # Exact finite-sum-plus-tail identity: sum of first N pairs + r_{2N} = 17.
    partial = Fraction(0)
    for n in range(1, limit + 1):
        partial += odd_term(n) + even_term(n)
        assert partial + even_tail(n) == 17


def verify_residue_bijection(max_level: int = 8) -> None:
    for level in range(1, max_level + 1):
        residues: set[int] = set()
        modulus = 4**level
        digit_sets = [pair_digits(n) for n in range(1, level + 1)]
        for digit_string in product(*digit_sets):
            value = sum(
                digit * 4 ** (level - index)
                for index, digit in enumerate(digit_string, start=1)
            )
            residues.add(value % modulus)
        assert residues == set(range(modulus))


def main() -> None:
    verify_elementary_identities()
    verify_residue_bijection()
    print("All exact-arithmetic consistency checks passed.")


if __name__ == "__main__":
    main()
