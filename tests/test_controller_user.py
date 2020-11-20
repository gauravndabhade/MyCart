from tests.setup import setup_database
from user.controller import UserController

mock_user = {
    'username' : 'Foo',
    'password' : '12345678',
    'is_admin' : True
}

def test_create(setup_database):
    user_controller = UserController()
    message = user_controller.create(
        username=mock_user['username'], 
        password=mock_user['password'], 
        is_admin=mock_user['is_admin'])

    assert message == 'User {0} already exist!'.format(mock_user['username'])

def test_login(setup_database):
    user_controller = UserController()
    message = user_controller.login(        
        username=mock_user['username'], 
        password=mock_user['password'])

    assert message == 'Login successfully for {0}!'.format(mock_user['username'])


def test_fail_login(setup_database):
    user_controller = UserController()
    message = user_controller.login(        
        username='ABC',  # User ABC not available
        password=mock_user['password'])

    assert message != '{0} doesn\'t exists'.format(mock_user['username'])

def test_fail_login_2(setup_database):
    user_controller = UserController()
    message = user_controller.login(        
        username=mock_user['username'], 
        password='password')

    assert message == 'Incorrect password'

def test_logout(setup_database):
    user_controller = UserController()
    message = user_controller.logout()
    assert message == f'Logout successfully!'
    