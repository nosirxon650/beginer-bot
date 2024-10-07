import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import token
from states import KinoADD, Delete
from aiogram.types import Message, FSInputFile, CallbackQuery
from base import Kino_Read, Kino_add, Kinolar_Read, Kino_Delete
from aiogram.fsm.context import FSMContext
from buttons import tasdiqlash, taom, taomlar

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()





@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    rasm = FSInputFile('foof.png')
    await message.answer_photo(photo="https://i.ytimg.com/vi/oe1-TWFpWqM/sddefault.jpg", caption=f"Qidiryotgan kinolaringizni id yuboring")



@dp.message(F.text == "o'chirish",  F.from_user.id == 5502720862)
async def Kinlardan_delete(message: Message, state: FSMContext):
    kinolar = ""
    for i in Kinolar_Read():
        kinolar += f"{i[0]}   {i[1]}\n"
    await message.answer(f"Qaysi kinoni o'chirmoqchisiz ?\n{kinolar}")
    await state.set_state(Delete.ochirish)

@dp.message(F.text, Delete.ochirish)
async def Kinolar_delete1(message: Message, state: FSMContext):
    xabar = message.text
    xabar = int(xabar)
    await state.update_data(
        {'id':xabar}
    )
    await message.answer(f"{Kino_Read(xabar)[1]} o'chirishga aminmisiz", reply_markup=tasdiqlash)
    await state.set_state(Delete.finish2)

@dp.callback_query(F.data, Delete.finish2)
async def Ochirish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    kino_id = data.get('id')
    xabar = call.data
    if xabar == 'ha':
        Kino_Delete(id=kino_id)
        await call.answer("Kino muafaqiyatli O'chirildi ")
        await state.clear()
    else:
        await call.answer("Kino O'chirmadingiz")
        await state.clear()



@dp.message(F.text=="kinolar", F.from_user.id == 5502720862)
async def Kinolar_Add(message: Message, state:FSMContext):
    await message.answer("Kinoning nomini yuboring ???")
    await state.set_state(KinoADD.nomi)

@dp.message(F.text, KinoADD.nomi)
async def KinoNomi(message: Message, state: FSMContext):
    kino_nomi = message.text
    await state.update_data(
        {"nomi":kino_nomi}
    )
    await message.answer("Kinoning description kiriting ...")
    await state.set_state(KinoADD.des)


@dp.message(F.text, KinoADD.des)
async def KinoNomi(message: Message, state: FSMContext):
    kino_des = message.text
    await state.update_data(
        {"des":kino_des}
    )
    await message.answer(f"Kinoning kino url kiritin...\n")
    await state.set_state(KinoADD.url)

@dp.message(F.text, KinoADD.url)
async def KinoNomi(message: Message, state: FSMContext):
    kino_url = message.text
    await state.update_data(
        {"url":kino_url}
    )
    data = await state.get_data()
    kino_nomi = data.get('nomi')
    kino_des = data.get('des')
    await message.answer_video(video=kino_url, caption=f"Nomi: {kino_nomi}\n\n{kino_des}", reply_markup=tasdiqlash)
    await state.set_state(KinoADD.finish)


@dp.callback_query(F.data, KinoADD.finish)
async def KinolarFinish(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    kino_nomi = data.get('nomi')
    kino_des = data.get('des')
    kino_url = data.get('url')
    xabar = call.data
    if xabar == 'ha':
        Kino_add(kino_nomi=kino_nomi, kino_des=kino_des, kino_url=kino_url)
        await call.answer("Kino muafaqiyatli qo'shildi ")
        await state.clear()
    else:
        await call.answer("Kino atmen qildingiz")
        await state.clear()




@dp.message(F.text)
async def Kinolar_olami(message: Message):
    xabar = message.text
    if xabar.isdigit():
        xabar = int(xabar)
        try:
            kinolar_olami = Kino_Read(xabar)
            await message.answer_video(video=f"{kinolar_olami[3]}", caption=f"Kino Nomi: {kinolar_olami[1]}\n\n{kinolar_olami[2]}")
            await bot.send_video(chat_id=-1002033926230, video=f"{kinolar_olami[3]}")
        except:
            await message.answer("Siz mavjud bo'lmagan raqam yubordingiz")
    else:
        await message.answer("Siz text yubormang raqam yuboring")




""""

Yangi branchga pull request

"""






@dp.callback_query(F.data == "taom")
async def TaomlarBot(call: CallbackQuery):
    rasm = FSInputFile('foof.png')
    await call.message.answer_photo(photo="https://t4.ftcdn.net/jpg/02/86/17/89/360_F_286178925_8zk89O9uC5JJVPvqhvBMUpaRxp8AFXzD.jpg", caption="Birini tanlang!!!", reply_markup=taomlar.as_markup())


@dp.callback_query(F.data == "ichimlik")
async def IchimliklarBot(call: CallbackQuery):
    await call.answer("Ichimliklar bo'limi bosh")
    


@dp.callback_query(F.data == "zakaz")
async def ZakazlarBot(call: CallbackQuery):
    user_id = call.from_user.id
    user = call.from_user.first_name
    print("ism", user, "user id", user_id)
    await call.answer("Zakaz bera olmaysiz", show_alert=True)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Tugadi")