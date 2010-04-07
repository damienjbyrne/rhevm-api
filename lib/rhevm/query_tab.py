
# query_tab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "g]\xfa'\x05o\xaf\x93]*\xd2\xd3\x08\xaeh\x96"
    
_lr_action_items = {'AND':([1,4,10,19,21,22,23,24,25,26,27,],[7,-2,-3,-4,-5,-13,-18,-14,-11,-12,-10,]),'GT':([2,3,6,28,],[13,-17,-15,-16,]),'GTE':([2,3,6,28,],[14,-17,-15,-16,]),'ID':([0,1,4,7,9,10,11,18,19,21,22,23,24,25,26,27,],[3,3,-2,3,3,-3,3,3,-4,-5,-13,-18,-14,-11,-12,-10,]),'ASC':([3,20,],[-17,29,]),'LT':([2,3,6,28,],[15,-17,-15,-16,]),'SORTBY':([1,4,10,19,21,22,23,24,25,26,27,],[9,-2,-3,-4,-5,-13,-18,-14,-11,-12,-10,]),'LTE':([2,3,6,28,],[16,-17,-15,-16,]),'STRING':([13,14,15,16,17,],[23,23,23,23,23,]),'DESC':([3,20,],[-17,30,]),'EQ':([2,3,6,28,],[17,-17,-15,-16,]),'OR':([1,4,10,19,21,22,23,24,25,26,27,],[11,-2,-3,-4,-5,-13,-18,-14,-11,-12,-10,]),'DOT':([2,3,6,28,],[18,-17,-15,-16,]),'$end':([1,3,4,5,8,10,12,19,20,21,22,23,24,25,26,27,29,30,],[-19,-17,-2,0,-1,-3,-9,-4,-8,-5,-13,-18,-14,-11,-12,-10,-6,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'name':([0,1,7,9,11,18,],[6,6,6,20,6,28,]),'sort_spec':([1,],[8,]),'expr_list':([0,],[1,]),'qname':([0,1,7,11,],[2,2,2,2,]),'value':([13,14,15,16,17,],[22,24,25,26,27,]),'expr':([0,1,7,11,],[4,10,19,21,]),'main':([0,],[5,]),'empty':([1,],[12,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> expr_list sort_spec','main',2,'p_main','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',155),
  ('expr_list -> expr','expr_list',1,'p_expr_list','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',159),
  ('expr_list -> expr_list expr','expr_list',2,'p_expr_list','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',160),
  ('expr_list -> expr_list AND expr','expr_list',3,'p_expr_list','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',161),
  ('expr_list -> expr_list OR expr','expr_list',3,'p_expr_list','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',162),
  ('sort_spec -> SORTBY name ASC','sort_spec',3,'p_sort_spec','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',174),
  ('sort_spec -> SORTBY name DESC','sort_spec',3,'p_sort_spec','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',175),
  ('sort_spec -> SORTBY name','sort_spec',2,'p_sort_spec','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',176),
  ('sort_spec -> empty','sort_spec',1,'p_sort_spec','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',177),
  ('expr -> qname EQ value','expr',3,'p_expr','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',186),
  ('expr -> qname LT value','expr',3,'p_expr','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',187),
  ('expr -> qname LTE value','expr',3,'p_expr','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',188),
  ('expr -> qname GT value','expr',3,'p_expr','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',189),
  ('expr -> qname GTE value','expr',3,'p_expr','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',190),
  ('qname -> name','qname',1,'p_qname','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',204),
  ('qname -> qname DOT name','qname',3,'p_qname','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',205),
  ('name -> ID','name',1,'p_name','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',213),
  ('value -> STRING','value',1,'p_value','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',217),
  ('empty -> <empty>','empty',0,'p_empty','c:\\users\\administrator\\documents\\rhevm-api\\lib\\rhevm\\query.py',221),
]
