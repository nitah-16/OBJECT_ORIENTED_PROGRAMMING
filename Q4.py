# Question4_Exceptions/reliable_account.py


class ReliableStudentAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount_input):
        try:
            # Safe numeric conversion
            amount = float(amount_input)
            # c) Custom Business Rule Exception
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
        except ValueError as e:
            print(f"Deposit Error: {e}")
        else:
            self.balance += amount
            print(
                f"Deposit successful! New Balance: UGX {self.balance:,.2f}"
            )
        finally:
            print("Deposit transaction attempt finished.")

    def make_payment(self, amount_input):
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError("Payment amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Payment exceeds available balance.")
        except ValueError as e:
            print(f"Payment Error: {e}")
            return False
        else:
            self.balance -= amount
            print(
                f"Payment successful! Remaining Balance: UGX {self.balance:,.2f}"
            )
            return True


# d) Demonstrating 5 Test Cases
if __name__ == "__main__":
    acc = ReliableStudentAccount("Anita", 50000)

    print("\n--- TEST CASE 1: Valid Deposit ---")
    acc.deposit(15000)

    print("\n--- TEST CASE 2: Invalid Negative Deposit ---")
    acc.deposit(-5000)

    print("\n--- TEST CASE 3: Valid Payment ---")
    acc.make_payment(20000)

    print("\n--- TEST CASE 4: Payment Exceeding Balance ---")
    acc.make_payment(100000)

    print("\n--- TEST CASE 5: Non-numeric Input ---")
    acc.deposit("five thousand")