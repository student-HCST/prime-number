import math

def analyze_prime(n):
    if n < 2:
        return {
            "number": n,
            "prime": False,
            "factors": [],
            "result": "Neither prime nor composite"
        }

    factors = [
        i for i in range(1, int(math.isqrt(n)) + 1)
        if n % i == 0
    ]

    all_factors = sorted({
        d for i in factors
        for d in (i, n // i)
    })

    is_prime = len(all_factors) == 2

    return {
        "number": n,
        "prime": is_prime,
        "factors": all_factors,
        "result": "Prime" if is_prime else "Composite"
    }


def main():
    print("=== PRIME NUMBER ANALYZER ===")

    try:
        n = int(input("Enter a positive integer: "))
        result = analyze_prime(n)

        print(f"\nNumber: {result['number']}")
        print(f"Classification: {result['result']}")
        print(f"Factors: {result['factors']}")

        if result["prime"]:
            print("It has exactly two positive factors.")
        elif n >= 2:
            print("It has more than two positive factors.")

        limit = int(input("\nAnalyze primes up to: "))
        if limit >= 2:
            primes = [
                x for x in range(2, limit + 1)
                if analyze_prime(x)["prime"]
            ]
            print("Prime numbers:", primes)
            print("Total primes:", len(primes))

    except ValueError:
        print("Please enter valid integers.")


if __name__ == "__main__":
    main()

