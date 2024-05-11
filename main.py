from tabulate import tabulate
from typing import Dict, List

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    # Initialize class attribute
    def __init__(self, username: str) -> None:
        self.username = username
    
    def check_benefit(self) -> None:
        '''
        A method for displaying all benefits from PacFlix.
        '''
        # Initialize headers of benefits data
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Benefits"]
        
        # Initialize benefits data
        tables = [
            [True, True, True, "Can Stream"],
            [True, True, True, "Can Download"],
            [True, True, True, "SD Quality"],
            [False, True, True, "HD Quality"],
            [False, False, False, "UHD Quality"],
            [1, 2, 4, "Number of Devices"],
            ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Plan Type"],
            [120_000, 160_000, 200_000, "Price"]
        ]
        
        print("===== PacFlix Plan List =====")
        print("")
        print(tabulate(tables, headers, tablefmt="github"))
        
    def check_plan(self, username: str) -> None:
        '''
        A method for retrieving PacFlix user data based on username.
        
        Parameter
        ---------
        username (str): username from user
        '''
        # Iterate keys and values based on data dictionary
        for keys, values in data.items():
            
            # Create branching loops to filter username
            if username == keys:
                
                # Create variables to store current plan, duration plan
                current_plan = values[0]
                duration_plan = values[1]
                
                print(f"Username: {username}")
                print(f"Current Plan: {current_plan}")
                print(f"Duration Plan: {duration_plan} Bulan")
                print("")

                try:
                    if current_plan == "Basic Plan":
                        headers = ["Basic Plan", "Services"]

                        table = [
                            [True, "Can Stream"],
                            [True, "Can Download"],
                            [True, "SD Quality"],
                            [False, "HD Quality"],
                            [False, "UHD Quality"],
                            [1, "Number of Devices"],
                            ["3rd party Movie only", "Plan Type"],
                            [120_000, "Price"]
                        ]

                        print(f"{current_plan} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers, tablefmt="github"))
                    
                    elif current_plan == "Standard Plan":
                        headers = ["Standard Plan", "Services"]

                        table = [
                            [True, "Can Stream"],
                            [True, "Can Download"],
                            [True, "SD Quality"],
                            [True, "HD Quality"],
                            [False, "UHD Quality"],
                            [2, "Number of Devices"],
                            ["Basic Plan + Sports", "Plan Type"],
                            [160_000, "Price"]
                        ]

                        print(f"{current_plan} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers, tablefmt="github"))

                    elif current_plan == "Premium Plan":
                        headers = ["Premium Plan", "Services"]

                        table = [
                            [True, "Can Stream"],
                            [True, "Can Download"],
                            [True, "SD Quality"],
                            [True, "HD Quality"],
                            [True, "UHD Quality"],
                            [4, "Number of Devices"],
                            ["Basic Plan + Standard Plan + PacFlix Original Series", "Plan Type"],
                            [200_000, "Price"]
                        ]

                        print(f"{current_plan} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers, tablefmt="github"))
                    
                    else:
                        raise Exception("Plan Type is not defined")

                except:
                    raise Exception("Unknown process")
                
            else:
                pass
    
    def upgrade_plan(self, username: str, upgrade_plan: str):
        '''
        A method for upgrading PacFlix subscription.

        Parameter
        ---------
        username (str): current user username
        upgrade_plan (str): upgrade plan selected by current user
        '''
        DISCOUNT = 0.05
        # Iterate keys and values based on data dictionary
        for keys, values in data.items():
            
            try:
                # Create branching loops to filter username
                if username == keys:
                    
                    # Create variables to store current plan, duration plan
                    current_plan = values[0]
                    duration_plan = values[1]

                    if upgrade_plan != current_plan:
                        
                        # Filter duration plan to get 5% discount
                        if duration_plan > 12:
                            
                            # Final price after 5% discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000 - (120_000 * DISCOUNT)
                                return total_price
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000 - (160_000 * DISCOUNT)
                                return total_price
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000 - (200_000 * DISCOUNT)
                                return total_price
                            else:
                                raise Exception("Plan Type is not defined")
                        
                        else:
                            # Price without 5% discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000
                                return total_price
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000
                                return total_price
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000
                                return total_price
                            else:
                                raise Exception("Plan Type is not defined")
                            
                    else:
                        raise Exception("Plan Type cannot be the same")
                
                else:
                    pass

            except:
                raise Exception("Unknown process")    

class NewUser:
    # Initialize class attribute
    referral_code = []

    def __init__(self, username: str) -> None:
        self.username = username
    
    def get_referral_code(self, data: Dict[str, str]) -> List[str]:
        '''
        A method for retrieving referral code from data Dictionary

        Parameter
        ---------
        data (dict): PacFlix user dictionary data

        Return
        ------
        referral_code (list): User referral code list
        '''
        # Iterate values based on data dictionary
        for value in data.values():
            ref_code = value[2]

            # Store ref_code values into the referral_code list
            self.referral_code.append(ref_code)
        
        return self.referral_code
    
    def pick_plan(self, new_plan: str, referral_code: str) -> float:
        DISCOUNT = 0.04

        # Check whether the referral code is already in the referral_code list
        if referral_code in self.referral_code:

            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT)
                return total_price 
            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT)
                return total_price
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT)
                return total_price
            else:
                raise Exception("Plan Type is not defined")
        
        else:
            raise Exception("Referral Code doesn't exist")        


### Create Object for User Class
user_1 = User("Shandy")

## Test Case 1
user_1.check_benefit()

## Test Case 2
user_1.check_plan(user_1.username)

## Test Case 3
user_1.upgrade_plan(user_1.username, "Standard Plan")

## Testing with Another Object
user_2 = User("Cahya")
user_2.check_benefit()
user_2.check_plan(user_2.username)
user_2.upgrade_plan(user_2.username, "Premium Plan")

### Create Object for NewUser Class
faizal = NewUser("faizal_handoko")

# Check available referral codes
print(faizal.get_referral_code(data))

## Test Case 4
print(faizal.pick_plan("Basic Plan", "shandy-2134"))
print(faizal.pick_plan("Bronze Plan", "shandy-2134"))
print(faizal.pick_plan("Basic Plan", "indira-22gs"))