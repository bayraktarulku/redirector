from app.models import Redirection, DBSession, IntegrityError
from uuid import uuid4


def get_redirection_value(redirection_hash):
    s = DBSession()
    r = s.query(Redirection).filter(
        Redirection.redirect_hash == redirection_hash).first()
    if not r:
        result = None
    else:
        result = r.redirect_value
    s.close()
    return result


def create_redirection(owner_id, url):
    print(owner_id, url)
    s = DBSession()
    r = Redirection(owner_id=owner_id,
                    redirect_value=url)
    r.redirect_hash = uuid4().hex
    s.add(r)
    try:
        s.commit()
        result = True
    except IntegrityError:
        s.rollback()
        result = False
    s.close()
    return result


def delete_redirection(redirection_id):
    s = DBSession()
    r = s.query(Redirection).get(redirection_id)
    if not r:
        result = False
    else:
        s.delete(r)
        s.commit()
        result = True
    s.close()
    return result

def update_redirection(redirection_id, url):
    print(redirection_id, url)
    s = DBSession()
    r = s.query(Redirection).get(redirection_id)
    if not r:
        result = False

    else:
        r.redirect_value = url
        try:
            s.commit()
            result = True
        except IntegrityError:
            s.rollback()
            result = False

    return result
