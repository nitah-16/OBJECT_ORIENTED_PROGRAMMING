# Question2_Encapsulation/student_account.py


class StudentAccount:
    institution_name = "Uganda Christian University"

    def __init__(
        self,
        student_name,
        reg_number,
        programme,
        initial_balance,
        pin,
        daily_limit=50000.0,
    ):
    
        self.student_name = student_name
        self.reg_number = reg_number

        
        self._programme = programme
        self._daily_spending_limit = daily_limit

        
        self.__balance = initial_balance
        self.__transaction_pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(
                f"[{self.student_name}] Deposited: UGX {amount:,} | New Balance: UGX {self.__balance:,}"
            )
        else:
            print("Invalid deposit amount.")

    def make_payment(self, amount, service_name):
        if amount <= 0:
            print("Payment amount must be positive.")
            return False
        if amount > self._daily_spending_limit:
            print(
                f"[{self.student_name}] Failed: Exceeds daily limit of UGX {self._daily_spending_limit:,}"
            )
            return False
        if amount > self.__balance:
            print(f"[{self.student_name}] Failed: Insufficient balance.")
            return False

        self.__balance -= amount
        print(
            f"[{self.student_name}] Paid UGX {amount:,} for {service_name} | Remaining: UGX {self.__balance:,}"
        )
        return True

    def display_summary(self):
        print(f"\n--- Account Summary ({StudentAccount.institution_name}) ---")
        print(
            f"Student: {self.student_name} | Reg No: {self.reg_number} | Prog: {self._programme}"
        )
        print(
            f"Balance: UGX {self.__balance:,} | Daily Limit: UGX {self._daily_spending_limit:,}\n"
        )


# --- DEMONSTRATION & INVESTIGATION ---
if __name__ == "__main__":
    # b) Three different objects
    acc1 = StudentAccount(
        "Anita", "BSIT/01", "BSIT", 100000, "1234", daily_limit=30000
    )
    acc2 = StudentAccount(
        "Kizito", "BSCS/02", "BSCS", 50000, "5678", daily_limit=20000
    )
    acc3 = StudentAccount(
        "Muwanguzi", "BSSE/03", "BSSE", 200000, "9999", daily_limit=100000
    )

    # c) Independent object state demonstration
    acc1.deposit(20000)
    acc2.make_payment(10000, "Cafeteria")
    acc1.display_summary()
    acc2.display_summary()

    # d) Encapsulation Investigation
    print("Public:", acc1.student_name)  # Accessible directly
    print(
        "Protected:", acc1._programme
    )  # Accessible, but by convention shouldn't be edited directly

    try:
        print(acc1.__balance)  # Raises AttributeError
    except AttributeError as e:
        print("Private direct access failed as expected:", e)

    # e) Name Mangling Demonstration
    # Python internally renames __balance to _ClassName__attribute
    print(
        "Accessed via Name Mangling:", acc1._StudentAccount__balance
    )  # Proves it's not encrypted!