"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    # print the value counts for pregnum
    print(resp.pregnum.value_counts())

    # test whether this df is the correct size
    assert (len(resp) == 7643)

    # check if the value count matches the pregnancy file
    assert (resp.pregnum.value_counts()[1] == 1267)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
