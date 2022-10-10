from all_madlibs import Madlib1, MadlibRomeoJuliet, MadlibWar, MadlibBeatlesSong

import random

if __name__ == "__main__":
    m = random.choice([Madlib1, MadlibRomeoJuliet, MadlibWar, MadlibBeatlesSong]) 
    m.madlib()