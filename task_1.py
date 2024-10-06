from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        now = datetime.now().date()
        converted_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Incorrect data format. Please enter date in format 'YYYY-MM-DD.'"
    
    return (now - converted_date).days
    
  