# Python 3.10
# Developer : Github.com/alireza536

# Importing ... 
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageFilter
from telegram.ext import Filters

from telegram.chataction import ChatAction

from telegram import Update
from telegram import ReplyKeyboardMarkup

from time import sleep , time

from ChatID import ChatID
from API import Get
ChatIDManagement = ChatID()

Messages = {
    'msg_start' : '{} درود',
    'msg_Warning_getrate' : 'لطفا حدقلا دو ارز را وارد کنید !',
    'msg_help' : 'این بات برای به دست اوردن قیمت ارز ساخته شده است برای استفاده از این بات باید دستوری /getrate را تایپ کرده و سپس ارز های مورد نظر خور را با یک فاصله از هم بنویسید \n برای مثال : \n/getrate BTC USD ABT\n',
    'msg_abut' : 'حساب گیت هاب توسعه دهنده : https://Github.com/alireza536',
    'msg_list_coins' : """
1 -  42 ------->   42 Coin
2 -  300 ------>   300 Token
3 -  365 ------>   365Coin
4 -  404 ------>   404Coin
5 -  433 ------>   433 Token
6 -  611 ------>   SixEleven
7 -  808 ------>   808Coin
8 -  ABBC ----->   Alibabacoin
9 -  ABT ------>   Arcblock
10 -  ABY ------>   ArtByte
11 -  AC ------->   AsiaCoin
12 -  ACC ------>   Accelerator Network
13 -  AD ------->   Andorra
14 -  ADA ------>   Cardano
15 -  ADC ------>   AudioCoin
16 -  ADEL ----->   Adelphoi
17 -  ADK ------>   Aidos Kuneen
18 -  ADX ------>   AdEx
19 -  ADZ ------>   Adzcoin
20 -  AE ------->   Aeternity
21 -  AEON ----->   Aeon
22 -  AGI ------>   SingularityNET
23 -  AGRS ----->   Agoras Tokens
24 -  AGRS ----->   IDNI Agoras
25 -  AIB ------>   AdvancedInternetBlock
26 -  AION ----->   Aion
27 -  AIR ------>   Aircoin
28 -  AKY ------>   Akuya Coin
29 -  ALIS ----->   ALISmedia
30 -  ALQO ----->   ALQO
31 -  ALT ------>   Altcoin
32 -  AMB ------>   Ambrosus
33 -  AMM ------>   MicroMoney
34 -  AMP ------>   Synereo
35 -  AMS ------>   AmsterdamCoin
36 -  ANC ------>   Anoncoin
37 -  ANS ------>   Antshares
38 -  ANT ------>   Aragon
39 -  AOA ------>   Aurora
40 -  APX ------>   ApexCoin
41 -  ARB ------>   ARbit
42 -  ARDR ----->   Ardor
43 -  ARG ------>   Argentum
44 -  ARK ------>   Ark
45 -  ARN ------>   Aeron
46 -  ARRR ----->   Pirate Chain
47 -  ART ------>   Maecenas
48 -  ASAFE ---->   AllSafe
49 -  AST ------>   AirSwap
50 -  ATH ------>   Atheios
51 -  ATM ------>   ATMChain
52 -  ATOM ----->   Cosmos
53 -  ATX ------>   Artex Coin
54 -  AUR ------>   AuroraCoin
55 -  AUT ------>   Autoria
56 -  AVA ------>   Travala
57 -  AVC ------>   Avera
58 -  AVH ------>   Animation Vision Cash
59 -  AXP ------>   AXP
60 -  B2B ------>   B2BX
61 -  B2X ------>   SegWit2x
62 -  BAB ------>   Binance BAB
63 -  BAC ------>   Beauty Chain
64 -  BASH ----->   LuckChain
65 -  BAT ------>   Basic Attention Token
66 -  BAY ------>   BitBay
67 -  BBC ------>   TraDove B2BCoin
68 -  BBK ------>   BitBlocks
69 -  BBP ------>   BiblePay
70 -  BCH ------>   Bitcoin Cash
71 -  BCN ------>   Bytecoin
72 -  BCO ------>   BridgeCoin
73 -  BCPT ----->   BlockMason Credit Protocol
74 -  BCX ------>   BitcoinX
75 -  BCY ------>   BitCrystals
76 -  BDG ------>   BitDegree
77 -  BDL ------>   Bitdeal
78 -  BELA ----->   Bela
79 -  BERN ----->   BERNcash
80 -  BET ------>   DAO
81 -  BFT ------>   BnkToTheFuture
82 -  BGC ------>   BagCoin
83 -  BIX ------>   Bibox Token
84 -  BLC ------>   Blakecoin
85 -  BLK ------>   BlackCoin
86 -  BLOCK ---->   Blocknet
87 -  BLRY ----->   BillaryCoin
88 -  BLZ ------>   Bluzelle
89 -  BMC ------>   Blackmoon Crypto
90 -  BMH ------>   BlockMesh
91 -  BNB ------>   Binance Coin
92 -  BNT ------>   Bancor Network Token
93 -  BNTY ----->   Bounty0x
94 -  BORA ----->   BORA
95 -  BOS ------>   BOScoin
96 -  BOXX ----->   Blockparty
97 -  BPT ------>   Blockport
98 -  BRAVO ---->   BRAVO Pay
99 -  BRD ------>   Bread
100 -  BRIT ----->   BritCoin
""",
    'msg_list_coin_2' : """
101 -  BRK ------>   Breakout
102 -  BRX ------>   Breakout Stake
103 -  BST ------>   BoostCoin
104 -  BT2 ------>   Bitcoin SegWit2X
105 -  BTA ------>   Bata
106 -  BTD ------>   Bitcloud
107 -  BTC ------>   Bitcoin
108 -  BTCA ----->   Bitair
109 -  BTCD ----->   BitcoinDark
110 -  BTCH ----->   Bitcoin Hush
111 -  BTCP ----->   Bitcoin Private
112 -  BTCZ ----->   BitcoinZ
113 -  BTDX ----->   Bitcloud 2
114 -  BTF ------>   Bitcoin Fast
115 -  BTG ------>   Bitcoin Gold
116 -  BTM ------>   Bitmark
117 -  BTN ------>   BitNewChain
118 -  BTS ------>   BitShares
119 -  BTX ------>   Bitcore
120 -  BTZ ------>   Bitz
121 -  BU ------->   BuzzCoin
122 -  BURST ---->   BurstCoin
123 -  BUX ------>   BUXcoin
124 -  BUZZ ----->   BuzzCoin
125 -  BWK ------>   Bulwark
126 -  BWS ------>   BitcoinWSpectrum
127 -  BWT ------>   Bittwatt
128 -  BYC ------>   Bytecent
129 -  BYND ----->   Beyondcoin
130 -  BYTOM ---->   Bytom
131 -  C20 ------>   Crypto20
132 -  C2 ------->   Coin2
133 -  C8 ------->   C8H10N4O2
134 -  CAB ------>   CabbageUnit
135 -  CACH ----->   CacheCoin
136 -  CADASTRAL ->   Bitland
137 -  CAG ------>   ChangeNOW
138 -  CAN ------>   CanYaCoin
139 -  CANN ----->   CannabisCoin
140 -  CAP ------>   Bottlecaps
141 -  CARAT ---->   CARAT
142 -  CASH ----->   Cashcoin
143 -  CAT ------>   BlockCAT
144 -  CBT ------>   CommerceBlock
145 -  CBX ------>   Crypto Bullion
146 -  CCC ------>   CyClean
147 -  CCL ------>   Ccore
148 -  CCP ------>   CampusCoin
149 -  CCRB ----->   CryptoCarbon
150 -  CCS ------>   CryptoCashbackRebate
151 -  CCT ------>   Crystal Clear Token
152 -  CDCC ----->   CDCC
153 -  CDN ------>   Canada eCoin
154 -  CDT ------>   CoinDash
155 -  CDX ------>   Commodity Ad Network
156 -  CEA ------>   Centra
157 -  CEEK ----->   Ceek VR
158 -  CEN ------>   Centurion
159 -  CENNZ ---->   Centrality
160 -  CETI ----->   CETUS Coin
161 -  CF ------->   Californium
162 -  CFC ------>   CoffeeCoin
163 -  CFUN ----->   CFun
164 -  CHAIN ---->   Chainmakers
165 -  CHAT ----->   ChatCoin
166 -  CHEAP ---->   Cheapcoin
167 -  CHECK ---->   CheckCoin
168 -  CHESS ---->   ChessCoin
169 -  CHIPS ---->   CHIPS
170 -  CHSB ----->   SwissBorg
171 -  CHT ------>   Coinhe Token
172 -  CIC ------>   CiCoin
173 -  CID ------>   Cryptocurrency eXchange
174 -  CIX ------>   Cryptonetix
175 -  CJ ------->   Cryptojacks
176 -  CKB ------>   Nervos Network
177 -  CLAM ----->   Clams
178 -  CLO ------>   Callisto Network
179 -  CLOAK ---->   CloakCoin
180 -  CLR ------>   Celer Network
181 -  CLUB ----->   ClubCoin
182 -  CLUD ----->   CludCoin
183 -  CLAM ----->   Clams
184 -  CMC ------>   CosmosCoin
185 -  CMT ------>   Comet
186 -  CND ------>   Cindicator
187 -  CNN ------>   Content Neutrality Network
188 -  CNO ------>   Coin(O)
189 -  CNT ------>   Centurion
190 -  COAL ----->   BitCoal
191 -  COB ------>   Cobinhood
192 -  COC ------>   Community Coin
193 -  COE ------>   CoEval
194 -  COFI------>   CoinFi
195 -  COLL ----->   COLL
196 -  COLX ----->   ColossusXT
197 -  COM ------>   Commercium
198 -  CON ------>   PayCon
199 -  CONI ----->   CoinBene Token
200 -  COSS ----->   COSS"""
}

