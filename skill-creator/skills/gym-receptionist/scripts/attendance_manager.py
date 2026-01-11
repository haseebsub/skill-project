#!/usr/bin/env python3
"""
Gym Attendance Manager
Tracks member attendance, generates reports, and manages check-in/check-out processes.
"""

import json
import datetime
import csv
from pathlib import Path

class GymAttendanceManager:
    def __init__(self, gym_name="Default Gym"):
        self.gym_name = gym_name
        self.data_file = Path("gym_attendance_data.json")
        self.load_data()

    def load_data(self):
        """Load existing attendance data"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "members": {},
                "attendance": [],
                "check_ins": {}
            }

    def save_data(self):
        """Save attendance data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def register_member(self, member_id, name, membership_type, phone, email):
        """Register a new member"""
        self.data["members"][member_id] = {
            "name": name,
            "membership_type": membership_type,
            "phone": phone,
            "email": email,
            "join_date": datetime.datetime.now().isoformat(),
            "total_visits": 0,
            "last_visit": None
        }
        self.save_data()
        print(f"Member {name} (ID: {member_id}) registered successfully!")

    def check_in(self, member_id):
        """Check member into gym"""
        if member_id not in self.data["members"]:
            print(f"Error: Member ID {member_id} not found!")
            return False

        current_time = datetime.datetime.now()
        member = self.data["members"][member_id]

        # Check if already checked in
        if member_id in self.data["check_ins"]:
            print(f"Error: {member['name']} is already checked in!")
            return False

        # Record check-in
        self.data["check_ins"][member_id] = {
            "name": member["name"],
            "check_in_time": current_time.isoformat(),
            "membership_type": member["membership_type"]
        }

        # Record attendance
        attendance_record = {
            "member_id": member_id,
            "name": member["name"],
            "check_in": current_time.isoformat(),
            "check_out": None,
            "duration": 0,
            "date": current_time.strftime("%Y-%m-%d")
        }
        self.data["attendance"].append(attendance_record)

        # Update member stats
        member["total_visits"] += 1
        member["last_visit"] = current_time.isoformat()
        self.save_data()

        print(f"Welcome {member['name']}! Checked in at {current_time.strftime('%H:%M')}")
        return True

    def check_out(self, member_id):
        """Check member out of gym"""
        if member_id not in self.data["check_ins"]:
            print(f"Error: Member ID {member_id} is not checked in!")
            return False

        current_time = datetime.datetime.now()
        check_in_record = self.data["check_ins"][member_id]
        member = self.data["members"][member_id]

        # Find attendance record
        for record in self.data["attendance"]:
            if record["member_id"] == member_id and record["check_out"] is None:
                check_in_time = datetime.datetime.fromisoformat(record["check_in"])
                duration = (current_time - check_in_time).total_seconds() / 3600
                record["check_out"] = current_time.isoformat()
                record["duration"] = round(duration, 2)
                break

        # Remove from check-ins
        del self.data["check_ins"][member_id]
        self.save_data()

        print(f"Goodbye {member['name']}! Session duration: {record['duration']} hours")
        return True

    def get_member_status(self, member_id):
        """Get member's current status and statistics"""
        if member_id not in self.data["members"]:
            return None

        member = self.data["members"][member_id]
        is_checked_in = member_id in self.data["check_ins"]

        # Calculate monthly visits
        current_month = datetime.datetime.now().strftime("%Y-%m")
        monthly_visits = sum(1 for record in self.data["attendance"]
                           if record["member_id"] == member_id and
                           record["date"].startswith(current_month))

        return {
            "name": member["name"],
            "membership_type": member["membership_type"],
            "total_visits": member["total_visits"],
            "monthly_visits": monthly_visits,
            "last_visit": member.get("last_visit"),
            "is_checked_in": is_checked_in,
            "phone": member["phone"],
            "email": member["email"]
        }

    def generate_daily_report(self, date=None):
        """Generate daily attendance report"""
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        daily_attendance = [record for record in self.data["attendance"]
                          if record["date"] == date]

        print(f"\n=== DAILY ATTENDANCE REPORT - {date} ===")
        print(f"Total Visitors: {len(daily_attendance)}")

        # Group by hour
        hourly_stats = {}
        for record in daily_attendance:
            check_in = datetime.datetime.fromisoformat(record["check_in"])
            hour = check_in.hour
            hourly_stats[hour] = hourly_stats.get(hour, 0) + 1

        print("\nPeak Hours:")
        for hour in sorted(hourly_stats.keys()):
            print(f"  {hour:02d}:00 - {hourly_stats[hour]} visitors")

        return daily_attendance

    def generate_monthly_report(self, month=None):
        """Generate monthly attendance report"""
        if month is None:
            month = datetime.datetime.now().strftime("%Y-%m")

        monthly_attendance = [record for record in self.data["attendance"]
                            if record["date"].startswith(month)]

        print(f"\n=== MONTHLY ATTENDANCE REPORT - {month} ===")

        # Member statistics
        member_stats = {}
        for record in monthly_attendance:
            member_id = record["member_id"]
            if member_id not in member_stats:
                member_stats[member_id] = {
                    "name": record["name"],
                    "visits": 0,
                    "total_duration": 0
                }
            member_stats[member_id]["visits"] += 1
            member_stats[member_id]["total_duration"] += record["duration"]

        print(f"Total Visits: {len(monthly_attendance)}")
        print(f"Unique Members: {len(member_stats)}")

        print("\nTop Members by Visits:")
        sorted_members = sorted(member_stats.items(),
                              key=lambda x: x[1]["visits"],
                              reverse=True)
        for i, (member_id, stats) in enumerate(sorted_members[:10], 1):
            avg_duration = stats["total_duration"] / stats["visits"]
            print(f"  {i}. {stats['name']}: {stats['visits']} visits (avg: {avg_duration:.1f}h)")

        return monthly_attendance

    def export_to_csv(self, filename="gym_attendance_export.csv"):
        """Export attendance data to CSV"""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["member_id", "name", "check_in", "check_out", "duration", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for record in self.data["attendance"]:
                writer.writerow(record)

        print(f"Data exported to {filename}")

    def get_current_checkins(self):
        """Get list of currently checked-in members"""
        current_time = datetime.datetime.now()
        print(f"\n=== CURRENTLY CHECKED IN - {current_time.strftime('%Y-%m-%d %H:%M')} ===")

        if not self.data["check_ins"]:
            print("No members currently checked in.")
            return []

        for member_id, check_in_info in self.data["check_ins"].items():
            check_in_time = datetime.datetime.fromisoformat(check_in_info["check_in_time"])
            duration = (current_time - check_in_time).total_seconds() / 3600
            print(f"  {check_in_info['name']} ({check_in_info['membership_type']})")
            print(f"    Check-in: {check_in_info['check_in_time']}")
            print(f"    Duration: {duration:.1f} hours")

        return list(self.data["check_ins"].keys())

def main():
    """Interactive attendance management system"""
    manager = GymAttendanceManager()

    print("GYM ATTENDANCE MANAGER")
    print("=" * 30)

    while True:
        print("\n1. Register Member")
        print("2. Check In")
        print("3. Check Out")
        print("4. Member Status")
        print("5. Daily Report")
        print("6. Monthly Report")
        print("7. Current Check-ins")
        print("8. Export Data")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            member_id = input("Member ID: ")
            name = input("Full Name: ")
            membership_type = input("Membership Type: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.register_member(member_id, name, membership_type, phone, email)

        elif choice == '2':
            member_id = input("Member ID: ")
            manager.check_in(member_id)

        elif choice == '3':
            member_id = input("Member ID: ")
            manager.check_out(member_id)

        elif choice == '4':
            member_id = input("Member ID: ")
            status = manager.get_member_status(member_id)
            if status:
                print(f"\nMember Status:")
                print(f"  Name: {status['name']}")
                print(f"  Membership: {status['membership_type']}")
                print(f"  Total Visits: {status['total_visits']}")
                print(f"  Monthly Visits: {status['monthly_visits']}")
                print(f"  Checked In: {'Yes' if status['is_checked_in'] else 'No'}")
            else:
                print("Member not found!")

        elif choice == '5':
            date = input("Date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                manager.generate_daily_report()
            else:
                manager.generate_daily_report(date)

        elif choice == '6':
            month = input("Month (YYYY-MM) or press Enter for current month: ")
            if not month:
                manager.generate_monthly_report()
            else:
                manager.generate_monthly_report(month)

        elif choice == '7':
            manager.get_current_checkins()

        elif choice == '8':
            filename = input("Export filename (default: gym_attendance_export.csv): ") or "gym_attendance_export.csv"
            manager.export_to_csv(filename)

        elif choice == '9':
            print("Thanks for using Gym Attendance Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()