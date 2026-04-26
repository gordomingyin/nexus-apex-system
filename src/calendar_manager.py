# Calendar Manager Module
# Manages Apex Week and Reverse Day structures

class CalendarManager:
    def __init__(self):
        # Define the Apex Week structure
        self.apex_week = {
            "Monday": "Sunrise to Sunset",
            "Tuesday": "Sunrise to Sunset",
            "Wednesday": "Sunrise to Sunset",
            "Thursday": "Sunrise to Sunset",
            "Friday": "Admin Day with 4 structured sessions"
        }

        # Define Reverse Day overlays
        self.reverse_days = {
            "Wednesday": "Reverse Day: Sunrise to Sunset",
            "Friday": "Mid-afternoon evaluation (15-90 min)"
        }

    def display_apex_week(self):
        """Display the Apex Week schedule."""
        print("Apex Week Schedule:")
        for day, schedule in self.apex_week.items():
            print(f"{day}: {schedule}")

    def display_reverse_days(self):
        """Display the Reverse Day overlays."""
        print("Reverse Day Overlays:")
        for day, schedule in self.reverse_days.items():
            print(f"{day}: {schedule}")