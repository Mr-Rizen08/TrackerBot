import requests
from config import DB_API
from datetime import datetime, timedelta

def create_user(user_id, user_name):
    requests.post(
        url = "https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/Users",
        headers= {
            "apikey": DB_API
        },
        json = {
        "user_id" : user_id,
        "user_name": user_name
        }
    )

def get_user(user_id):
    data = requests.get(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/Users?user_id=eq.{user_id}",
        headers={
            "apikey": DB_API
        }
    )
    user = data.json()
    return user[0] if len(user) > 0 else None

def create_user_habit(user_id ,name, description):
    requests.post(
        url="https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/habits",
        headers={
          "apikey": DB_API
        },
        json = {
            "user_id": user_id,
            "name": name,
            "description": description
        }
    )

def get_user_habit(user_id):
    data = requests.get(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/habits?user_id=eq.{user_id}",
        headers={
            "apikey": DB_API
        }
    )
    habits = data.json()
    return habits

def delete_habits(user_id, name):
    requests.delete(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/habits?user_id=eq.{user_id}&id=eq.{name}",
        headers={
            "apikey": DB_API
        }
    )

def search_user_habit(user_id, id):
    data = requests.get(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/habits?user_id=eq.{user_id}&id=eq.{id}",
        headers={
            "apikey": DB_API
        }
    )
    habits = data.json()
    return habits

def create_progress(habit_id, user_id):
    requests.post(
        url= "https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/progress",
        headers={
            "apikey": DB_API
        },
        json={
            "habit_id": habit_id,
            "user_id": user_id
        }
    )

def update_progress(habit_id):
    now = datetime.now().isoformat()
    requests.patch(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/progress?habit_id=eq.{habit_id}",
        headers={
            "apikey": DB_API,
        },
        json={
            "date": now
        }
    )

def get_progress(habit_id):
    now = datetime.now()
    time = now - timedelta(days=30)
    data = requests.get(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/progress?habit_id=eq.{habit_id}&date=gt.{time}&select=*,habits(name)",
        headers={
            "apikey": DB_API,
            "Authorization": f"Bearer {DB_API}"
        }
    )
    progress = data.json()
    return progress[0] if len(progress) > 0 else None


def get_progress_7_days(user_id):
    now = datetime.now()
    time = now - timedelta(days=7)
    data = requests.get(
        url=f"https://xvaepidgrhnxkhpzexwh.supabase.co/rest/v1/progress?user_id=eq.{user_id}&date=gt.{time}",
        headers={
            "apikey": DB_API
        }
    )
    progress = data.json()
    return progress
