label op01:
    $ save_name = _("オープニング")
    play music "audio/bgm/bgm16.ogg"

    play sound "audio/sound/se119.ogg" loop

    "（タッタッタッタッ……）"

    kosuke "「急げ！　急ぐんだ！」"
    kosuke "「早くしないと、今日発売のエロゲー『いたずら女神ラヴちゃん』の限定特典が無くなってしまうっ！！」"
    kosuke "「あの『女神さま抱き枕』を貰って、俺は今日から甘酸っぱい夏休みを過ごすんだ！」"

    scene bg24
    with ImageDissolve("images/wipe/06.png", 1.0)

    kosuke "「ハァ……ハァ……ハァ……ハァ……！」"

    stop sound

    kosuke "「んー、ハァハァ言ってると、なんだか萌えてるみたいだ」"
    kosuke "「なんてこと言ってる場合じゃない！　とにかく走れっ！」"

    play sound "audio/sound/se119.ogg" loop

    scene black
    with ImageDissolve("images/wipe/06.png", 1.0)

    scene bg25
    with ImageDissolve("images/wipe/06.png", 1.0)

    kosuke "「よし、目標接近！　あの角を曲がったらすぐだっ！　加速しちゃうぜ装置・スイッチオン！（カチーンッ！！）」"

    stop music
    play sound "audio/sound/se040.ogg"

    scene fau_h000_big

    stop sound

    kosuke "「ぶはっ」"

    $ fauna_name = _("？？？")

    voice "audio/voice/op01/op01_1000.ogg"
    fauna "「きゃっ」"

    kosuke "「な、なんだ！？　顔に何か柔らかいものがぶつかったぞ！？」"

    scene fau_h000
    play music "audio/bgm/bgm19.ogg"

    kosuke "「こ、これは……」"
    "おぱんつ……というか、おにゃのこのお尻！？"
    kosuke "「な、なんでこんな所におにゃのこのお尻が！？」"
    kosuke "「ほ、本物かな。それとも、今エロゲーのことしか頭に無い俺の素晴らしき妄想力……？」"
    kosuke "「ちょっと触ってみよーっと」"

    play sound "audio/sound/se040.ogg"
    "（なでなで）"

    $ fauna_name = _("女の子")

    voice "audio/voice/op01/op01_1001.ogg"
    fauna 008 "「きゃんっ！　お尻、撫でられてる！？」"

    kosuke "「わっ」"

    "綺麗な足がジタバタと動く。"

    kosuke "「うーん、本物だったか……」"
    kosuke "「って、ちょっ……この子、浮いてない！？」"

    voice "audio/voice/op01/op01_1002.ogg"
    fauna 009 "「あの、どなたか存じませんが、スカートが引っかかって降りられないんです！　手伝って頂けませんか？」"

    kosuke "「え？」"

    voice "audio/voice/op01/op01_1003.ogg"
    fauna 010 "「お願いしますっ！」"

    kosuke "「は、はいっ！」"

    "俺は慌てて、白い太股を軽く掴んだ。"

    voice "audio/voice/op01/op01_1004.ogg"
    fauna 008 "「きゃっ！　太股、くすぐったいですっ！」"

    kosuke "「そ、そんな事言ったって！」"
    kosuke "「よ、よし、じゃあ太股をしっかり抱えて……わ、目の前におにゃのこのぱんつがっ！！」"

    voice "audio/voice/op01/op01_1005.ogg"
    fauna 008 "「ふわっ！　太股の内側に指が……！　だめっ、そんな所触られたら、わたし感じちゃうぅっ！！」"

    kosuke "「わっ、こらっ！　足をバタバタさせない！　体も揺らさないで！　これじゃ掴みにく…………うわぁっ！！」"

    voice "audio/voice/op01/op01_1006.ogg"
    fauna 008 "「きゃっ！」"

    "引っ掛かりが取れたのか、突然、女の子が落下を始めた。"

    kosuke "「危ない！！」"

    "俺は咄嗟に彼女をキャッチしようとした。"
    "が……！"

    jump op02
