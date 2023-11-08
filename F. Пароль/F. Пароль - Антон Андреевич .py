def password_level(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    #Проверяем состоит ли пароль только из цифр, либо только из символов одного регистра
    elif password.isdigit() or (password.isalpha() and (password.isupper() or password.islower())):
        return 'Ненадежный пароль'
    #Проверяем есть ли в пароле одновременно цифры и буквы верхнего и нижнего регистра
    elif (any(map(str.isdigit, password)) and any(map(str.islower,password)) and any(map(str.isupper,password))):
        return 'Надежный пароль'
    #Если ни одно из условий не выполняется то пароль - слабый
    else:
        return 'Слабый пароль'