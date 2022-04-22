from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_JIHC, URL_APPLE, URL_TELEGRAM, URL_WHATSAPP
from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="College site", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_pear = InlineKeyboardButton(text="Telegram", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_pear = InlineKeyboardButton(text="Whatsapp", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples =InlineKeyboardButton(text="Apple", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="Visit", url=URL_JIHC)
	]
	])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="Visit", URL=URL_APPLE)
	]
	])
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="Visit", url=URL_TELEGRAM)
	]
	])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="Visit", URL=URL_WHATSAPP)
	]
])