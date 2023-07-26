from application.salary import *
from application.db.people import *
from datetime import *

from cowsay import *

def main():
    print(get_output_string('turtle', f"Current date {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}"))
    cow(calculate_salary())
    cow(get_employees())
    cow("Moo...")

if __name__ == "__main__":
    main()