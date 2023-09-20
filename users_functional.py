# In this functional example of updating a list, users is passed straight into a function 'update_users'
# Instead of changing 'users' that is passed in, a new array is constructed using data from 'users', with the updated age

def update_users(users):
    return [{'email': user['email'], 'id': user['id'], 'age': user['age'] + 1} for user in users]

# I'm keeping the tests in the same file just to demo, run with 'pytest users_functional.py'
def test_update_users_returns_empty_array_given_no_users():
    # Arrange
    users = []
    updated_users = []
    # Here Act and Assert are done in one line, that's fine
    assert update_users(users) == updated_users

def test_update_users_increments_user_age():
    # Arrange
    users = [{
        'age': 99,
        'id': 6070,
        'email': 'test@email.com'
    }]
    updated_users = [{
        'age': 100,
        'id': 6070,
        'email': 'test@email.com'
    }]
    # Act, Assert
    assert update_users(users) == updated_users
