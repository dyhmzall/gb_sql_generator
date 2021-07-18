import random


def get_random_datetime():
    return f'{random.randint(2020, 2021)}-{random.randint(1, 12):02}-{random.randint(1, 28):02} {random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}'


def get_random_date():
    return f'{random.randint(1930, 2015)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}'