# Question5_FileHandling/transactions.py
import os


class PersistentTransactionManager:

    def __init__(self, filename="transactions.txt"):
        self.filename = filename

    # b) Save Transactions
    def save_transaction(
        self, reg_num, trans_type, amount, service, remaining_balance
    ):
        record = f"{reg_num} | {trans_type} | {amount} | {service} | {remaining_balance}\n"
        # Using 'a' mode to append without overwriting
        with open(self.filename, "a") as file:
            file.write(record)
        print("Transaction persisted to storage.")

    # c) & d) Read Previous Transactions with Missing File Handling
    def read_transactions(self):
        print(f"\n--- Transaction History ({self.filename}) ---")
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
                if not records:
                    print("No recorded transactions found.")
                for line in records:
                    print(line.strip())
        except FileNotFoundError:
            print(
                f"File '{self.filename}' does not exist yet. No past records to show."
            )


# e) Demonstration
if __name__ == "__main__":
    tm = PersistentTransactionManager()

    # Read prior to creation
    tm.read_transactions()

    # Save transaction
    tm.save_transaction("S21B13/001", "PAYMENT", 5000, "CAFETERIA", 25000)

    # Read stored data
    tm.read_transactions()