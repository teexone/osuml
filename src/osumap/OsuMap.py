import re
from src.osumap.HitObject import HitObject 

class OsuMap:

    INTEGER = r"\d+"
    COMMA_SEPARATED_LIST = r"\w(?:,\w)*"
    COLON_SEPERATED_LIST = r"\w(?:\:\w)*"

    SECTIONS = re.compile(r"\[(?P<SECTION_NAME>\w+)\]\s(?P<SECTION_CONTENT>[^\[]+)")
    HIT_OBJECT = re.compile(f"(?P<x>{INTEGER}),"
                            f"(?P<y>{INTEGER}),"
                            f"(?P<time>{INTEGER}),"
                            f"(?P<type>{INTEGER}),"
                            f"(?P<hit_sound>{INTEGER}),"
                            f"(?:(?P<obj_params>{COMMA_SEPARATED_LIST}),)?"
                            f"(?P<hit_sample>{COLON_SEPERATED_LIST})\:") 

    

    def __init__(self, inputs) -> None:
        if isinstance(inputs, str):
            self.data = self._parse(inputs)
        pass

    def _parse(self, text):
        # https://osu.ppy.sh/wiki/en/Client/File_formats/Osu_%28file_format%29
        hit_objects = []
        for section_name, section_content in re.findall(OsuMap.SECTIONS, text):
            if section_name == "HitObjects":
                hit_objects.extend(re.findall(OsuMap.HIT_OBJECT, section_content))
        return list(map(lambda args: HitObject(*args), hit_objects))
        



        

