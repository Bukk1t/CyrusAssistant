from database.database import (
    add_user,
    add_message,
    get_user,
)


def register_user(user):
    add_user(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
    )


def register_message(user_id):
    add_message(user_id)


def get_profile(user_id):
    return get_user(user_id)