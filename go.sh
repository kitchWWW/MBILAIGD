#!/bin/bash

clingo 3 generator.lp chords-general.lp prettify.py


# generate guitar chords things
#clingo 0 generator.lp chords-2.lp prettify.py chords-general.lp 

# generate a sp1 counterpoint voice above the specified cf
#clingo 10 generator.lp sp-general.lp sp-1.lp sp-cantus/c.lp prettify.py --parallel-mode 4

# generate a line that is valid counterpoint forward and backwards
#clingo 10 generator.lp sp-general.lp sp-no-cantus.lp sp-cantus/puzzle.lp prettify.py --parallel-mode 4

# generate a canon 5 notes offset at the octave
#clingo 10 generator.lp sp-general.lp sp-no-cantus.lp sp-cantus/canon.lp prettify.py --parallel-mode 4
