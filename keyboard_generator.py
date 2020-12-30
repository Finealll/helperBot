# -*- coding: utf-8 -*-
import json

BLUE = 'primary'
WHITE = 'default'
GREEN = 'positive'
RED = 'negative'


class Button:
    TYPE_TEXT = 'text'
    TYPE_LOCATION = 'location'
    TYPE_VK_PAY = 'vkpay'
    TYPE_VK_APPS = 'open_app'
    TYPE_OPEN_LINK = 'open_link'
    TYPE_CALLBACK = 'callback'

    @staticmethod
    def text(label: str, color: str = None, payload: dict = None):
        if payload is None:
            payload = {}

        if color is None:
            color = WHITE

        data = {
            "action": {
                "type": Button.TYPE_TEXT,
                "label": label,
                "payload": payload,
            },
            "color": color
        }

        return data

    @staticmethod
    def link(link: str, label: str = None, payload: dict = None):
        if payload is None:
            payload = {}

        if label is None:
            label = link

        data = {
            "action": {
                "type": Button.TYPE_OPEN_LINK,
                "link": link,
                "label": label,
                "payload": payload,
            }
        }

        return data

    @staticmethod
    def location(payload: dict = None):
        if payload is None:
            payload = {}

        data = {
            "action": {
                "type": Button.TYPE_LOCATION,
                "payload": payload,
            }
        }

        return data

    @staticmethod
    def vk_pay(vk_pay_hash: str, payload: dict = None):
        if payload is None:
            payload = {}

        data = {
            "action": {
                "type": Button.TYPE_VK_PAY,
                "hash": vk_pay_hash,
                "payload": payload,
            }
        }

        return data

    @staticmethod
    def vk_app(app_id: int, label: str, owner_id: int = None, app_hash: str = None, payload: dict = None):
        if payload is None:
            payload = {}

        data = {
            "action": {
                "type": Button.TYPE_VK_APPS,
                "app_id": app_id,
                # "owner_id": owner_id,
                "label": label,
                # "hash": app_hash,
                "payload": payload,
            }
        }

        return data

    @staticmethod
    def callback(label: str, payload: dict = None):
        if payload is None:
            payload = {}

        data = {
            "action": {
                "type": Button.TYPE_CALLBACK,
                "label": label,
                "payload": payload,
            }
        }

        return data

class KeyBoard:
    def __init__(self, one_time: bool = False, inline: bool = False, one_line: bool = False):
        self.keyboard = {
            "one_time": one_time,
            "inline": inline,
            "buttons": [],
        }
        self.buttons = []
        self.one_line = one_line

    def load(self, buttons: list):
        self.buttons = buttons
        res = []
        if self.one_line:
            res.append([])
            for i in range(len(buttons)):
                res[0].append(buttons[i])

        else:
            for i in range(len(buttons)):
                res.append([])
                res[i].append(buttons[i])

        self.keyboard['buttons'] = res
        return self.keyboard


    def get(self):
        return json.dumps(self.keyboard, ensure_ascii=False)



