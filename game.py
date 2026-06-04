import json
import os
from config import SAVE_FILE

DEFAULT_DATA = {
    "high_score": 0,
    "coins": 0,
    "unlocked_cars": ["neon_drift"],
    "selected_car": "neon_drift",
    "sfx_volume": 0.5,
    "music_volume": 0.3
}

class Database:
    def __init__(self):
        self.data = DEFAULT_DATA.copy()
        self.load()

    def load(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    loaded = json.load(f)
                    for key, val in DEFAULT_DATA.items():
                        if key not in loaded:
                            loaded[key] = val
                    self.data = loaded
            except Exception as e:
                print(f"Failed to load save data: {e}. Resetting to defaults.")
                self.data = DEFAULT_DATA.copy()
                self.save()
        else:
            self.data = DEFAULT_DATA.copy()
            self.save()

    def save(self):
        try:
            with open(SAVE_FILE, "w") as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"Failed to save data: {e}")

    def get_high_score(self):
        return self.data.get("high_score", 0)

    def set_high_score(self, score):
        if score > self.data["high_score"]:
            self.data["high_score"] = score
            self.save()
            return True
        return False

    def get_coins(self):
        return self.data.get("coins", 0)

    def add_coins(self, amount):
        self.data["coins"] = max(0, self.data["coins"] + amount)
        self.save()

    def deduct_coins(self, amount):
        if self.data["coins"] >= amount:
            self.data["coins"] -= amount
            self.save()
            return True
        return False

    def get_selected_car(self):
        return self.data.get("selected_car", "neon_drift")

    def set_selected_car(self, car_id):
        self.data["selected_car"] = car_id
        self.save()

    def is_car_unlocked(self, car_id):
        return car_id in self.data.get("unlocked_cars", ["neon_drift"])

    def unlock_car(self, car_id):
        if car_id not in self.data["unlocked_cars"]:
            self.data["unlocked_cars"].append(car_id)
            self.save()

    def get_sfx_volume(self):
        return self.data.get("sfx_volume", 0.5)

    def set_sfx_volume(self, vol):
        self.data["sfx_volume"] = max(0.0, min(1.0, vol))
        self.save()

    def get_music_volume(self):
        return self.data.get("music_volume", 0.3)

    def set_music_volume(self, vol):
        self.data["music_volume"] = max(0.0, min(1.0, vol))
        self.save()

db = Database()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

