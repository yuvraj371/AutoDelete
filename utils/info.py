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

API_ID       = int(os.environ.get("API_ID", "10246965"))
API_HASH     = os.environ.get("API_HASH", "ef650551668be9e53efb691180ce0880")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6690067645:AAHRqm4-dvU3s4gjS07d9CEFPdInWB6D2ak")
SESSION      = os.environ.get("SESSION", "BQCcWzUAichAsdFVVzrkUZFZdivo5Mqp7J8xGj5ZoTUVz8OivMoVTD6AVXe0xGFOZpWkrE7cPLwg_H_KdBd6qX0iR2r7uA_Rw7uFBvk1ZriPA4UzIQnwyPmptM_s2nnkFxVouqei7zX1hRT-QHLqAdMBSy6SqecZj6uCyR8TC97q2c_YqW51nOPSuDBiGBIEFUW2jUo53ITmB6hf7SdsqY4_uLDLbOomP0XOligQXVSj8TYYx1a68IKjdjf50GZO4a3VQA5HlKCG7SVWmAqzlyQuJRgxpv0xilIziamQAw6ocd4GubfToI84bSrSPJfxSnrgLpitad2HxwoE6fNJoiNp3x5XOwAAAABQjsH4AA")
TIME         = int(os.environ.get("TIME", 1200))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001699421068 -1001969653899 -1001940605857").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Autodeletebot:Dharamveer1100@cluster0.luyy59m.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
