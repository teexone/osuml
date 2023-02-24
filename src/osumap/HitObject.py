from typing import NamedTuple, Any


class HitObject:
    def __init__(self, x, y, time, type, hit_sound, obj_params, hit_sample) -> None:
        self.x = int(x)
        self.y = int(y)
        self.time = int(time) / 1000
        self.type = int(type)
        self.hit_sound = int(hit_sound)
        self.obj_params = obj_params
        self.hit_sample = hit_sample
    