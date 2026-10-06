from auth.tokens import generate_token

def login(username, password):
    print("Login attempt")
    return generate_token(username)