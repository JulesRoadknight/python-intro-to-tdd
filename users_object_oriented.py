# In this OO way of updating a list, users is saved in __init__
# A loop then updates each 'age' attribute, changing the original users value
# OO languages use 'getter' and 'setter' methods, that access and modify state, like self.users

class Users:
    def __init__(self, users):
        self.users = users
    
    @property
    def users(self):
        return self._users
    
    @users.setter
    def users(self, updated_users):
        self._users = updated_users

    def update_users(self):
        if self.users:
            for user in self._users:
                user['age'] += 1


# I'm keeping the tests in the same file just to demo, test with `pytest users_object_oriented.py`
def test_update_users_returns_empty_array_given_no_users():
    # Arrange
    user_list = []
    updated_user_list = []
    users = Users(user_list)
    # Act
    users.update_users()
    # Assert
    assert users.users == updated_user_list

def test_update_users_increments_user_age():
    # Arrange
    user_list = [{
        'age': 99,
        'id': 6070,
        'email': 'test@email.com'
    }]
    updated_user_list = [{
        'age': 100,
        'id': 6070,
        'email': 'test@email.com'
    }]
    users = Users(user_list)
    # Act
    users.update_users()
    # Assert
    assert users.users == updated_user_list