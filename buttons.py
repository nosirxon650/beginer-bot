from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='ha'), InlineKeyboardButton(text="❌ Bekor qilish", callback_data='yoq')]
    ]
)









menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🍛 Taomlar", callback_data='taom'), InlineKeyboardButton(text="🍷 Ichimliklar", callback_data='ichimlik')],
        [InlineKeyboardButton(text="🧺 Zakaz berish", callback_data="zakaz"), InlineKeyboardButton(text="Bog'lanish", url="t.me//rajabov_shohruhbek"), InlineKeyboardButton(text="Site", web_app=WebAppInfo(url="https://www.thefoodmarket.com/gifts?tfm_click=category-bar"))]
    ]
)


menyular = {
    'Hod Dog': "https://img.freepik.com/premium-photo/handcrafted-gourmet-hot-dog-with-love-white-background-best-hot-dog-image-photography_1020697-119628.jpg",
    'Lavash': "https://www.healthyseasonalrecipes.com/wp-content/uploads/2022/09/mediterranean-lavash-wraps-sq-053.jpg",
    'chiz burger': 'https://minifood.uz/wp-content/uploads/2024/03/chiz-burger.png',
}



taomlar = InlineKeyboardBuilder()
for taom in menyular.keys():
    taomlar.button(text=f"{taom}", callback_data=f"{taom}")
taomlar.button(text="⬅️ Ortga", callback_data="ortga")
taomlar.adjust(2)