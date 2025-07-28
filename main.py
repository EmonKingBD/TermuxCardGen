import asyncio
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from cardgen import generate_card
from nidgen import generate_nid

BOT_TOKEN = "8274638806:AAFelCVIeQ12WockinqCWcdXcewDHb3_aGY"
API_ID = 12345678  # Replace with your API_ID from my.telegram.org
API_HASH = "your_api_hash"  # Replace with your API_HASH

bot = Client("TermuxCardGenBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

REQUIRED_CHANNEL = "TermuxHubBD"

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = message.from_user

    try:
        chat_member = await client.get_chat_member(f"@{REQUIRED_CHANNEL}", user.id)
        if chat_member.status not in ("member", "administrator", "creator"):
            raise Exception("Not a member")
    except:
        join_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ চ্যানেলে Join করুন", url=f"https://t.me/{REQUIRED_CHANNEL}")]
        ])
        return await message.reply("❌ আপনি আমাদের চ্যানেলে Join করেননি।", reply_markup=join_button)

    buttons = ReplyKeyboardMarkup([
        ["🧮 কার্ড জেনারেট করুন", "🆔 ফেক এনআইডি কার্ড তৈরি করুন"],
        ["📢 আমাদের চ্যানেল"]
    ], resize_keyboard=True)

    await message.reply(
        f"👋 স্বাগতম {user.first_name}!\n\nনিচের অপশনগুলো ব্যবহার করে আপনার কাজ করুন।",
        reply_markup=buttons
    )

@bot.on_message(filters.text("🧮 কার্ড জেনারেট করুন"))
async def gen_card(client, message):
    await message.reply("💳 BIN দিন (6 ডিজিট):")

    @bot.on_message(filters.text & ~filters.command(["start"]))
    async def bin_reply(client, msg):
        bin_input = msg.text.strip()
        card = generate_card(bin_input)
        await msg.reply(f"💳 Card:\n`{card}`", quote=True)

@bot.on_message(filters.text("🆔 ফেক এনআইডি কার্ড তৈরি করুন"))
async def fake_nid(client, message):
    await message.reply("🧾 নাম, ঠিকানা, জন্মতারিখ দিন\nFormat:\n`নাম | ঠিকানা | DD/MM/YYYY`")

    @bot.on_message(filters.text & ~filters.command(["start"]))
    async def nid_input(client, msg):
        try:
            name, address, dob = map(str.strip, msg.text.split("|"))
            path = generate_nid(name, address, dob)
            await msg.reply_photo(photo=path, caption="✅ ফেক এনআইডি কার্ড তৈরি হয়েছে!")
        except:
            await msg.reply("❌ ইনপুট ভুল। সঠিক ফরম্যাট: নাম | ঠিকানা | DD/MM/YYYY")

@bot.on_message(filters.text("📢 আমাদের চ্যানেল"))
async def channel(client, message):
    await message.reply("📢 আমাদের চ্যানেল:\n👉 https://t.me/TermuxHubBD")

bot.run()
