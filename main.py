from lorem_text import lorem
import random
from lib.helper import get_random_datetime, get_random_date
# классы для представления таблиц
from tables.user import User
from tables.community import Community
from tables.media_type import MediaType
from tables.media import Media
from tables.photo_album import PhotoAlbum

# настройки
config = {
    'users': {
        'count': 150,
        'items': []
    },
    'messages': {
        'count': 500
    },
    'friend_requests': {
        'count': 80
    },
    'communities': {
        'count': 50,
        'items': []
    },
    'users_communities': {
        'count': 100
    },
    'media_types': {
        'count': 4,
        'items': []
    },
    # media должно быть больше, чем users, иначе - сбоит по пока непонятным причинам
    'media': {
        'count': 200,
        'items': []
    },
    'likes': {
        'count': 150
    },
    'photo_albums': {
        'count': 50,
        'items': []
    },
    'photos': {
        'count': 300
    }
}

# таблица users
email_unique_list = []
phone_unique_list = []
users_count = 0

f = open('data.sql', 'w', encoding='utf-8')

while True:

    user = User(
        users_count + 1,
        lorem.words(1),
        lorem.words(1),
        lorem.words(1) + '@gmail.com',
        random.randint(79000000000, 79999999999)
    )

    # проверка уникальности email
    if user.email in email_unique_list:
        continue
    else:
        email_unique_list.append(user.email)

    # проверка уникальности phone
    if user.phone in phone_unique_list:
        continue
    else:
        phone_unique_list.append(user.phone)

    config['users']['items'].append(user)
    users_count += 1

    sql = f"INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `password_hash`, `phone`) VALUES ('{user.id}', '{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}', '{user.phone}');\n"
    f.write(sql)

    if users_count >= config['users']['count']:
        break

# таблица messages
messages_count = 0

while True:

    from_user = random.choice(config['users']['items'])
    to_user = random.choice(config['users']['items'])

    # пользователь не может отправить сообщение сам себе
    if from_user == to_user:
        continue

    messages_count += 1

    sql = f"INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `created_at`) VALUES (NULL, '{from_user.id}', '{to_user.id}', '{lorem.sentence()}', '{get_random_datetime()}');\n"
    f.write(sql)

    if messages_count >= config['messages']['count']:
        break

# таблица friend_requests
friend_requests_count = 0

while True:

    initiator_user = random.choice(config['users']['items'])
    target_user = random.choice(config['users']['items'])

    # пользователь не может отправить запрос на дружбу сам себе
    if initiator_user == target_user:
        continue

    friend_requests_count += 1

    status = random.choice(['requested', 'approved', 'declined', 'unfriended'])

    sql = f"INSERT INTO `friend_requests` (`initiator_user_id`, `target_user_id`, `status`, `requested_at`, `updated_at`) VALUES ('{initiator_user.id}', '{target_user.id}', '{status}', '{get_random_datetime()}', '{get_random_datetime()}');\n"
    f.write(sql)

    if friend_requests_count >= config['friend_requests']['count']:
        break

# таблица communities
communities_count = 0

while True:

    admin = random.choice(config['users']['items'])

    community = Community(
        communities_count + 1,
        lorem.words(random.randint(1, 3)),
        admin.id
    )

    config['communities']['items'].append(community)
    communities_count += 1

    sql = f"INSERT INTO `communities` (`id`, `name`, `admin_user_id`) VALUES ({community.id}, '{community.name}', '{community.admin_id}');\n"
    f.write(sql)

    if communities_count >= config['communities']['count']:
        break

# таблица users_communities
users_communities_count = 0
check_uniq_list = []

while True:

    user = random.choice(config['users']['items'])
    community = random.choice(config['communities']['items'])

    if f"{user.id}_{community.id}" in check_uniq_list:
        continue
    else:
        check_uniq_list.append(f"{user.id}_{community.id}")

    users_communities_count += 1

    sql = f"INSERT INTO `users_communities` (`user_id`, `community_id`) VALUES ('{user.id}', '{community.id}');\n"
    f.write(sql)

    if users_communities_count >= config['users_communities']['count']:
        break

# таблица media_types
media_types_count = 0

while True:

    media_type = MediaType(
        media_types_count + 1,
        lorem.words(1)
    )

    config['media_types']['items'].append(media_type)

    media_types_count += 1

    sql = f"INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES ('{media_type.id}', '{media_type.name}', '{get_random_datetime()}', '{get_random_datetime()}');\n"
    f.write(sql)

    if media_types_count >= config['media_types']['count']:
        break

# таблица media
media_count = 0

while True:

    media = Media(
        media_count + 1
    )

    media_type = random.choice(config['media_types']['items'])
    user = random.choice(config['users']['items'])

    # сохраним у пользователя, связка потребуется в таблице photos
    user.medias.append(media)

    config['media']['items'].append(media)
    media_count += 1

    sql = f"INSERT INTO `media` (`id`, `media_type_id`, `user_id`, `body`, `filename`, `size`, `metadata`, `created_at`, `updated_at`) VALUES ('{media.id}', '{media_type.id}', '{user.id}', '{lorem.sentence()}', '{lorem.words(1)}', {random.randint(1, 10000)}, NULL, '{get_random_datetime()}', '{get_random_datetime()}');\n"
    f.write(sql)

    if media_count >= config['media']['count']:
        break

# таблица likes
likes_count = 0
likes_unique_list = []

while True:

    user = random.choice(config['users']['items'])
    media = random.choice(config['media']['items'])

    if f"{user.id}_{media.id}" in likes_unique_list:
        continue
    else:
        likes_unique_list.append(f"{user.id}_{media.id}")

    likes_count += 1

    sql = f"INSERT INTO `likes` (`id`, `user_id`, `media_id`, `created_at`) VALUES (NULL, '{user.id}', '{media.id}', '{get_random_datetime()}');\n"
    f.write(sql)

    if likes_count >= config['likes']['count']:
        break

# таблица photo_albums
photo_albums_count = 0

while True:

    photo_album = PhotoAlbum(
        photo_albums_count + 1
    )

    user = random.choice(config['users']['items'])

    # сохраним у пользователя, связка потребуется в таблице photos
    user.photo_albums.append(photo_album)

    config['photo_albums']['items'].append(photo_album)
    photo_albums_count += 1

    sql = f"INSERT INTO `photo_albums` (`id`, `name`, `user_id`) VALUES ('{photo_album.id}', '{lorem.words(1)}', '{user.id}');\n"
    f.write(sql)

    if photo_albums_count >= config['photo_albums']['count']:
        break

# таблица photos
photos_count = 0

while True:

    # альбом и медиа должны принадлежать одному и тому же пользователю
    user = random.choice(config['users']['items'])

    if not len(user.photo_albums):
        continue

    if not len(user.medias):
        continue

    photo_album = random.choice(user.photo_albums)
    media = random.choice(user.medias)

    photos_count += 1

    user.photos.append(photos_count)

    sql = f"INSERT INTO `photos` (`id`, `album_id`, `media_id`) VALUES ('{photos_count}', '{photo_album.id}', '{media.id}');\n"
    f.write(sql)

    if photos_count >= config['photos']['count']:
        break

# таблица profiles
for user in config['users']['items']:

    if len(user.medias):
        media = random.choice(user.medias)
        media_id = media.id
    else:
        media_id = 'NULL'

    sql = f"INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `created_at`, `hometown`) VALUES ('{user.id}', '{random.choice(['m', 'f'])}', '{get_random_date()}', {media_id}, '{get_random_datetime()}', '{lorem.words(1)}');\n"
    f.write(sql)

f.close()
