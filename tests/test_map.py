from map.OsuMap import OsuMap

if __name__ == "__main__":
    with open("./tests/test.osu") as inpt:
        mp = OsuMap(inpt.read())    
        print(mp.data)