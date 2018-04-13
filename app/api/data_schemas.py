from schema import Schema, Use

USER_SCHEMA = Schema({
    'name': Use(str),
    'password': Use(str),
})

UPDATE_USER_SCHEMA = Schema({
    'name': Use(str),
    'password': Use(str),
    'new_password': Use(str),
})


REDIRECTION_SCHEMA = Schema({
    'url': Use(str),
})