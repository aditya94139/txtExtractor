#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6973701854:AAE2zRZAK23LkKJbAC7dJ84eVZonwkwar2A")
    API_ID = int(os.environ.get("API_ID", "23537723"))
    API_HASH = os.environ.get("API_HASH", "165f8ac57a0fc673437772bbffd315a4")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6767962475")
