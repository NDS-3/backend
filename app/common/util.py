from datetime import datetime

BASE_DATE = datetime(2022, 11, 11)

class Util:
    def is_passed_basedate(self):
        current_date = datetime.now()
        
        return current_date > BASE_DATE