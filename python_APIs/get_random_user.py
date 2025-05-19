from typing import Dict, List, Optional, Union
import requests
from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserData:
    username: str
    first_name: str
    last_name: str
    country: str
    email: str
    phone: str
    gender: str
    age: int
    registration_date: str
    picture_url: str

class RandomUserAPI:
    BASE_URL = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    @staticmethod
    def _format_date(date_str: str) -> str:
        """Format date string to a more readable format."""
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return date_str

    @classmethod
    def fetch_single_user(cls) -> Optional[UserData]:
        """Fetch a single random user."""
        try:
            response = requests.get(cls.BASE_URL)
            response.raise_for_status()
            data = response.json()

            if not data.get("success") or "data" not in data:
                raise ValueError("Invalid API response format")

            user_data = data["data"]
            return UserData(
                username=user_data['login']['username'],
                first_name=user_data['name']['first'],
                last_name=user_data['name']['last'],
                country=user_data['location']['country'],
                email=user_data['email'],
                phone=user_data['phone'],
                gender=user_data['gender'],
                age=user_data['dob']['age'],
                registration_date=cls._format_date(user_data['registered']['date']),
                picture_url=user_data['picture']['large']
            )
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Data parsing error: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None

    @classmethod
    def fetch_multiple_users(cls, count: int = 5) -> List[UserData]:
        """Fetch multiple random users."""
        users = []
        for _ in range(count):
            if user := cls.fetch_single_user():
                users.append(user)
        return users

    @staticmethod
    def format_user_output(user: UserData, format_type: str = "text") -> Union[str, Dict]:
        """Format user data in different output formats."""
        if format_type == "json":
            return {
                "username": user.username,
                "name": f"{user.first_name} {user.last_name}",
                "country": user.country,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
                "age": user.age,
                "registration_date": user.registration_date,
                "picture_url": user.picture_url
            }
        else:
            return f"""
User Information:
----------------
Name: {user.first_name} {user.last_name}
Username: {user.username}
Email: {user.email}
Phone: {user.phone}
Gender: {user.gender}
Age: {user.age}
Country: {user.country}
Registration Date: {user.registration_date}
Profile Picture: {user.picture_url}
"""

def main():
    # Example usage
    api = RandomUserAPI()
    
    # Fetch single user
    print("Fetching single user:")
    if user := api.fetch_single_user():
        print(api.format_user_output(user))
    
    # Fetch multiple users
    print("\nFetching multiple users:")
    users = api.fetch_multiple_users(count=3)
    for user in users:
        print(api.format_user_output(user))
        print("-" * 50)
    
    # Example of JSON output
    if user := api.fetch_single_user():
        print("\nJSON format output:")
        print(api.format_user_output(user, format_type="json"))

if __name__ == "__main__":
    main()