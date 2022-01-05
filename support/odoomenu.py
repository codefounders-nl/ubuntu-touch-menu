#!/usr/bin/python3

import xmlrpc.client
import json
from shutil import copyfile, copyfileobj
import sys

def get_websitemenu_entry(id):
    return models.execute_kw(db, uid, password, 'website.menu', 'read', [id])

def print_json(s):
    print(json.dumps(s, indent=4, sort_keys=True))
    
# Authenticate, and return the uid
def get_uid():
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    return(uid)

# top level menu item with dropdown
def create_nav_item_with_dropdown(menuitem, dropdownitems):
    return('''
                        <li class="nav-item dropdown  ">
                            <a data-toggle="dropdown" href="#" class="nav-link dropdown-toggle  ">
                                <span>''' + menuitem + '''</span>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                            '''+ dropdownitems +'''
                            </ul>
                        </li>

    ''')

# top level menu item with no dropdown
def create_nav_item_no_dropdown(menuitem, url):
    return('''
                        <li class="nav-item">
                            <a role="menuitem" href="''' + url + '''" class="nav-link  ">
                                <span>''' + menuitem + '''</span>
                            </a>
                        </li>

    ''')

# menu item enclosing html
def create_dropdown_menu(menuitem):
    return('''<ul class="dropdown-menu" role="menu">'''
    + menuitem +
      '''</ul>
    ''')

# menu item
def create_dropdown_menu_item(menuitem, url):
    return('''                       
                                <li class="">
                                    <a role="menuitem" href="''' + url + '''" class="dropdown-item  "
                                          style="position: relative; overflow: hidden;">
                                          <span>''' + menuitem + '''</span>
                                    </a>
                                </li>
    ''')

def create_header_with_top_menu(menuitem):
    return(''' <header id="graph_header" data-anchor="true" data-name="Header" class="">
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <div class="container">
                <a href="/" class="navbar-brand logo">
                    <span role="img" aria-label="Logo of Ubuntu Touch" title="Ubuntu Touch"><img
                            src="https://ubuntu-touch.io/web/image/website/2/logo/Ubuntu%20Touch?unique=315c0d7" class="img img-fluid"
                            alt="Ubuntu Touch"></span>
                </a>
                <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#top_menu_collapse">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="top_menu_collapse">
                    <ul class="nav navbar-nav ml-auto text-right" id="top_menu">
                                ''' + menuitem + '''
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    ''')


def traverse_child_ids(ids):
    returnHtml = ""
    for id in ids:
        # Get website menu item as Json
        websiteMenuItem = get_websitemenu_entry(id)[0]
        childIds = websiteMenuItem["child_id"]
        menuItemName = websiteMenuItem["name"]
        hierarchy_level = len(websiteMenuItem['parent_path'].split('/'))
        url = websiteMenuItem["url"]
        # print("A ", menuItemName, hierarchy_level, childIds)
        if hierarchy_level == 2:
            # print("X ", menuItemName)
            returnHtml += create_header_with_top_menu(traverse_child_ids(childIds))
        elif hierarchy_level == 3 and len(childIds) == 0:
            # print("XX no", menuItemName)
            returnHtml +=  create_nav_item_no_dropdown(menuItemName, url)
        elif hierarchy_level == 3 and len(childIds) > 0:
            # print("XX yes", menuItemName)
            returnHtml +=  create_nav_item_with_dropdown(menuItemName, traverse_child_ids(childIds))
        elif hierarchy_level == 4:
            # print("XXx ", menuItemName)
            returnHtml +=  create_dropdown_menu_item(menuItemName, url)
    return returnHtml


url = 'https://ubports13.onestein.eu'
db = 'UBports-13'
username = 'XXXXXXXXX'
password = 'XXXXXXXXXX'
uid = get_uid()

# Create object for executing rpc calls
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

menuFile = "odoomenu.html"

print(traverse_child_ids([4]))
