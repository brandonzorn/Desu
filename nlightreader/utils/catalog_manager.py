from nlightreader.parsers import (
    Desu,
    MangaDex, MangaDexLib,
    ShikimoriBase, ShikimoriRanobe, ShikimoriManga, ShikimoriLib, ShikimoriAnime,
    Rulate, Erolate,
    Ranobehub,
    Remanga,
    NHentai, AllHentai,
    LibRanobelib, LibMangalib, LibAnilib,
    SlashLib, MangaLib,
)


CATALOGS = {
    0: Desu,
    1: ShikimoriBase,
    2: MangaDex,
    3: Rulate,
    4: Ranobehub,
    5: Erolate,
    6: Remanga,
    7: NHentai,
    8: AllHentai,
    9: SlashLib,
    10: MangaLib,
    11: ShikimoriAnime,
    13: LibRanobelib,
    14: LibMangalib,
    15: LibAnilib,
}
USER_CATALOGS = [
    Desu,
    MangaDex,
    Remanga,

    ShikimoriManga,
    ShikimoriRanobe,
    ShikimoriAnime,

    MangaLib,
    LibMangalib,
    LibRanobelib,
    LibAnilib,

    Rulate,
    Erolate,
    Ranobehub,

    SlashLib,
    NHentai,
    AllHentai,
]
LIB_CATALOGS = {ShikimoriBase: ShikimoriLib, MangaDex: MangaDexLib}


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
