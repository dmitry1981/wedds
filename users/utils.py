import uuid


def generate_activation_code():
    return uuid.uuid4().hex
