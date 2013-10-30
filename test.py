
class Globals(object):

    _REGISTERED_GLOBALS = {}

    @classmethod
    def register(cls, name, value):
        assert name not in cls._REGISTERED_GLOBALS, 'Global exists'
        cls.set(name, value)

    @classmethod
    def set(cls, name, value):
        cls._REGISTERED_GLOBALS[name] = value

    @classmethod
    def setattr(cls, name, attr_name, attr_value):
        assert name in cls._REGISTERED_GLOBALS, 'Global does not exist'
        setattr(cls.get(name), attr_name, attr_value)

    @classmethod
    def get(cls, name):
        return cls._REGISTERED_GLOBALS[name]


class State(object):
    pass


class GoTo(object):
    pass


def create_type(name, **kwargs):
    return type(name, (), **kwargs)


def goto(state_name):
    pass


user = create_type(name='User',
                   active=False,
                   authed=False,
                   agent=False,
                   landlord=False,
                   rules_agreed=False,
                   payed=False)


State.register('register')
State.get('register').steps = [
    lambda: Globals.register('user', user()),
    GoTo('place_an_ad')
]

State.register('registered')
State.get('register').steps = [
    lambda: Globals.register('user', user()),
    lambda: Globals.setattr('user', 'active', True),
    lambda: Globals.setattr('user', 'authed', True),
    lambda: Globals.setattr('user', 'rules_agreed', True),

    GoTo('place_an_ad')
]

State.register('place_an_ad')

def state_place_an_ad():
    goto('enter_details')


class State_enter_details():
