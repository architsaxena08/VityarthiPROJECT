# COLLEGE TASK MANAGER 


class HostelTaskManager:
    """Handles everything - tasks, chores, laundry, expenses, mess menu entirely in memory."""

    def __init__(self):
        self.data = self._init_default_state()

    def _init_default_state(self):
        return {
            "tasks": [],
            "chores": [],
            "expenses": [],
            "mess_menu": {
                "Monday": {"Breakfast": "Poha, Tea", "Lunch": "Dal, Rice, Roti, Sabzi", "Dinner": "Paneer, Roti, Rice"},
                "Tuesday": {"Breakfast": "Idli, Sambar", "Lunch": "Rajma, Chawal, Roti", "Dinner": "Egg Curry / Kofta, Rice"},
                "Wednesday": {"Breakfast": "Paratha, Curd", "Lunch": "Chole, Bhature/Rice", "Dinner": "Mix Veg, Dal Tadka"},
                "Thursday": {"Breakfast": "Upma, Chutney", "Lunch": "Kadhi, Rice, Roti", "Dinner": "Aloo Gobhi, Dal Fry"},
                "Friday": {"Breakfast": "Puri, Bhaji", "Lunch": "Dal Makhani, Jeera Rice", "Dinner": "Special Pulao, Raita"},
                "Saturday": {"Breakfast": "Sandwich, Milk", "Lunch": "Khichdi, Papad, Dahi", "Dinner": "Soyabean Curry, Roti"},
                "Sunday": {"Breakfast": "Chole Bhature", "Lunch": "Special Biryani/Thali", "Dinner": "Light Khichdi / Roti"},
            },
            "laundry_records": [],
        }

    # ---------------------------------------------------------------
    # Tasks (assignments, exams, whatever)
    # ---------------------------------------------------------------
    def add_task(self, title, category, due_date, priority):
        task = {
            "id": len(self.data["tasks"]) + 1,
            "title": title,
            "category": category,
            "due_date": due_date,
            "priority": priority.upper(),
            "completed": False,
        }
        self.data["tasks"].append(task)
        print(f"\n[+] Task '{title}' saved successfully under [{category}].")

    def view_tasks(self, filter_category=None):
        tasks = self.data["tasks"]
        if filter_category:
            tasks = [t for t in tasks if t["category"].lower() == filter_category.lower()]

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n" + "=" * 76)
        print(f"{'ID':<4} | {'Status':<8} | {'Priority':<8} | {'Category':<10} | {'Due Date':<12} | {'Title'}")
        print("-" * 76)
        for t in tasks:
            status = "[x] Done" if t["completed"] else "[ ] Open"
            print(f"{t['id']:<4} | {status:<8} | {t['priority']:<8} | {t['category']:<10} | {t['due_date']:<12} | {t['title']}")
        print("=" * 76)

    def mark_completed(self, task_id):
        for task in self.data["tasks"]:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"\n[+] Task {task_id} marked as completed!")
                return
        print(f"\n[-] Task ID {task_id} not found.")

    # ---------------------------------------------------------------
    # Room chores - so nobody "forgets" it's their turn for the dustbin
    # ---------------------------------------------------------------
    def add_chore_rotation(self, chore_name, roommates):
        chore = {
            "name": chore_name,
            "roommates": [r.strip() for r in roommates.split(",")],
            "current_turn": 0,
        }
        self.data["chores"].append(chore)
        print(f"\n[+] Chore '{chore_name}' added with rotation: {chore['roommates']}")

    def rotate_chore(self, chore_index):
        if 0 <= chore_index < len(self.data["chores"]):
            chore = self.data["chores"][chore_index]
            chore["current_turn"] = (chore["current_turn"] + 1) % len(chore["roommates"])
            assigned_to = chore["roommates"][chore["current_turn"]]
            print(f"\n[+] Turn updated! Next person responsible for '{chore['name']}': {assigned_to}")
        else:
            print("\n[-] Invalid chore index.")

    def view_chores(self):
        if not self.data["chores"]:
            print("\nNo chores configured yet.")
            return
        print("\n--- Room Chore Rotations ---")
        for idx, chore in enumerate(self.data["chores"]):
            current_person = chore["roommates"][chore["current_turn"]]
            print(f"[{idx}] {chore['name']} -> Current Turn: **{current_person}** (Team: {', '.join(chore['roommates'])})")

    # ---------------------------------------------------------------
    # Mess menu
    # ---------------------------------------------------------------
    def view_mess_menu(self, day=None):
        if day:
            day_title = day.capitalize()
            meals = self.data["mess_menu"].get(day_title)
            if meals:
                print(f"\n--- Mess Menu: {day_title} ---")
                for meal_type, items in meals.items():
                    print(f"• {meal_type:<10}: {items}")
            else:
                print("[-] Invalid day entered.")
        else:
            print("\n--- Weekly Mess Menu ---")
            for d, meals in self.data["mess_menu"].items():
                print(f"\n[{d}]")
                for meal_type, items in meals.items():
                    print(f"  {meal_type:<10}: {items}")

    def update_mess_menu(self, day, meal_type, items):
        day_title = day.capitalize()
        meal_title = meal_type.capitalize()
        if day_title in self.data["mess_menu"]:
            self.data["mess_menu"][day_title][meal_title] = items
            print(f"\n[+] Updated {day_title} {meal_title} to: {items}")
        else:
            print("[-] Invalid day of the week.")

    # ---------------------------------------------------------------
    # Laundry tracker
    # ---------------------------------------------------------------
    def add_laundry_drop(self, token_or_tag, cloth_count, drop_date, pickup_date):
        drop = {
            "id": len(self.data["laundry_records"]) + 1,
            "tag": token_or_tag,
            "count": cloth_count,
            "drop_date": drop_date,
            "pickup_date": pickup_date,
            "collected": False,
        }
        self.data["laundry_records"].append(drop)
        print(f"\n[+] Laundry lot #{drop['id']} recorded. Ready for pickup on {pickup_date}.")

    def view_laundry(self):
        records = self.data["laundry_records"]
        if not records:
            print("\nNo laundry batches recorded.")
            return

        print("\n--- Laundry Batches ---")
        print(f"{'ID':<4} | {'Status':<10} | {'Token/Tag':<12} | {'Pieces':<8} | {'Dropped On':<12} | {'Pickup Due'}")
        print("-" * 65)
        for r in records:
            status = "Collected" if r["collected"] else "At Dhobi"
            print(f"{r['id']:<4} | {status:<10} | {r['tag']:<12} | {r['count']:<8} | {r['drop_date']:<12} | {r['pickup_date']}")

    def mark_laundry_collected(self, lot_id):
        for r in self.data["laundry_records"]:
            if r["id"] == lot_id:
                r["collected"] = True
                print(f"\n[+] Laundry batch #{lot_id} marked as collected!")
                return
        print(f"\n[-] Laundry lot #{lot_id} not found.")

    # ---------------------------------------------------------------
    # Expense splitter
    # ---------------------------------------------------------------
    def add_expense(self, desc, total_amount, paid_by, num_roommates, date_str):
        per_person = round(total_amount / num_roommates, 2)
        expense = {
            "desc": desc,
            "total": total_amount,
            "paid_by": paid_by,
            "per_person": per_person,
            "date": date_str,
        }
        self.data["expenses"].append(expense)
        print(f"\n[+] Added: {desc} (Total: {total_amount}). Split: {per_person} per person to {paid_by}.")

    def view_expenses(self):
        if not self.data["expenses"]:
            print("\nNo shared expenses recorded.")
            return
        print("\n--- Shared Expenses ---")
        for exp in self.data["expenses"]:
            print(f"[{exp['date']}] {exp['desc']} | Total: {exp['total']} | Paid By: {exp['paid_by']} | Per Head: {exp['per_person']}")


