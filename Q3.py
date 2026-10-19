# Question3_Properties/controlled_account.py


class StudentAccount:

    def __init__(
        self,
        student_name,
        reg_number,
        programme,
        initial_balance,
        daily_limit=50000.0,
    ):
        self.student_name = student_name
        self.reg_number = reg_number
        self._programme = programme
        self.__balance = initial_balance
        self._daily_limit = daily_limit
        self._transaction_count = 0  # Internal transaction counter

    # a) Classic Getter
    def get_balance(self):
        return self.__balance

    # b) Classic Setter with Validation
    def set_programme(self, new_programme):
        if isinstance(new_programme, str) and new_programme.strip() != "":
            self._programme = new_programme
            print(f"Programme updated to: {self._programme}")
        else:
            print("Error: Invalid programme name! Value preserved.")

    # d) Refactored Attribute using @property Syntax
    @property
    def daily_limit(self):
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, value):
        if value >= 0:
            self._daily_limit = value
        else:
            print("Error: Daily limit cannot be negative! Value preserved.")

    # e) Read-Only Property (Getter only, no setter)
    @property
    def transaction_count(self):
        return self._transaction_count

    def perform_action(self):
        self._transaction_count += 1


# --- DEMONSTRATION ---
if __name__ == "__main__":
    acc = StudentAccount("Anita", "BSIT/01", "BSIT", 50000, 30000)

    # Getter and Setter tests
    print("Balance via Classic Getter:", acc.get_balance())
    acc.set_programme("")  # Invalid: Preserves old value
    acc.set_programme("BSSE")  # Valid

    # Property tests
    print("Initial Daily Limit:", acc.daily_limit)
    acc.daily_limit = 45000  # Valid setter
    print("Updated Daily Limit:", acc.daily_limit)
    acc.daily_limit = -10000  # Invalid setter attempt
    print("Daily Limit after invalid attempt:", acc.daily_limit)

    # Read-Only Property test
    print("Transaction Count:", acc.transaction_count)
    acc.perform_action()
    print("Transaction Count after action:", acc.transaction_count)
    try:
        acc.transaction_count = 10  # Attempting illegal modification
    except AttributeError as e:
        print("Read-only protection working:", e)