from enum import Enum
import uuid
import Utils
import Storage
from abc import ABC


class Habit(ABC):
    """_summary_"""

    def __init__(self, name, description, periodicity):
        """Constructs all the necessary attributes for the habit object."""
        self.id = uuid.uuid4().hex
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created = Utils.get_timestamp()
        self.check_off_list = list()

    def check_off(self, date):
        """Mark the habit as completed (checked-off)."""
        self.check_off_list.append(date)
        return self.check_off_list

    def create_habit(self):
        """Create the habit in the database."""
        pass

    def display_habit(self):
        """Display the habit."""
        pass

    def delete_habit(self):
        """Delete the habit."""
        pass

    def analyze_habit(self):
        """Analyze the habit."""
        pass

    def store_habit(self):
        """Store the habit in the database."""
        pass

    def modify_habit(self):
        """Modify the habit."""
        pass

    def __repr__(self) -> dict:
        return str(
            {
                "Name": self.name,
                "Description": self.description,
                "Periodicity": self.periodicity,
                "Created": self.created,
                "CheckOffs": self.check_off_list,
            }
        )


if __name__ == "__main__":
    myhabit = Habit("My Habit", "This is my habit", "DAILY")
    myhabit.check_off("2022-09-25")
    print(myhabit)
