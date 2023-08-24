#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "21938068"))
API_HASH     = os.environ.get("API_HASH", "c18fd98f3e58484df0aecd95a3d5a6a9")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "BQFOv5QATBQj9Bn7HHqZ_m7JmYE4HcMRohsbPpJfGMcn0P4ZPEDdY1mM1dVI3J39-VFX6v65nBhsREtUrM6cCUxht8qJczjsXiYKpXIEDbPYW6q74FldqDBTNVUOx-b8O5CEbThTpaaHnh1OoOjoWq5jN8dQpjgQrF05JguEzRpPceSSKvKMW_DDFKaTu42GNmg0IBCjaATwxaEqQ1Rcmu7vDVGb8vxIKFh23AI_wLzVfRaKvkn6HxRVJR0ZpR-l5o1APv_XZUYmN8hRhCq6YmAN1GjeF5apsjfzdlHoCuambXfEl00FSpVpvlwcPEfjlT6tROSPhmuiFllA_qI_KTMZ_qaG_gAAAAGBujeNAQ")
SESSION      = os.environ.get("SESSION", "Y6XJlFjg9WmeY7LGQ7eQAAAAFY9mSPAA")
TIME         = int(os.environ.get("TIME", 3600))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001920976113").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Autodeletebot:yuvraj178@autodeletebot.khceugr.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
