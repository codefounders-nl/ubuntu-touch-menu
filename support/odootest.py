#!/bin/env python3
import xmlrpc.client
import odooly
import pprint
import json

def get_websitemenu_entry(id):
    return models.execute_kw(db, uid, password, 'website.menu', 'read', [id])

def get_table_entry(tableName, id):
    return models.execute_kw(db, uid, password, tableName, 'read', [id])

def print_json(s):
    print(json.dumps(s, indent=4, sort_keys=True))

def print_all_table_entries(tableName):
    ids = models.execute_kw(db, uid, password, tableName, 'search', [[]], {'limit': 1000})
    print(ids)
    for id in ids:
        print("ID: ", id)
        tableEntry = get_table_entry(tableName, id)
        print(tableEntry)


# info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = \
#     info['host'], info['database'], info['user'], info['password']

# print(info)

o = odooly.Client('https://ubports13.onestein.eu', 'UBports-13', 'api-user', '9(;C94+I,qNA@v$')
# print (vars(o._model))
# print (o.env.models())

# print all tables                  
# for i in o.env.models():
    # print(i)
# print()

url = 'https://ubports13.onestein.eu'
db = 'UBports-13'
username = 'XXXXXXXXX'
password = 'XXXXXXXXX'

# Authenticate and get uid
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print(uid)

# Create object for executing rpc calls
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

print_all_table_entries('website.page')
quit()
# Test example
# modelsresult = models.execute_kw(db, uid, password,
#     'res.partner', 'check_access_rights',
#     ['read'], {'raise_exception': False})

# print(modelsresult)

# Get fields of website.menu
modelsresult = models.execute_kw(
    db, uid, password, 'website.menu', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})
# print(modelsresult)

# parsed = json.loads(modelsresult)
# print_json(modelsresult)
# print()

# Get id's of website.menu
print('Ids in table website.menu')
ids = models.execute_kw(db, uid, password,
    'website.menu', 'search',
    [[]],    {'limit': 1000})
# print (ids)
# print ('Number of ids ', len(ids))
print()


records = models.execute_kw(db, uid, password,
    'website.menu', 'read', [1])
# count the number of fields fetched by default
print(len(records))

print("Menu items")
print_json (get_websitemenu_entry(1))

# print("for loop 1")
# response = json.load(records.text)

def traverse_child_ids(id):
    print ("START")
    childs = get_websitemenu_entry(id)
    # print(childs["display_name"])
    # print(childs)
    # print(childs["id"])
    # print(childs["display_name"])
    # print(childs["child_id"])
    for child in childs:
        # print(child)
        # parsed = json.loads(child)
        # print(parsed)
        print("0 -- ", childs[0]["id"])
        print(child["id"])
        print(child["display_name"])
        print(child["child_id"])
        print(child["parent_path"])
        print(len(child['child_id']))
        for cid in child["child_id"]:
            print ("CHILD: ", cid)
            print ("============================")
            traverse_child_ids(cid)
        # traverse_child_ids(child["child_id"])

# traverse_child_ids(1)
print("===============================>")
traverse_child_ids(4)

print_json(get_websitemenu_entry(4))
print_json(get_websitemenu_entry(25))
print_json(get_websitemenu_entry(55))

quit()
print("for loop")
for record in records:
    print(record["child_id"])
    print_json(record)
    parsed = json.loads(record)
    print(parsed)
print("END for loop")

# parsed = json.loads('[{"child": 1}]')
# print(parsed['child'])
quit()


quit()

# Get values of website.menu
menuItems = models.execute_kw(
    db, uid, password, 'website.menu', 'read',
     [ids], {'fields': ['id', 'is_visible', 'display_name']})


quit()
x = common.listMethods()

menus = o.env['website.menu'].search([])
print (vars(menus))
# menus.env.execute_kw(db, uid, password, 'res.partner', 'fields_get',
#     [], {'attributes': ['string', 'help', 'type']})


print()
x = o.env.models.execute_kw(
    db, uid, password, 'res.partner', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})

print(x)
# print (vars(x.env['attributes']))
