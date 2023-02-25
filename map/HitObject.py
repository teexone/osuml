from typing import NamedTuple

HitObject = NamedTuple("HitObject", 
                        x=int, 
                        y=int, 
                        time=int, 
                        type=int, 
                        hit_sound=int, 
                     # "obj_params",        skipped since not used
                     # "hit_sample"         skipped since not used
)
