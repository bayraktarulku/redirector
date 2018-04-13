from app.models import User, DBSession


def create_user(data):
    try:
        s = DBSession()
        u = User(name=data['name'], password=data['password'])

        s.add(u)
        s.commit()
        result = True
    except:
        s.rollback()
        result = False

    s.close()
    return result


def del_user(data):
    s = DBSession()
    u = s.query(User).filter(User.name == data['name'],
                             User.password == data['password']).first()
    print(u)

    if not u:
        result = False
    else:
        s.delete(u)
        s.commit()
        result = True
    s.close()
    return result


def change_password(data):
    data = {k: data[k] for k in data if k in ['name', 'password',
                                              'new_password']}

    s = DBSession()
    u = s.query(User).filter(User.name == data['name'],
                             User.password == data['password']).first()

    if not u:
        result = False
    else:
        u.password = data['new_password']
        result = True
        s.commit()
    s.close()
    return result


def get_redirections(user_id):
    s = DBSession()
    u = s.query(User).get(user_id)
    print(u)
    if not u:
        result = None
    else:
        result = [r.to_dict() for r in u.redirections]
    s.close()
    return result
