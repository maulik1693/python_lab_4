emp = {
    'id': 1,
    'name': 'Ujeniya Samir',
    'designation': 'SE',
    'salary': 70000
}
if 'designation' in emp:
    del emp['designation']
emp['name'] = 'Ujeniya Maulik'
print(emp)
