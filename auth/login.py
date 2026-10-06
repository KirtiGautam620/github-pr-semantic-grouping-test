from auth.tokens import generate_token

def login(username, password):
    return generate_token(username)