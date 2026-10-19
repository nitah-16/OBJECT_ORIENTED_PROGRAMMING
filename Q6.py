# Question6_FinalSystem/main.py
import os


# 1. Main Integrated Class
class IntegratedStudentAccount:

    def __init__(self, name, reg_no, programme, balance, daily_limit=50000):
        # Encapsulation
        self.name = name  # Public
        self.reg_no = reg_no  # Public
        self._programme = programme  # Protected
        self.__balance = float(balance)  # Private
        self._daily_limit = float(daily_limit)

    # Property
    @property
    def balance(self):
        return self.__balance

    # Deposit Method
    def deposit(self, amount_input):
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
        except ValueError as e:
            print(f"[{self.name}] Deposit Error: {e}")
            return False
        else:
            self.__balance += amount
            self._log_transaction("DEPOSIT", amount, "BANK", self.__balance)
            print(
                f"[{self.name}] Deposit Success: UGX {amount:,} | Balance: UGX {self.__balance:,}"
            )
            return True

    # Payment Method
    def make_payment(self, amount_input, service_name):
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError("Payment must be positive.")
            if amount > self._daily_limit:
                raise ValueError("Payment exceeds daily limit.")
            if amount > self.__balance:
                raise ValueError("Insufficient balance.")
        except ValueError as e:
            print(f"[{self.name}] Transaction Failed: {e}")
            return False
        else:
            self.__balance -= amount
            self._log_transaction(
                "PAYMENT", amount, service_name, self.__balance
            )
            print(
                f"[{self.name}] Paid UGX {amount:,} for {service_name} | Balance: UGX {self.__balance:,}"
            )
            return True

    # Save Transaction to File
    def _log_transaction(
        self, trans_type, amount, service, remaining_balance
    ):
        record = f"{self.reg_no} | {trans_type} | {amount} | {service} | {remaining_balance}\n"
        with open("transactions.txt", "a") as f:
            f.write(record)

    def display_info(self):
        print(
            f"Account: {self.name} ({self.reg_no}) | Prog: {self._programme} | Balance: UGX {self.__balance:,}"
        )


def display_saved_history():
    print("\n================ SAVED TRANSACTION HISTORY ================")
    try:
        with open("transactions.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No historical file found.")
    print("===========================================================\n")


# REALISTIC INTEGRATED DEMONSTRATION
if __name__ == "__main__":
    # Clean file for clean test
    if os.path.exists("transactions.txt"):
        os.remove("transactions.txt")

    # a) Multiple Objects
    s1 = IntegratedStudentAccount(
        "Student A", "S21B13/001", "BSIT", 20000, daily_limit=50000
    )
    s2 = IntegratedStudentAccount(
        "Student B", "S21B13/002", "BSCS", 15000, daily_limit=50000
    )
    s3 = IntegratedStudentAccount(
        "Student C", "S21B13/003", "BSSE", 5000, daily_limit=10000
    )

    print("--- REALISTIC SCENARIO EXECUTION ---")
    # 1. Student A deposits money
    s1.deposit(30000)

    # 2. Student A pays for printing
    s1.make_payment(5000, "PRINTING")

    # 3. Student B pays for cafeteria service
    s2.make_payment(10000, "CAFETERIA")

    # 4. Student C attempts an invalid transaction (Exceeding balance)
    s3.make_payment(15000, "LAB_FEES")

    # 5. Display Transaction History saved in file
    display_saved_history()

    # 6. Final account states
    print("--- FINAL ACCOUNT STATES ---")
    s1.display_info()
    s2.display_info()
    s3.display_info()