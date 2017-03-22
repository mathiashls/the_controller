class SKYHDTV(object):
    message_delay = 0.5
    buttons = {
        # CHANNEL_DOWN
        'j': '50027800750078003a003c003a003d0039003d007500780075003c0075003d0075007800390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # CHANNEL_UP
        'k': '510278007400790039003d0039003d0039003d00750078003900790074003d0075003d00390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # VOLUME_UP
        'l': '50027800750078003a003c003a0078003a00780075003c003a00780039003d0075007800390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # VOLUME_DOWN
        'h': '510278007400790039003d00390078003900790074003d003a00780039003d0075007800390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_0
        '0': '50027800750078003a003c003a003d003900780039003d003a0078003900790075003c00390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_1
        '1': '510277007500790039003d0039003d0039003d0039003d003a0078003a003d0039007800390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER 2
        '2': '510277007500790039003d0039003d0039003d0039003d0075003d0039003d0075003d00390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_3
        '3': '510277007500790039003d0039003d0039003d0039003d00750078003a003d0075007800390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_4
        '4': '50027800750078003a003d0038003e0039003d00390078003a003d0039003d00750077003a0000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_5
        '5': '50027800750078003a003d0039003d0039003d003a007800390078003a0078003a003c003a0000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_6
        '6': '51027700750078003a003d0039003d003a003c003a00780075003c003a007800390078003a0000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_7
        '7': '510278007400790039003d0039003d0039003d0039007800750079003900780075003d00390000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_8
        '8': '510278007400790039003d0039003d0039003d0076003c0039003d003a00780075003c003a0000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa

        # NUMBER_9
        '9': '500278007500780039003d003a003d0039003d0075003c003a00780039007900740078003a0000003a003d0039003d0039002c003400ab0035003a003500ab0035003a003500ab0035003a003500aa003500ab0035003a0035003a0035003a0035003b0034003a003500ab0035003a0035003a003500ab003500ab003500ab003400ab00350000003500aa0033003c0035003b0034003a003000400034003a003600aa0035003a0035003a003300ad003500ab003200ae003400ab0035000d00010011000100bf000000df000000df00010019000000c40011001c000000b2000000140001000d0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000140000000000000028000000',  # noqa
    }