def Start_Handller( update : Update , context : CallbackContext ):
    # Get first Name and Chat ID
    name = update.message.chat.first_name
    chat_id = update.message.chat_id
    # Send Message Hello
    context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.2)
    update.message.reply_text(Messages['msg_start'].format(name))
    # Seve Chat Id 
    ChatIDManagement.Send(ChatID=chat_id) 

def GetRate_Handller( update : Update , context : CallbackContext ) :
    # Get Chat Id
    chat_id = update.message.chat_id
    # Get Args  
    Currencies = context.args
    # Control Warning
    try : Coin1 = Currencies[0]
    except IndexError : context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.2) ; update.message.reply_text(Messages['msg_Warning_getrate']) ; return
    
    Coins = ''
    _Dict_Coin = []
    for coin in Currencies[1:]: Coins += coin + ',' ; _Dict_Coin.append(coin)
    
    # Control Warning
    if len(Currencies) < 2 :
        context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.2)
        update.message.reply_text(Messages['msg_Warning_getrate'])
        return
    
    # Get Data
    repouns =  Get(coin1= Coin1 , coin2=Coins , API='2bf1ee827a234b6a572cb202c95a5938f41a02071fb935f08587ed4531ae9f1c')
    TextResult = ''
    for coin in _Dict_Coin :
        try :
            TextResult +=  f"{Coin1} -> {coin} : {repouns[coin]}\n"
        except KeyError : 
            TextResult +=  f"این ارز وجود ندارد {coin}\n"
    update.message.reply_text(TextResult)