def handle_hostel_options(manager):
    """The 'everything about hostel life' submenu."""
    while True:
        print("\n=== Hostel Life Hub ===")
        print("1. Mess Menu - View Today / Specific Day")
        print("2. Mess Menu - View Complete Week")
        print("3. Mess Menu - Edit a Meal")
        print("4. Laundry - Log New Drop (Token & Clothes Count)")
        print("5. Laundry - View Pending & Past Pickups")
        print("6. Laundry - Mark Clothes as Collected")
        print("7. Chores - View Room Duty Rotation")
        print("8. Chores - Add or Rotate Turn")
        print("9. Back to Main Menu")

        choice = input("\nSelect hostel feature (1-9): ").strip()

        if choice == "1":
            day = input("Enter day (e.g., Monday, Tuesday): ").strip()
            manager.view_mess_menu(day)

        elif choice == "2":
            manager.view_mess_menu()

        elif choice == "3":
            day = input("Enter day: ").strip()
            meal = input("Meal type (Breakfast/Lunch/Dinner): ").strip()
            items = input("Updated food items: ").strip()
            manager.update_mess_menu(day, meal, items)

        elif choice == "4":
            token = input("Laundry Slip / Token Number: ").strip() or "No-Slip"
            while True:
                raw_count = input("Total number of clothes: ").strip()
                try:
                    count = int(raw_count)
                    break
                except ValueError:
                    print("[-] That's not a number, try again.")
            drop_date = input("Drop date (DD-MM-YYYY) [press Enter for 'Today']: ").strip() or "Today"
            pickup = input("Expected pickup date (DD-MM-YYYY): ").strip()
            manager.add_laundry_drop(token, count, drop_date, pickup)

        elif choice == "5":
            manager.view_laundry()

        elif choice == "6":
            manager.view_laundry()
            try:
                lot_id = int(input("Enter laundry batch ID to mark collected: "))
                manager.mark_laundry_collected(lot_id)
            except ValueError:
                print("[-] Enter a valid numeric ID.")

        elif choice == "7":
            manager.view_chores()

        elif choice == "8":
            print("a. Add a new chore rotation")
            print("b. Rotate turn (pass duty to next roommate)")
            sub = input("Select (a/b): ").strip().lower()
            if sub == "a":
                cname = input("Chore name (e.g., Water Dispenser Can, Room Dusting): ").strip()
                names = input("Roommates comma-separated (e.g., Rohan, Aman, Dev): ").strip()
                manager.add_chore_rotation(cname, names)
            elif sub == "b":
                manager.view_chores()
                try:
                    idx = int(input("Enter index to rotate: "))
                    manager.rotate_chore(idx)
                except ValueError:
                    print("[-] Enter a valid numeric index.")
            else:
                print("[-] Invalid sub-option.")

        elif choice == "9":
            break

        else:
            print("[-] Invalid option.")


