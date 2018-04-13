from app.models import User, DBSession, IntegrityError


def create_user(name, password):
    s = DBSession()
    u = User(name=name, password=password)
    s.add(u)
    try:
        s.commit()
        result = True
    except IntegrityError:
        s.rollback()
        result = False

    s.close()
    return result


def del_user(name, password):
    s = DBSession()
    u = s.query(User).filter(User.name == name,
                             User.password == password).first()
    if not u:
        result = False
    else:
        s.delete(u)
        s.commit()
        result = True
    s.close()
    return result


def change_password(name, password, new_password):
    s = DBSession()
    u = s.query(User).filter(User.name == name,
                             User.password == password).first()

    if not u:
        result = False
    else:
        u.password = new_password
        result = True
        s.commit()
    s.close()
    return result


def get_redirections(user_id):
    s = DBSession()
    u = s.query(User).get(user_id)
    if not u:
        result = None
    else:
        result = [r.to_dict() for r in u.redirections]
    s.close()
    return result
