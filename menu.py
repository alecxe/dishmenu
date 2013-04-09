# -*- coding: cp1251 -*-
import xlrd
import re

coldDishesName = ur'Холодные блюда'
firstDishesName = ur'Первые блюда'
secondDishesName = ur'Вторые блюда'
garnirDishesName = ur'Гарнир'
drinksName = ur'Напитки'
bakingsName = ur'Мучные изделия'
dir = 'Меню Приятного аппетита для сотрудников.xlsx'

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
            def getWeight(s):
                return int(s[1])
            listNext = sorted(v, reverse=True, key=getWeight)
            for tup in listNext:
                print tup[1]
            print listNext
            result.append(listNext[0])
    return result

def printDishes(dishesList):
    for dishGroupDict in dishesList:
        for k,v in dishGroupDict.items():
            for dishTuple in v:
                print k+' : '+convertType(dishTuple[0])+' : '+convertType(dishTuple[1])+ur' гр. : '+convertType(dishTuple[2])+ur' р.'

workbook = xlrd.open_workbook(dir,encoding_override="cp1251")
worksheet = workbook.sheet_by_name('меню'.decode('cp1251'))
num_rows = worksheet.nrows - 1
curr_row = -1
dishes = []
while curr_row < num_rows:
    qty = 0
    curr_row += 1
    dish = worksheet.cell_value(curr_row, 2)
    qtyList = worksheet.cell_value(curr_row, 3).replace(ur' 1 шт','50').strip().split('/')
    if len(qtyList) == 1:
        qty = qtyList[0]
    elif len(qtyList) == 2:
        qty = qtyList[1]
    elif len(qtyList) > 2:
        qtyList = map(int, qtyList)
        qty = sum(qtyList)
    price = worksheet.cell_value(curr_row, 4)
    if len(dish) > 0 and re.search('\S+', dish) and not re.search(ur'МЕНЮ', dish):
        dishes.append((dish,qty,price))
dishesList = getDishes(dishes)
#printDishes(dishesList)
for dishTuple in generateMostNourishing(dishesList):
    print convertType(dishTuple[0])+', '+convertType(dishTuple[1])+', '+convertType(dishTuple[2])