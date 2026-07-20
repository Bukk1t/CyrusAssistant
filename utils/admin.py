from config import OWNER_ID


def is_admin(user_id: int) -> bool:
    return user_id == OWNER_ID