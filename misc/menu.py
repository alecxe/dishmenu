# -*- coding: cp1251 -*-
from django.core.management import setup_environ
from dishmenu import settings

setup_environ(settings)

import xlrd
import re
from makemenu.models import DishType, Dish

coldDishesName = ur'�������� �����'
firstDishesName = ur'������ �����'
secondDishesName = ur'������ �����'
garnirDishesName = ur'������'
drinksName = ur'�������'
bakingsName = ur'������ �������'
directory = 'C:\Python27\dishmenu\misc\���� ��������� �������� ��� �����������.xlsx'

def convertType(val):
    return str(val) if type(val) == int or type(val) == float else val

def getDishes(dishesList):
    coldDishesIndex = 0
    firstDishesIndex = 0
    secondDishesIndex = 0
    garnirDishesIndex = 0
    drinksIndex = 0
    bakingsIndex = 0
    result = []
    for dish in dishesList:
        if re.search(coldDishesName, dish[0]):
            coldDishesIndex = dishesList.index(dish)
        if re.search(firstDishesName, dish[0]):
            firstDishesIndex = dishesList.index(dish)
        if re.search(secondDishesName, dish[0]):
            secondDishesIndex = dishesList.index(dish)
        if re.search(garnirDishesName, dish[0]):
            garnirDishesIndex = dishesList.index(dish)
        if re.search(drinksName, dish[0]):
            drinksIndex = dishesList.index(dish)
        if re.search(bakingsName, dish[0]):
            bakingsIndex = dishesList.index(dish)
    result.append({coldDishesName : dishesList[coldDishesIndex + 1:firstDishesIndex]})
    result.append({firstDishesName : dishesList[firstDishesIndex + 1:secondDishesIndex]})
    result.append({secondDishesName : dishesList[secondDishesIndex + 1:garnirDishesIndex]})
    result.append({drinksName : dishesList[drinksIndex + 1:bakingsIndex]})
    result.append({bakingsName : dishesList[bakingsIndex + 1:]})
    return result

def generateMostNourishing(dishesList):
    result = []
    for dishGroupDict in dishesList:
        for k,v in dishGroupDict.items():
            print k
            def getWeight(s):
                return s[1]
            listNext = sorted(v, reverse=True, key=getWeight)
            for tup in listNext:
                print tup[1]
            result.append(listNext[0])
    return result

def printDishes(dishesList):
    for dishGroupDict in dishesList:
        for k,v in dishGroupDict.items():
            for dishTuple in v:
                print k+' : '+convertType(dishTuple[0])+' : '+convertType(dishTuple[1])+ur' ��. : '+convertType(dishTuple[2])+ur' �.'

workbook = xlrd.open_workbook(directory,encoding_override="cp1251")
worksheet = workbook.sheet_by_name('����'.decode('cp1251'))
num_rows = worksheet.nrows - 1
curr_row = -1
dishes = []
while curr_row < num_rows:
    qty = 0
    curr_row += 1
    dish = worksheet.cell_value(curr_row, 2)
    if dish != '':
        qtyList = worksheet.cell_value(curr_row, 3).replace(ur'1 ��','50').strip().split('/')
        if len(qtyList) == 1:
            qty = qtyList[0]
        elif len(qtyList) == 2:
            qty = qtyList[1]
        elif len(qtyList) > 2:
            qtyList = map(int, qtyList)
            qty = sum(qtyList)
        if type(qty) != int:
            if len(qty) == 0:
                qty = 0
            elif re.match('\d+',qty):
                qty = int(qty)
        price = worksheet.cell_value(curr_row, 4)
        if len(dish) > 0 and re.search('\S+', dish) and not re.search(ur'����', dish):
            dishes.append((dish,qty,price))
dishesList = getDishes(dishes)

for dish_group_dict in dishesList:
    for dish_group_name, dishes_list in dish_group_dict.items():
        new_dish_type = DishType(name=dish_group_name)
        new_dish_type.save()
        for dish_tuple in dishes_list:
            new_dish_type.dish_set.create(dish_name=dish_tuple[0],dish_weight=dish_tuple[1],dish_price=dish_tuple[2])
        print new_dish_type.dish_set.count()
#generateMostNourishing(dishesList)
#printDishes(dishesList)
#for dishTuple in generateMostNourishing(dishesList):
 #   print convertType(dishTuple[0])+', '+convertType(dishTuple[1])+', '+convertType(dishTuple[2])