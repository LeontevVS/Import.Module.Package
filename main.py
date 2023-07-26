from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

from cowsay import cow
from cowsay import get_output_string

def main():
    print(get_output_string('turtle', f"Current date {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}"))
    cow(calculate_salary())
    cow(get_employees())
    cow("Moo...")

if __name__ == "__main__":
    main()