import random
from faker import Faker
from faker.providers import person

MY_LASTNAME = 'Salvatierra'
COUNTRY_PROVIDERS = ['en_US', 'fr_FR', 'he_IL', 'en_AU', 'ja_JP']


lines = []
for country in COUNTRY_PROVIDERS:
    country_faker = Faker(country)
    country_faker.add_provider(person)

    for _ in range(20):
        address_line = country_faker.address().replace('\n', ' ')
        line = f'{country_faker.first_name()} {country_faker.last_name()} '\
            f'{random.randint(18, 80)} '\
            f'{country_faker.random_element(["Male", "Female"])} '\
            f'{country_faker.job()} {address_line} {country_faker.email()} '\
            f'{country_faker.ipv4_private()}\n'
        lines.append(line)

with open(f'{MY_LASTNAME}Faker1.txt', 'w') as file:
    file.writelines(lines)