def main():
    manager = HostelTaskManager()

    while True:
        print("\n=== College Student Task Manager ===")
        print("1. Add New Task")
        print("2. View Tasks (Academics / Exams / Personal)")
        print("3. Mark Task as Done")
        print("4. Hostel Options (Mess Menu, Laundry, Chores)")
        print("5. Room Expense Distribution")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            category = input("Category (Academic / Lab / Hostel / Personal): ").strip() or "Academic"
            due_date = input("Due date (DD-MM-YYYY): ").strip() or "No Due Date"
            priority = input("Priority (HIGH / MED / LOW): ").strip() or "MED"
            manager.add_task(title, category, due_date, priority)

        elif choice == "2":
            cat = input("Filter category (Academic/Hostel/Exam, or press Enter for all): ").strip()
            manager.view_tasks(filter_category=cat if cat else None)

        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to complete: "))
                manager.mark_completed(task_id)
            except ValueError:
                print("[-] Please enter a valid number.")

        elif choice == "4":
            handle_hostel_options(manager)

        elif choice == "5":
            print("\n--- Shared Expenses ---")
            print("a. View past splits")
            print("b. Add new room expense")
            sub = input("Select (a/b): ").strip().lower()
            if sub == "a":
                manager.view_expenses()
            elif sub == "b":
                desc = input("Expense title (e.g., Night Canteen, Water Can): ").strip()
                try:
                    amt = float(input("Total cost: "))
                    payer = input("Who covered it?: ").strip()
                    count = int(input("Number of roommates sharing: "))
                    if count <= 0:
                        print("[-] Roommate count has to be at least 1.")
                    else:
                        exp_date = input("Expense date (DD-MM-YYYY) [press Enter for 'Today']: ").strip() or "Today"
                        manager.add_expense(desc, amt, payer, count, exp_date)
                except ValueError:
                    print("[-] Invalid input for amount or member count.")
            else:
                print("[-] Invalid sub-option.")

        elif choice == "6":
            print("\nExiting. Best of luck with college and hostel life!")
            break

        else:
            print("[-] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()