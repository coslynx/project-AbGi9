import requests

def verify_account(email, verification_code):
    verification_url = "https://discord.com/api/v9/auth/verify"
    payload = {
        "email": email,
        "code": verification_code
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(verification_url, json=payload, headers=headers)

    if response.status_code == 200:
        return "Account successfully verified"
    else:
        return "Failed to verify account, please try again"