# -*- coding: utf-8 -*-
# :Project:   pg_query -- DO NOT EDIT: automatically extracted from lockoptions.h @ 10-latest-0-g1ec5c22
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017 Lele Gaifax
#

import enum


class LockClauseStrength(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/lockoptions.h#L21>`__."

    LCS_NONE = 0
    LCS_FORKEYSHARE = enum.auto()
    LCS_FORSHARE = enum.auto()
    LCS_FORNOKEYUPDATE = enum.auto()
    LCS_FORUPDATE = enum.auto()

class LockWaitPolicy(enum.IntEnum):
    "See `here for details <https://github.com/lfittl/libpg_query/blob/1ec5c22/src/postgres/include/nodes/lockoptions.h#L36>`__."

    LockWaitBlock = 0
    LockWaitSkip = enum.auto()
    LockWaitError = enum.auto()
