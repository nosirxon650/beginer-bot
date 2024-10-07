from aiogram.fsm.state import State, StatesGroup


class KinoADD(StatesGroup):
    nomi = State()
    des = State()
    url = State()
    finish = State()
    
class Delete(StatesGroup):
    ochirish = State()
    finish2 = State()