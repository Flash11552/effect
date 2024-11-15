from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", 7701053753:AAGmFujoXiZp3SAONBhqEbqNAfI4KDgcAw0)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", AgE3dlgAFqUwmM6Ed2SN5BoPhmBCtzEIEZSes2dtBv2Tzd4LPCfiHuwjBCFfHerz7dEnSRX1n_aYejjufXu3z6-H6io3ESaDaLrZ_IfjzEriSsQbbCRb350UXRoneDWPs3UZwtm-qPCFgaZudTdrYObEhn23HQRHaKojjXgpDj92Kv8rYkDTCpTW7eUJRQ_TD4hco6WP0clLLCqSGKxeiPx4P7QU6-mvAmuZxs9gpqJO0iKazriv8duP35-MnOHPV3LoXRGkuf2D9UEY6QeXVTc6KusgliKhiAUycR2gBZM_V070MFwfiSyXwtvjnw42mT1RthfR6O1TLIEijC7SWYu4gzkwAAAAFjuAY9AA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
