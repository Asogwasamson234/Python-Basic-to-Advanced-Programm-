# # Simple Interest Calculator


def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest based on principal, rate, and time."""
    si = (principal * rate * time) / 100
    return si


if __name__ == "__main__":
    # Example usage
    principal = input("Enter the principal amount: ")
    rate = input("Enter the rate amount: ")
    time = input("Enter the time (in years): ")
    simple_interest = calculate_simple_interest(
        float(principal), float(rate), float(time)
    )
    print(f"Simple Interest = {simple_interest}")
