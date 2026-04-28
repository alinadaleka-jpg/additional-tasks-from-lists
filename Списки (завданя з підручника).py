names = ['Олексій', 'Марія', 'Іван', 'Анна']

for name in names:
    print(name)
transport = ['велосипед', 'автомобіль', 'мотоцикл', 'самокат']

for i in transport:
    print(f"Я хотів би купити {i}.")
years_list = [ 2009, 2010, 2011, 2012, 2013, 2014]
print(f"3 роки мені було в {years_list[3]} році")
years_list.append(2015)
print(f"Оновлений список: {years_list}")
print(f"Найбільше років мені було в {years_list[-1]} році")


things = ['wallet', 'mirror', 'umbrella']
print(things[2].capitalize())
print(things)
things[2] = things[2].upper()
print(things)
things.remove('UMBRELLA')
print(things)


languages = ['Georgian', 'Estonian', 'Ukrainian']
last_lang = languages[-1].lower()
reversed_lang = last_lang[::-1]
result = reversed_lang.capitalize()
print(result)



hardware = ('Monitor', 'CPU', 'Mouse')
software = ['Python', 'Windows', 'Browser']
print("Hardware:")
for device in hardware:
    print(f"- {device}")
for app in software:
    print(f"- {app}")
software[1] = 'Linux'
print(f"Список оновлено успішно: {software}")
hardware = ('Monitor', 'GPU', 'Mouse')
print(f"Кортеж 'оновлено' через новий об'єкт: {hardware}")



languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
print(f"Початковий список: {languages}")
sorted_languages = sorted(languages)
print(f"\nПісля sorted(): {sorted_languages}")
languages.reverse()
print(f"\nПісля reverse(): {languages}")
languages.sort()
print(f"\nПісля sort(): {languages}")



cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = f"{cities[0]}, {cities[1]}, {cities[2]}, {cities[3]}, {cities[4]} and {cities[5]}"
print(message)



professions = ['Doctor', 'Engineer', 'Artist']
sports = ['Football', 'Tennis', 'Swimming', 'Boxing']
family = ['Mother', 'Father', 'Brother']
oceans = ('Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic')
print(f"Початкові професії: {professions}")
professions.append('Pilot')
sports.remove('Boxing')
removed_member = family.pop()
print(f"Видалений член родини: {removed_member}")
print(f"Кількість океанів у світі: {len(oceans)}")
print(f"Спорт за алфавітом: {sorted(sports)}")
print(f"Спорт як був: {sports}")
sports_tuple = tuple(sports)

