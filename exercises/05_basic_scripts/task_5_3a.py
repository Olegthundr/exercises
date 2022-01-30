# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
int_mode = input('Введите режим работы интерфейса (access/trunk): ')
variants = {
    "access": 'Введите номер VLAN:',
    "trunk": 'Введите разрешенные VLANы:',
}
modes = {
    "access": [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
],
"trunk": [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
],
}
iface = input('Введите тип и номер интерфейса: ')
vlan = input(variants[int_mode])
modes['access'][1] = "switchport access vlan " + str(vlan)
modes['trunk'][2] = "switchport trunk allowed vlan " + str(vlan)

print(f'''interface {iface}''')
print('{}'.format('\n'.join(modes[int_mode])))
