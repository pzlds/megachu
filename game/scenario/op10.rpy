label op10:
    $ save_name = _("オープニング")

    play music "audio/bgm/bgm12.ogg"

    scene bg05d
    with ImageDissolve("images/wipe/09.png", 2)

    voice "audio/voice/op10/op10_0000.ogg"
    shuryo "「クロトよ、おるか」"

    $ klotho_name = _("クロト")

    show kur 211 at center
    with dissolve

    voice "audio/voice/op10/op10_0001.ogg"
    klotho "「はっ、首領様！」"

    voice "audio/voice/op10/op10_0002.ogg"
    shuryo "「女神が現れたようだな」"

    voice "audio/voice/op10/op10_0003.ogg"
    klotho "「はい」"

    voice "audio/voice/op10/op10_0004.ogg"
    shuryo "「天界のヤツらめ、『魔王の種』に気付いたな？」"

    voice "audio/voice/op10/op10_0005.ogg"
    shuryo "「まぁ良い。クロトよ、予定通り今宵から作戦を決行するのだ。そして、川神幸介の中に眠る魔王を目覚めさせるのだ！」"

    voice "audio/voice/op10/op10_0006.ogg"
    klotho "「はっ！」"

    stop music

    scene black
    with ImageDissolve("images/wipe/09.png", 2)

    scene bg01nlb
    with Dissolve(0.5)

    play sound "audio/sound/se115.ogg"

    kosuke "「ふぁぁー……」"
    kosuke "「なんだか今日はいろいろあって疲れたなぁ」"
    kosuke "「さっさと寝ちまおう……」"

    play sound "audio/sound/se118.ogg"

    scene bg01ndb
    with Dissolve(0.5)

    play sound "audio/sound/se115.ogg"

    kosuke "「良い夢見られますように。おやすみ……」"
    kosuke "「（できればえっちな夢希望……）」"

    "………………。"
    "…………。"
    "……。"

    scene black
    with ImageDissolve("images/wipe/20.png", 2)

    jump in_op