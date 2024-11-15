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

SESSION = getenv("SESSION", AgE3dlgALqM02yMVAwXLrnYjDtyGdTFlO-U33WEVUjDq5nnp0ag6B3Xzlzj_4Cr5ZHU-Z8xQsGnCcIFQ8hWHDyQype3GR9hLToZuykJnSYBk6lfp4T3E2UNoEbJTTKK1HYVICqtAlqfc1AsUYyhcK8blZbX2QAdJ6_uERrtdGJUXBEKeCwe7J2gONNMe9CRgETvX6z5QompUNb8syCJF4gxaYckBNHwU5DvbBudYIk_sEB6otsALB3pjiU_J8p0LqFoZ_JhSlBD35n9TQadOcqRZNKc9v0sJprDY02rBFhUJ3o6f4EmZ4RmeMNn1uj12twjqXg463zTNzwCDEQecYfoF2GkULQAAAAFjuAY9AA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