def CoinList_Handller(update : Update , context : CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.3)
    update.message.reply_text(Messages['msg_list_coins'])
    context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.3)
    update.message.reply_text(Messages['msg_list_coin_2'])

def Help_Handller(update : Update , context : CallbackContext):
    # Get Chat id
    chat_id = update.message.chat_id
    # Chat Action
    context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.3)
    update.message.reply_text(Messages['msg_help'])

def About_Handller(update : Update , context : CallbackContext):
    # Get Chat id
    chat_id = update.message.chat_id
    # Chat Action
    context.bot.send_chat_action(chat_id , ChatAction.TYPING) ; sleep(0.3)
    update.message.reply_text(Messages['msg_abut'])

# Main
if __name__ == '__main__' :
    # Get API Token
    TOKEN = open('Token.txt' , 'r').readline()
    
    # Updater
    updater = Updater(token=TOKEN)

    # #  # Commands ... # # #

    updater.dispatcher.add_handler(CommandHandler('start' , Start_Handller))

    updater.dispatcher.add_handler(CommandHandler('getrate' , GetRate_Handller))

    updater.dispatcher.add_handler(CommandHandler('help' , Help_Handller))

    updater.dispatcher.add_handler(CommandHandler('coinslist' , CoinList_Handller))

    updater.dispatcher.add_handler(CommandHandler('about' , About_Handller))

    # Start Bot
    updater.start_polling()
    updater.idle()