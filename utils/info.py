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
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6471432077:AAHhFOnRuhUTuBy3gnNbLE11DZ_aEl00llU")
SESSION      = os.environ.get("SESSION", "BQFOv5QAWPlIUyFD5u5-haj_rUat7TGNU-lp5iv8wF1CCq7gPaibzW7PgYxUqkUBAlnyGtBTz6gOuPqtwGmHeJzWHH_rzco4ZdPDKCcUtXs5MTKC3yfvwJZ5cWlbg_WmMHYlaTXuq4-CgWM7gVE1kq0_P730J1wKZJCgyH-K3HEOzQkB1yVn6uJhGPydO8FxL8yNNBaU157jtV0qWvpe47-95mZk9sHdSGxnpjqzpAVEjFw7yCs1xthbNiKMkrcutbCiNps4jvb9sRpwNjd1vxao6PMExxHTcQYmZn50G_AhBFVqZD2IzGIFO6PMizxc5kjmEMrtKgwBugH_-dO6xVX7tt0nAAAAAAFY9mSPAA")
TIME         = int(os.environ.get("TIME", 3600))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001920976113").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Autodeletebot:yuvraj178@autodeletebot.khceugr.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
