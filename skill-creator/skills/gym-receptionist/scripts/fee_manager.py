#!/usr/bin/env python3
"""
Gym Fee Manager
Manages membership fees, payment tracking, reminders, and financial reports.
"""

import json
import datetime
import csv
from pathlib import Path

class GymFeeManager:
    def __init__(self, gym_name="Default Gym"):
        self.gym_name = gym_name
        self.data_file = Path("gym_fee_data.json")
        self.load_data()

    def load_data(self):
        """Load existing fee data"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "members": {},
                "payments": [],
                "fees": {},
                "reminders": []
            }

    def save_data(self):
        """Save fee data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def setup_fee_structure(self, fee_types):
        """Setup gym fee structure"""
        self.data["fees"] = fee_types
        self.save_data()
        print("Fee structure updated successfully!")

    def register_member_fee(self, member_id, fee_type, amount, start_date, billing_cycle="monthly"):
        """Register a member's fee plan"""
        if member_id not in self.data["members"]:
            print(f"Error: Member ID {member_id} not found!")
            return False

        # Calculate next due date
        start = datetime.datetime.fromisoformat(start_date)
        if billing_cycle == "monthly":
            next_due = start.replace(day=1)
            if start.month == 12:
                next_due = next_due.replace(year=start.year + 1, month=1)
            else:
                next_due = next_due.replace(month=start.month + 1)
        elif billing_cycle == "quarterly":
            next_due = start.replace(day=1)
            next_due = next_due.replace(month=start.month + 3)
        elif billing_cycle == "annually":
            next_due = start.replace(year=start.year + 1, month=1, day=1)
        else:
            next_due = start

        self.data["members"][member_id]["fee_plan"] = {
            "fee_type": fee_type,
            "amount": amount,
            "billing_cycle": billing_cycle,
            "start_date": start_date,
            "next_due_date": next_due.isoformat(),
            "status": "active"
        }

        self.save_data()
        print(f"Fee plan registered for {member_id}")
        return True

    def record_payment(self, member_id, amount, payment_date=None, payment_method="Cash"):
        """Record a payment from a member"""
        if member_id not in self.data["members"]:
            print(f"Error: Member ID {member_id} not found!")
            return False

        if payment_date is None:
            payment_date = datetime.datetime.now().isoformat()
        else:
            payment_date = datetime.datetime.fromisoformat(payment_date).isoformat()

        payment_record = {
            "member_id": member_id,
            "member_name": self.data["members"][member_id]["name"],
            "amount": amount,
            "payment_date": payment_date,
            "payment_method": payment_method,
            "status": "completed"
        }

        self.data["payments"].append(payment_record)

        # Update member's next due date
        if "fee_plan" in self.data["members"][member_id]:
            fee_plan = self.data["members"][member_id]["fee_plan"]
            current_due = datetime.datetime.fromisoformat(fee_plan["next_due_date"])

            # Calculate next due date
            if fee_plan["billing_cycle"] == "monthly":
                if current_due.month == 12:
                    next_due = current_due.replace(year=current_due.year + 1, month=1)
                else:
                    next_due = current_due.replace(month=current_due.month + 1)
            elif fee_plan["billing_cycle"] == "quarterly":
                next_due = current_due.replace(month=current_due.month + 3)
            elif fee_plan["billing_cycle"] == "annually":
                next_due = current_due.replace(year=current_due.year + 1)

            fee_plan["next_due_date"] = next_due.isoformat()

        self.save_data()
        print(f"Payment of ${amount} recorded for {member_id}")
        return True

    def check_overdue_payments(self, days_overdue=0):
        """Check for overdue payments"""
        current_date = datetime.datetime.now()
        overdue_members = []

        for member_id, member in self.data["members"].items():
            if "fee_plan" in member and member["fee_plan"]["status"] == "active":
                due_date = datetime.datetime.fromisoformat(member["fee_plan"]["next_due_date"])
                days_late = (current_date - due_date).days

                if days_late > days_overdue:
                    overdue_members.append({
                        "member_id": member_id,
                        "name": member["name"],
                        "fee_type": member["fee_plan"]["fee_type"],
                        "amount": member["fee_plan"]["amount"],
                        "due_date": member["fee_plan"]["next_due_date"],
                        "days_late": days_late,
                        "late_fee": max(0, days_late * 1)  # $1 per day late fee
                    })

        return overdue_members

    def send_payment_reminders(self, days_before=3):
        """Send payment reminders to members"""
        current_date = datetime.datetime.now()
        reminder_date = current_date + datetime.timedelta(days=days_before)

        reminders = []
        for member_id, member in self.data["members"].items():
            if "fee_plan" in member and member["fee_plan"]["status"] == "active":
                due_date = datetime.datetime.fromisoformat(member["fee_plan"]["next_due_date"])
                days_until_due = (due_date - current_date).days

                if 0 <= days_until_due <= days_before:
                    reminder = {
                        "member_id": member_id,
                        "name": member["name"],
                        "email": member["email"],
                        "due_date": member["fee_plan"]["next_due_date"],
                        "amount_due": member["fee_plan"]["amount"],
                        "days_until_due": days_until_due
                    }
                    reminders.append(reminder)

                    # Log reminder
                    reminder_log = {
                        "member_id": member_id,
                        "reminder_date": datetime.datetime.now().isoformat(),
                        "days_before_due": days_until_due,
                        "method": "email"
                    }
                    self.data["reminders"].append(reminder_log)

        self.save_data()
        return reminders

    def generate_payment_report(self, start_date=None, end_date=None):
        """Generate payment report for a date range"""
        if start_date is None:
            start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
        else:
            start_date = datetime.datetime.fromisoformat(start_date).isoformat()

        if end_date is None:
            end_date = datetime.datetime.now().isoformat()
        else:
            end_date = datetime.datetime.fromisoformat(end_date).isoformat()

        payments_in_range = [
            p for p in self.data["payments"]
            if start_date <= p["payment_date"] <= end_date
        ]

        total_revenue = sum(p["amount"] for p in payments_in_range)
        payment_methods = {}

        for payment in payments_in_range:
            method = payment["payment_method"]
            payment_methods[method] = payment_methods.get(method, 0) + payment["amount"]

        print(f"\n=== PAYMENT REPORT ===")
        print(f"Date Range: {start_date[:10]} to {end_date[:10]}")
        print(f"Total Payments: {len(payments_in_range)}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"\nPayment Methods:")
        for method, amount in payment_methods.items():
            percentage = (amount / total_revenue) * 100 if total_revenue > 0 else 0
            print(f"  {method}: ${amount:.2f} ({percentage:.1f}%)")

        return payments_in_range

    def get_member_balance(self, member_id):
        """Get member's payment history and balance"""
        if member_id not in self.data["members"]:
            return None

        member = self.data["members"][member_id]
        payments = [p for p in self.data["payments"] if p["member_id"] == member_id]
        payments.sort(key=lambda x: x["payment_date"], reverse=True)

        balance_info = {
            "member_id": member_id,
            "name": member["name"],
            "email": member["email"],
            "fee_plan": member.get("fee_plan", {}),
            "payment_history": payments,
            "total_paid": sum(p["amount"] for p in payments)
        }

        return balance_info

    def export_financial_report(self, filename="gym_financial_report.csv"):
        """Export financial data to CSV"""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["member_id", "name", "payment_date", "amount", "payment_method", "status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for payment in self.data["payments"]:
                writer.writerow(payment)

        print(f"Financial report exported to {filename}")

def main():
    """Interactive fee management system"""
    manager = GymFeeManager()

    # Setup default fee structure
    default_fees = {
        "basic_monthly": {"name": "Basic Monthly", "amount": 50.00, "cycle": "monthly"},
        "premium_monthly": {"name": "Premium Monthly", "amount": 80.00, "cycle": "monthly"},
        "basic_annual": {"name": "Basic Annual", "amount": 540.00, "cycle": "annually"},
        "premium_annual": {"name": "Premium Annual", "amount": 864.00, "cycle": "annually"}
    }

    manager.setup_fee_structure(default_fees)

    print("GYM FEE MANAGER")
    print("=" * 20)

    while True:
        print("\n1. Register Member Fee Plan")
        print("2. Record Payment")
        print("3. Check Overdue Payments")
        print("4. Send Payment Reminders")
        print("5. Generate Payment Report")
        print("6. Member Balance")
        print("7. Export Financial Report")
        print("8. Setup Fee Structure")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            member_id = input("Member ID: ")
            fee_type = input("Fee Type (basic_monthly/premium_monthly/etc.): ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            if fee_type in default_fees:
                amount = default_fees[fee_type]["amount"]
                billing_cycle = default_fees[fee_type]["cycle"]
                manager.register_member_fee(member_id, fee_type, amount, start_date, billing_cycle)
            else:
                amount = float(input("Amount: "))
                billing_cycle = input("Billing Cycle (monthly/quarterly/annually): ")
                manager.register_member_fee(member_id, fee_type, amount, start_date, billing_cycle)

        elif choice == '2':
            member_id = input("Member ID: ")
            amount = float(input("Payment Amount: "))
            payment_method = input("Payment Method (Cash/Card/Online): ") or "Cash"
            manager.record_payment(member_id, amount, None, payment_method)

        elif choice == '3':
            days_overdue = int(input("Check for payments overdue by how many days? (default: 0): ") or "0")
            overdue = manager.check_overdue_payments(days_overdue)
            print(f"\nFound {len(overdue)} overdue payments:")
            for payment in overdue:
                print(f"  {payment['name']}: ${payment['amount']} ({payment['days_late']} days late)")

        elif choice == '4':
            days_before = int(input("Send reminders how many days before due date? (default: 3): ") or "3")
            reminders = manager.send_payment_reminders(days_before)
            print(f"\nGenerated {len(reminders)} payment reminders")

        elif choice == '5':
            start = input("Start Date (YYYY-MM-DD) or press Enter for last 30 days: ")
            end = input("End Date (YYYY-MM-DD) or press Enter for today: ")
            manager.generate_payment_report(start or None, end or None)

        elif choice == '6':
            member_id = input("Member ID: ")
            balance = manager.get_member_balance(member_id)
            if balance:
                print(f"\nMember Balance for {balance['name']}:")
                print(f"  Total Paid: ${balance['total_paid']:.2f}")
                print(f"  Fee Plan: {balance['fee_plan'].get('fee_type', 'None')}")
                print(f"  Next Due: {balance['fee_plan'].get('next_due_date', 'N/A')}")
            else:
                print("Member not found!")

        elif choice == '7':
            filename = input("Export filename (default: gym_financial_report.csv): ") or "gym_financial_report.csv"
            manager.export_financial_report(filename)

        elif choice == '8':
            print("Current fee structure:")
            for fee_type, details in default_fees.items():
                print(f"  {fee_type}: ${details['amount']} ({details['cycle']})")

        elif choice == '9':
            print("Thanks for using Gym Fee Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()