from kesi import Ku


def tsingkuihua(han, lo):
    ku = Ku(han.lstrip('-').lower(), lo.lstrip('0').lstrip('-').lower()).TL()
    return ku.hanlo, ku.lomaji
