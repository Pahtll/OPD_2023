def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit() or (password.isalpha() and (password.isupper() or password.islower())):
        return 'Ненадежный пароль'
    elif (any(map(str.isdigit, password)) and any(map(str.islower,password)) and any(map(str.isupper,password))):
        return 'Надежный пароль'
    else:
        return 'Слабый пароль'