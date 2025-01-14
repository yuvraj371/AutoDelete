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
SESSION      = os.environ.get("SESSION", "BQFOv5QATjy-qsL-DvRZ_ov3ygPRpWzGKP1uqSzg3tQhGISObg9Be8_uq2GK3se3QONt1_rp4ZJqt7ixDRK5OYKDphM2NVw5jAp5V5M7ZN9rWABERVz0fENeEsTyOzT3n96eBbMn5c0z4jRcPkJnqHf1oFS-svGcnQz7BikaEpYh2VjmiswdOT9aTnVURk8DJqRwMbdzvfgDAc7YOPWTDyNln5_H_IIskKLF-pPEM-CvCWEuL51uH5Go2guNMVAIz2UgLMHr8a_2Mt9eZkTS1Tue7U5SiB7AI0DtXtKewnTRSoYSzdY6Xzyr2UDDBWalI-i_G1U-iZyvhDlYAjfKa_G5Rs2zTwAAAAFY9mSPAA")
TIME         = int(os.environ.get("TIME", 420))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001971491129 -1001929049930 -1001920976113 -1001922942986").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Autodeletebot:Yuvraj178@autodeletebot.5v4tirm.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
