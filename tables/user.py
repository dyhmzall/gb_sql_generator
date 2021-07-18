import hashlib


class User:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        hash_object = hashlib.md5(first_name.encode())
        self.password = hash_object.hexdigest()
        self.phone = phone

        # будут заполняться по ходу действия
        self.photo_albums = []
        self.medias = []

        self.photos = []