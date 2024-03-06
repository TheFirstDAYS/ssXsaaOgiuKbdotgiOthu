from pyrogram import Client, filters
import requests
import json
import re
import time
from FUNC.usersdb_func import *
from FUNC.GATES.SHOPIFY.main_func import *
from FUNC.defs import *
from datetime import date
import requests
import json
import random
import asyncio
import threading
session = requests.session()


@Client.on_message(filters.command("sh", [".", "/"]))
def multi(Client,message):
    t1 = threading.Thread(target=bcall, args=(Client,message))
    t1.start()

def bcall(Client,message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(thread(Client, message))
    loop.close()
async def thread(Client,message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = str(getuserinfo(user_id))
        if regdata == 'None':
            resp = "𝐔𝐧𝐫𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐞𝐝 𝐔𝐬𝐞𝐫. 𝐏𝐫𝐞𝐬𝐬 /register 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞."
            await message.reply_text(resp, message.id)
        else:
            getuser = getuserinfo(user_id)
            status = getuser["status"]
            role = status
            plan = getuser["plan"]
            expiry = getuser["expiry"]
            credit = int(getuser["credit"])
            antispam_time = int(getuser["antispam_time"])
            checkgroup = str(getchatinfo(chat_id))
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "𝐔𝐍𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃 𝐔𝐒𝐄𝐑 𝐋𝐌𝐀𝐎! 𝐑𝐔𝐍 𝐁𝐎𝐙𝐎 𝐑𝐔𝐍"
                await message.reply_text(resp, message.id)

            elif chat_type == "ChatType.GROUP" or chat_type == "ChatType.SUPERGROUP" and checkgroup == "None":
                resp = "𝐂𝐇𝐀𝐓 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐙𝐄𝐃, 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃, 𝐀𝐒𝐊 𝐌𝐘 𝐎𝐖𝐍𝐄𝐑 @stripe_xD 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
                await message.reply_text(resp, message.id)
            else:
                if credit < 3:
                    resp = "𝐒𝐎𝐑𝐑𝐘 𝐁𝐑𝐎! 𝐑𝐀𝐍 𝐎𝐔𝐓 𝐎𝐅 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 𝐋𝐌𝐀𝐎. 𝐓𝐎 𝐁𝐔𝐘 𝐃𝐦 @stripe_xD"
                    await message.reply_text(resp, message.id)
                else:
                    now = int(time.time())
                    count_antispam = now - antispam_time
                    if status == 'FREE' and count_antispam < 30:
                        after = 30 - count_antispam
                        resp = f"""
𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐒𝐓𝐅𝐔!
𝐃𝐎𝐍'𝐓 𝐓𝐑𝐘 𝐁𝐄𝐅𝐎𝐑𝐄 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    elif status == 'PREMIUM' and count_antispam < 5:
                        after = 5 - count_antispam
                        resp = f"""
𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐒𝐓𝐅𝐔!
𝐃𝐎𝐍'𝐓 𝐓𝐑𝐘 𝐁𝐄𝐅𝐎𝐑𝐄 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
                        await message.reply_text(resp, message.id)
                    else:
                        msg = message.text.split(" ")
                        try:
                            try:
                                cc = msg[1]
                            except:
                                cc = message.reply_to_message.text
                        except Exception as e:
                            resp = "𝗚𝗜𝗩𝗘 𝗠𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗖𝗖 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️"
                            await message.reply_text(resp, message.id)
                        checkcc = getcards(cc)
                        if checkcc == None:
                            resp = "𝗚𝗜𝗩𝗘 𝗠𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗖𝗖 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️"
                            await message.reply_text(resp, message.id)
                        else:
                            cc = checkcc[0]
                            mes = checkcc[1]
                            ano = checkcc[2]
                            cvv = checkcc[3]
                            fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                            firstresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ ꆜꆜꆜꆜꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """

                            firstchk = await message.reply_text(
                                firstresp, message.id)
                            secondresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """
                            secondchk = await Client.edit_message_text(
                                message.chat.id, firstchk.id, secondresp)
                            thirdresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ꆜꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """
                            thirdchk = await Client.edit_message_text(
                                message.chat.id, secondchk.id, thirdresp)
                            #STARTED CHECKING CC#
                            tic = time.perf_counter()
                            result = str(check_shopify(cc,mes,ano,cvv))
                            fourthresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ꆜꆜꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """
                            fourthchk = await Client.edit_message_text(
                                message.chat.id, thirdchk.id, fourthresp)
                            #BIN RESPINSE
                            fbin = cc[:6]
                            bin = session.get(
                                f"https://lookup.binlist.net/{fbin}").json()
                            try:
                                brand = bin["scheme"].upper()
                            except:
                                brand = "N/A"
                            try:
                                type = bin["type"].upper()
                            except:
                                type = "N/A"
                            try:
                                level = bin["brand"].upper()
                            except:
                                level = "N/A"
                            try:
                                bank_data = bin["bank"]
                            except:
                                bank_data = "N/A"
                            try:
                                bank = bank_data["name"].upper()
                            except:
                                bank = "N/A"
                            try:
                                country_data = bin["country"]
                            except:
                                country_data = "N/A"
                            try:
                                country = country_data["name"].upper()
                            except:
                                country = "N/A"
                            try:
                                flag = country_data["emoji"]
                            except:
                                flag = "N/A"
                            try:
                                currency = country_data["currency"].upper()
                            except:
                                currency = "N/A"
                            toc = time.perf_counter()
                            #RESPONSE SECTION
                            fifthresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ꆜꆜꆜꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """
                            fifthchk = await Client.edit_message_text(
                                message.chat.id, fourthchk.id, fifthresp)
                            sixresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 ⟿ 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆.........
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿ꆜꆜꆜꆜꆜ
⊗ GATEWAY- Shopify 20$
</b>
              """
                            sixchk = await Client.edit_message_text(
                                message.chat.id, fifthchk.id, sixresp)
                            if 'thank you' in result or 'Your order is confirmed' in result or "Thank you" in result:
                                status = "Live 🟢"
                                response = "Payment Successfull ✅"


                            elif "insufficient_funds" in result or "card has insufficient funds." in result:
                                status = "Live 🟢"
                                response = "Insufficient Funds ❎"

                            elif "Security code was not matched by the processor" in result:
                                status = "Live 🟡"
                                response = "Security code was not matched by the processor ❎"

                            elif "transaction_not_allowed" in result:
                                status = "Live 🟡"
                                response = "Card Doesn't Support Purchase ❎"  

                            elif '"cvc_check": "pass"' in result:
                                status = "Live 🟢"
                                response = "CVV LIVE ❎"

                            elif "https://js.stripe.com/v3" in result:
                                status = "Live 🟡"
                                response = "3D Secure Redirected ❎"

                            elif "stripe_3ds2_fingerprint" in result:
                                status = "Live 🟡"
                                response = "3D Secured ❎"

                            elif "Your card does not support this type of purchase." in result:
                                status = "Live 🟡"
                                response = "Card Doesn't Support Purchase ❎"

                            elif "generic_decline" in result or "You have exceeded the maximum number of declines on this card in the last 24 hour period." in result or "card_decline_rate_limit_exceeded" in result:
                                status = "Dead 🔴"
                                response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"

                            elif "do_not_honor" in result:
                                status = "Dead 🔴"
                                response = "𝐃𝐈𝐃 𝐍𝐎𝐓 𝐇𝐎𝐍𝐎𝐑 𝐘𝐎𝐔 𝐀𝐒 𝐀 𝐂𝐀𝐑𝐃𝐄𝐑 𝐋𝐌𝐀𝐎💔❌"
                            elif "Cannot connect to proxy." in result:
                                status = "Dead 🔴"
                                response = "Proxy Error 🚫"
                            elif "CERTIFICATE_VERIFY_FAILED" in result:
                                status = "Dead 🔴"
                                response = "Can't Reach to The Site 🚫"
                            elif "CARD PROCESSING ERROR" in result:
                                status = "Dead 🔴"
                                response = "Unable To Process This Card 🚫"
                            elif "Card was declined" in result:
                                status = "Dead 🔴"
                                response = "Card Was Declined 🚫"

                            elif "fraudulent" in result:
                                status = "Dead 🔴"
                                response = "Fraudulent 🚫"

                            elif "stolen_card" in result:
                                status = "Dead 🔴"
                                response = "Stolen Card 🚫"

                            elif "lost_card" in result:
                                status = "Dead 🔴"
                                response = "Lost Card 🚫"

                            elif "pickup_card" in result:
                                status = "Dead 🔴"
                                response = "Pickup Card 🚫"

                            elif "Card number is incorrect" in result:
                                status = "Dead 🔴"
                                response = "Incorrect Card Number 🚫"

                            elif "Your card has expired." in result or "expired_card" in result:
                                status = "Dead 🔴"
                                response = "Expired Card 🚫"

                            elif "intent_confirmation_challenge" in result:
                                status = "Dead 🔴"
                                response = "Captcha 😥"

                            elif "Your card number is incorrect." in result:
                                status = "Dead 🔴"
                                response = "Incorrect Card Number 🚫"

                            elif "Your card's expiration year is invalid." in result or "Your card\'s expiration year is invalid." in result:
                                status = "Dead 🔴"
                                response = "Expiration Year Invalid 🚫"

                            elif "Your card's expiration month is invalid." in result or "invalid_expiry_month" in result:
                                status = "Dead 🔴"
                                response = "Expiration Month Invalid 🚫"

                            elif "card is not supported." in result:
                                status = "Dead 🔴"
                                response = "Card Not Supported 🚫"

                            elif "invalid_account" in result:
                                status = "Dead 🔴"
                                response = "Dead Card 🚫"

                            elif "Invalid API Key provided" in result or "testmode_charges_only" in result or "api_key_expired" in result:
                                status = "Dead 🔴"
                                response = "SK DEAD 🚫"
                                refundcredit(user_id)

                            elif "Your card was declined." in result or "card was declined" in result:
                                status = "Dead 🔴"
                                response = "𝐃𝐄𝐀𝐃 𝐂𝐀𝐑𝐃 𝐍𝐈𝐆𝐆𝐀! 💔❌"

                            else:
                                status = "Dead 🔴"
                                response = f"Card Declined 🚫"
                                refundcredit(user_id)
                                with open("shopify_error.txt","a",encoding="UTF-8") as f:
                                    f.write(f"{result}\n")

                    #--------------FINAL RESPONSE ------------#

                            finalresp = f"""
<b>↯ SHOPIFY 

𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 ⟿ <code>{fullcc}</code> 
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅 𝐂𝐀𝐑𝐃{status}
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ⟿{response}
⊗ GATEWAY- Shopify 20$ 

𝐂𝐀𝐑𝐃𝐬 𝐁𝐈𝐍 𝐈𝐍𝐅𝐎
𝐁𝐈𝐍 ⟿ {fbin} - {brand} - {type} - {level}
𝐁𝐀𝐍𝐊 ⟿  {bank} 🏛  
𝐂𝐎𝐔𝐍𝐓𝐑𝐘 ⟿ {country} - {flag} - {currency}


 
𝐓𝐈𝐌𝐄 ⟿ 𝐓𝐈𝐌𝐄 𝐓𝐀𝐊𝐄𝐍 {toc - tic:0.4f}sec
𝐂𝐑𝐄𝐃𝐈𝐓 𝐒𝐏𝐄𝐍𝐓 ⟿ 1
𝐔𝐒𝐄𝐑 ⟿ <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> 🗿 [ {role} ]
- 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐎𝐓 𝐎𝐅 𝐓𝐄𝐀𝐌 𝐍𝐌𝐁
</b>
            """

                            await Client.edit_message_text(message.chat.id, sixchk.id, finalresp)
                            #ANTISPAM TIME SET
                            setantispamtime(user_id)
                            deductcredit(user_id)
                            plancheck = plan_expirychk(user_id)
                            if plancheck == "YES":
                                resp = """
𝐇𝐄𝐘 𝐁𝐎𝐙𝐎𝐎!
𝐏𝐋𝐀𝐍 𝐄𝐗𝐏𝐈𝐑𝐄𝐃 𝐁𝐀𝐁𝐘! 𝐁𝐔𝐘 /buy 𝐨𝐫 𝐁𝐄𝐆 @stripe_xD
                """
                                await Client.send_message(user_id, resp)
                            else:
                                pass

    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"{e}\n")
