def solution(id_pw, db):
    user_id, user_pw = id_pw
    
    for db_id, db_pw in db:
        if user_id == db_id:
            if user_pw == db_pw:
                return "login"
            else:
                return "wrong pw"
                
    return "fail"