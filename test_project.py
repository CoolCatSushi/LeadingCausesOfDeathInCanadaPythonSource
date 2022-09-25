from project import *
from tkinter import ttk
from tkinter import *

click=0
src = Tk()
src.configure()
f = ttk.Frame(src)
data = {1:1,2:2}
x, y = (1,2)
listBox = single(src, f, data, x, y)

frame = Tk()
frame.configure()


def test_loadCsvMeta():
    residence, age, sex, cause, year = loadCsvMeta()
    assert len(residence) > 0
    assert len (age) > 0
    assert len(sex) > 0
    assert len(cause) > 0
    assert len(year) > 0

def test_multi():
    lb = multi(src, f, data, x, y)
    assert lb != None 


def test_single():
    lb = single(src, f, data, x, y)
    assert lb != None 

def test_label():
    assert label(src, data, x ,y, listBox) == None
    
def test_counter():
    assert counter(listBox) == None
    
def test_label_bind():
    assert label_bind(listBox, listBox) == None
    
def test_createLabels():
    assert createLabels(src, ["1","2","3"], [listBox,listBox,listBox]) == None

def test_create_ok():
    assert create_ok(src) == None

def test_get_values():
    assert get_values(listBox) == []

def test_display():
    assert display('text') == None

def test_loadCsv():
    assert loadCsv() == None

def test_singleLabel():
    assert singleLabel(frame, 'test') == None

def test_year_Label():
    assert year_Label(frame, 'test') == None 

def test_create_tree():
    assert create_tree() == None

if __name__ == '__main__':
    test_loadCsvMeta()
    test_multi()
    test_single()
    test_label()
    test_counter()
    test_label_bind()
    test_createLabels()
    test_create_ok()
    test_get_values()
    test_display()
    test_loadCsv()
    test_singleLabel()
    test_year_Label()
    test_create_tree()