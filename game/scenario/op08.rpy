label op08:
    $ save_name = _("オープニング")

    # TODO: ^music,bgm01,,500
    # TODO: \clk,1000
    play music "audio/bgm/bgm01.ogg"

    $ fauna_name = _("女の子Ａ")
    $ jordh_name = _("女の子Ｂ")

    voice "audio/voice/op08/op08_0000.ogg"
    fauna "「ごめんくださーい」"

    kosuke "「…………」"

    voice "audio/voice/op08/op08_0001.ogg"
    jordh "「ごめんくださーい！」"

    scene bg01b
    with Dissolve(2)

    kosuke "「……んん……？　なんだぁ……？」"

    voice "audio/voice/op08/op08_0002.ogg"
    jordh "「ねぇ、勝手に入っちゃおうよ」"

    voice "audio/voice/op08/op08_0003.ogg"
    fauna "「だめよ。きちんとご挨拶しないと」"

    kosuke "「…………」"

    "玄関から女の人の声が聞こえてくる。"
    "このアパート、壁が薄いから声が筒抜けなんだよな。"

    voice "audio/voice/op08/op08_0004.ogg"
    fauna "「ごめんくださーい」"

    "管理人さん、いないのかな。"

    voice "audio/voice/op08/op08_0005.ogg"
    jordh "「ごはんくださーい」"

    voice "audio/voice/op08/op08_0006.ogg"
    fauna "「お食事処じゃないのよ？」"

    voice "audio/voice/op08/op08_0007.ogg"
    jordh "「お腹減ったのよ」"

    voice "audio/voice/op08/op08_0008.ogg"
    fauna "「さっきハンバーガーとか言うのを食べたばかりでしょ？」"

    voice "audio/voice/op08/op08_0009.ogg"
    jordh "「こんなことならテイクオフすればよかった」"

    voice "audio/voice/op08/op08_0010.ogg"
    fauna "「テイクアウトよ。離陸してどうするの」"

    voice "audio/voice/op08/op08_0011.ogg"
    jordh "「ごはんくださーい」"

    "……なんなんだ。"
    "仕方ない、俺が行くか。"

    scene bg07
    with Dissolve(2)

    kosuke "「はーい、どちらさま……あっ！」"

    stop music

    show fau 001 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op08/op08_0012.ogg"
    fauna "「おはようございますぅっ」"

    voice "audio/voice/op08/op08_0013.ogg"
    jordh 001 "「おはようございまーす」"

    play music "audio/bgm/bgm12.ogg"

    kosuke "「き、君たちは！！」"

    "昨日の惨劇が鮮明に蘇る。"

    voice "audio/voice/op08/op08_0014.ogg"
    fauna 000 "「はい。実はわたしたち、今日からここに……」"

    kosuke "「やっぱりあれは夢なんかじゃなかったんだ！　やばっ、逃げなきゃ！」"

    voice "audio/voice/op08/op08_0015.ogg"
    fauna 008 "「あ、あの！　どうなさったのですか？」"

    show jor 003 at left
    with dissolve

    kosuke "「どうなさったのって、昨日、人のこと散々……うわ！」"

    play sound "audio/sound/se015.ogg"

    # TODO: ^effect,Quake,1000
    # TODO: \clk,1000

    kosuke "「イテテ……。何で転んだんだ……？」"

    voice "audio/voice/op08/op08_0016.ogg"
    fauna 002 "「姉さんっ」"

    voice "audio/voice/op08/op08_0017.ogg"
    jordh 000 "「さあねー」"

    voice "audio/voice/op08/op08_0018.ogg"
    fauna 009 "「あの、大丈夫ですか？」"

    kosuke "ひえっ……！！　こっち来んなっ！」"

    voice "audio/voice/op08/op08_0019.ogg"
    fauna "「あの、ひょっとして、どなたかと勘違いされていませんか？」"

    stop music

    kosuke "「……へ？　勘違い？」"

    play music "audio/bgm/bgm01.ogg"

    voice "audio/voice/op08/op08_0020.ogg"
    jordh 007 "「私ーたち、ユーと会うのは今日が初めてでーすよー？」"

    kosuke "「そんな……！　だってキミ達は……！」"

    voice "audio/voice/op08/op08_0021.ogg"
    fauna 000 "「あ、わたしは昨日会いましたけど……。街でぶつかって倒れて……」"

    voice "audio/voice/op08/op08_0022.ogg"
    jordh 001 "「Ｏｈ！　ファウナの言ってたカレはカレのことですかー？　カレーバーガー、辛ぇー辛ぇーでーす」"

    kosuke "「……何言ってるんですか？」"

    voice "audio/voice/op08/op08_0023.ogg"
    fauna 008 "「すっ、すみません、姉はまだこの国の言葉をちゃんと話せなくて……」"

    kosuke "「はぁ……。すると外国の方……？」"

    show fau 000 at right
    with dissolve

    voice "audio/voice/op08/op08_0024.ogg"
    jordh "「いえーす！　嘘じゃありませーん」"

    kosuke "「…………」"
    kosuke "「（確かに、昨日俺を襲った二人に似てるけど、お姉さんはこんな喋り方じゃなかったよな……）」"
    kosuke "「（すると、やっぱり別人……？）」"
    kosuke "「（でも、あの髪の毛にある羽根、気になるよなァ）」"
    kosuke "「ねえ、その頭の羽根、何？」"

    voice "audio/voice/op08/op08_0025.ogg"
    fauna 007 "「え？　羽根……？」"

    show fau 008 at right
    show jor 008 at left
    with dissolve

    voice "audio/voice/op08/op08_0026.ogg"
    fauna "「ああっ！」"

    voice "audio/voice/op08/op08_0027.ogg"
    fauna "「（忘れてたわ！）」"

    voice "audio/voice/op08/op08_0028.ogg"
    jordh "「（そうか、付いてて当たり前のものだから、全然気にしなかった！）」"

    voice "audio/voice/op08/op08_0029.ogg"
    fauna 010 "「こ、これはその……」"

    voice "audio/voice/op08/op08_0030.ogg"
    jordh 000 "「ファ、ファッションでーす！　おふらんすで流行の、最新のファッションでーす！」"

    kosuke "「ああ、そうなんだ。俺、そう言うの全然知らないからなぁ……はは……」"
    kosuke "「（そうだよなぁ。もし俺を騙すつもりなら、そんなわかり易い物を付けたままにするわけないよなぁ……）」"
    kosuke "「（しかも、昨日は問答無用に襲って来たんだ。同じ人ならこんな和やかに会話したりしないよなぁ……）」"
    kosuke "「（…………）」"
    kosuke "「（いいや、別人！　うん。もう別人ってことでＯＫ！）」"
    kosuke "「それで、このアパートに何か用ですか？」"

    voice "audio/voice/op08/op08_0031.ogg"
    fauna 000 "「そ、そうでした。自己紹介が遅れました。わたしはファウナ。本日よりこの弁天荘に住まわせて頂きます。どうぞ宜しくお願いします」"

    "（ぺこり）"

    kosuke "「はぁ……。って、新しい住人！？」"

    $ fauna_name = _("ファウナ")
    $ jordh_name = _("ヨルズ")

    voice "audio/voice/op08/op08_0032.ogg"
    fauna 001 "「はい」"

    kosuke "「（こ、こんな美人が……？）」"

    voice "audio/voice/op08/op08_0033.ogg"
    fauna 000 "「そして、こちらが姉のヨルズです」"

    voice "audio/voice/op08/op08_0034.ogg"
    jordh 001 "「ハーイ、ヨルズでーす。宜しく頼むアルよー。ＨＡＨＡＨＡー」"

    voice "audio/voice/op08/op08_0035.ogg"
    fauna 009 "「ねぇ、普通に喋りましょうよ」"

    voice "audio/voice/op08/op08_0036.ogg"
    jordh 003 "「そんなことしたら正体バレちゃうじゃない」"

    voice "audio/voice/op08/op08_0037.ogg"
    fauna "「そうかしら……」"

    show jor 000 at left
    with dissolve

    kosuke "「…………」"
    kosuke "「（でも、こんな美女姉妹がこのボロアパートに引っ越してくるなんて事、有り得るんだろうか……？）」"
    kosuke "「（ひょっとして、本当はもっと良い家に住みたかったのに、外国人の住宅問題のせいでこんな家にしか住めないとか……？）」"
    kosuke "「（外国の人に対して我が国はなかなか厳しいからな……。この人たち、辛い思いをしてここまで来たのかもしれないなぁ）」"
    kosuke "「あの、ファウナさん」"

    voice "audio/voice/op08/op08_0038.ogg"
    fauna 000 "「あ、ファウナで良いですよ。えっと……」"

    kosuke "「あ、川神幸介です」"

    voice "audio/voice/op08/op08_0039.ogg"
    fauna "「じゃあ、幸介さんってお呼びしても良いですか？」"

    kosuke "「ええっ！？」"

    voice "audio/voice/op08/op08_0040.ogg"
    fauna 009 "「あ、嫌……でしたか？」"

    kosuke "「ノーノー、とんでもない！　大歓迎さっ！」"

    "『幸介さん』だって、『幸介さん』！　女の子に『名前＋さん』で呼ばれたのなんて初めてだ！　嬉しい！！"

    voice "audio/voice/op08/op08_0041.ogg"
    jordh 001 "「わたーしはヨルズでいいでーす。あなたのことー、幸介呼んじゃうねんからー」"

    kosuke "「（どこの言葉だ……）」"

    voice "audio/voice/op08/op08_0042.ogg"
    fauna 007 "「あの、何か訊きたいことがあったのでは？」"

    kosuke "「ああ、別に大したことじゃないんだけど……。二人はどうしてこのアパートに来たの？」"

    voice "audio/voice/op08/op08_0043.ogg"
    fauna 000 "「あ、えっと、実は私、この度Ｇ大学に留学が決定致しまして、昨日より住居を探していました所偶然こちらが見つかり、早速手続きを致しまして……」"

    kosuke "「え？　Ｇ大？」"

    voice "audio/voice/op08/op08_0044.ogg"
    fauna 001 "「はい。そうです」"

    kosuke "「お姉さんも？」"

    voice "audio/voice/op08/op08_0045.ogg"
    jordh 000 "「わたーしは彼女のマネージャーでーす。ジャーマネ、ジャーマネ……、ジャーマネ・スープレックス！」"

    kosuke "「え？　マネージャーって……君ってひょっとして芸能人か何か？」"

    voice "audio/voice/op08/op08_0046.ogg"
    jordh 003 "「わたーしのギャグは無視でーすか？」"

    kosuke "「（無視しとこう）」"

    voice "audio/voice/op08/op08_0047.ogg"
    fauna 000 "「いえ、そんなことはないですよ。わたしはただの学生で、姉さんはただの付き添いです」"

    voice "audio/voice/op08/op08_0048.ogg"
    jordh 001 "「Ｏｈ！　Ｙｅｓ！」"

    kosuke "「じゃあ、ファウナだけがＧ大生？」"

    voice "audio/voice/op08/op08_0049.ogg"
    fauna "「ええ、そうです」"

    kosuke "「実はさ、俺もＧ大なんだよね」"

    voice "audio/voice/op08/op08_0050.ogg"
    fauna 001 "「まぁ、そうだったんですかぁ〜！　奇遇ですねぇ〜♪」"

    kosuke "「どの学部？」"

    show fau 008 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op08/op08_0051.ogg"
    fauna "「え？　学部？」"

    kosuke "「うん、学部。あそこ総合大学だから、理系・文系なんでも有るんだよね。あ、それと学科は？」"

    voice "audio/voice/op08/op08_0052.ogg"
    fauna 010 "「え？　学科？　学部？　えっと、その……」"

    voice "audio/voice/op08/op08_0053.ogg"
    fauna 004 "「（姉さん）」"

    voice "audio/voice/op08/op08_0054.ogg"
    jordh 011 "「（アドリブで突っ走れ！）」"

    voice "audio/voice/op08/op08_0055.ogg"
    fauna "「（そんな……）」"

    kosuke "「どうしたの？」"

    voice "audio/voice/op08/op08_0056.ogg"
    fauna 009 "「ええーっと、あの、ちょっと思い出せなくて……」"

    kosuke "「え？　だって、自分の学科でしょ？」"

    voice "audio/voice/op08/op08_0057.ogg"
    fauna 008 "「そ、それはその……そうなんですけど、あの……」"

    kosuke "「……ホントにＧ大生なの？」"

    voice "audio/voice/op08/op08_0058.ogg"
    fauna 009 "「え、それは……その……」"

    voice "audio/voice/op08/op08_0059.ogg"
    fauna 010 "「（姉さん！　なんとかして！）」"

    voice "audio/voice/op08/op08_0060.ogg"
    jordh 009 "「（仕方ないわね）」"

    voice "audio/voice/op08/op08_0061.ogg"
    jordh 000 "「お疑いになりまーすか？」"

    kosuke "「あ、いや、そういうワケじゃ……」"

    voice "audio/voice/op08/op08_0062.ogg"
    jordh "「では、論より証拠をお見せしましょ〜」"

    kosuke "「証拠？」"

    voice "audio/voice/op08/op08_0063.ogg"
    jordh 001 "「パンツちら〜っ▼」"
    # TODO: 「パンツちら〜っ[c,$FFEC6C76]▼[c]」

    play music "audio/bgm/bgm19.ogg"

    voice "audio/voice/op08/op08_0064.ogg"
    fauna 008 "「きゃあっ！」"

    kosuke "「うおっ！？　純白……！　しかも……食い込み！？」"

    voice "audio/voice/op08/op08_0065.ogg"
    fauna 002 "「ね、姉さん、なんてこと！！」"

    voice "audio/voice/op08/op08_0066.ogg"
    jordh 011 "「我慢おし！」"

    voice "audio/voice/op08/op08_0067.ogg"
    fauna 005 "「あーん、スカート下ろしてぇ！」"

    voice "audio/voice/op08/op08_0068.ogg"
    jordh 001 "「ここでーす！　ここ！　ほら、ここに学校名が印刷されてまーす」"

    kosuke "「おおっ！　こここ、ここですか！　この白い布の、ちょっと膨らんだココですか！」"

    voice "audio/voice/op08/op08_0069.ogg"
    jordh "「じっくり見てくださーい！」"

    voice "audio/voice/op08/op08_0070.ogg"
    fauna "「イヤーッ！」"

    kosuke "「ホントだ！　確かにこんな危険なところに学校名が！！」"

    voice "audio/voice/op08/op08_0071.ogg"
    fauna "「見ないでくださーい！」"

    voice "audio/voice/op08/op08_0072.ogg"
    jordh 011 "「これは伝説の、学校指定女子用おぱんつでーす！！」"

    kosuke "「伝説の……おぱんつ！」"

    voice "audio/voice/op08/op08_0073.ogg"
    jordh "「そうでーす！　Ｇ大の購買部で年に５枚しか売られないという、伝説のレアアイテムでーす！」"

    kosuke "「うーん……うーん……これが伝説のおぱんつ……うーん……うーん……！」"

    voice "audio/voice/op08/op08_0074.ogg"
    fauna 008 "「そんな、じっくり見ないでください！！　あん、鼻息くすぐったいっ！」"

    voice "audio/voice/op08/op08_0075.ogg"
    jordh 000 "「目に焼き付けましたかー？」"

    kosuke "「はい！　しっかりくっきり！　今夜のおかずはもうバッチリっす！！」"

    voice "audio/voice/op08/op08_0076.ogg"
    fauna 005 "「もう、イヤー！！」"

    stop music

    scene black
    with Dissolve(1)

    scene bg07
    with Dissolve(1)

    play music "audio/bgm/bgm01.ogg"

    show fau 004 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op08/op08_0077.ogg"
    fauna "「…………」"

    kosuke "「あ、鼻血が」"

    voice "audio/voice/op08/op08_0078.ogg"
    fauna 003 "「……えっち」"

    voice "audio/voice/op08/op08_0079.ogg"
    jordh "「どうですかー？　彼女がＧ大生だとわかってくれまーしたかー？」"

    kosuke "「…………」"

    voice "audio/voice/op08/op08_0080.ogg"
    fauna "「もう、こんなので信用するわけないでしょ？　大体、伝説のおぱんつって一体何！？」"

    voice "audio/voice/op08/op08_0081.ogg"
    jordh 009 "「うーん、人間の男はこれで誤魔化せるはずなんだけど……」"

    voice "audio/voice/op08/op08_0082.ogg"
    fauna 002 "「そんなわけないでしょ！」"

    kosuke "「……〜〜〜〜！！」"

    voice "audio/voice/op08/op08_0083.ogg"
    fauna "「ほら、余計怪しんでるじゃない！」"

    voice "audio/voice/op08/op08_0084.ogg"
    jordh "「おっかしいなぁ……」"

    show fau 009 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op08/op08_0085.ogg"
    fauna "「あの……」"

    kosuke "「う〜〜〜〜〜っ」"

    voice "audio/voice/op08/op08_0086.ogg"
    fauna 008 "「え？」"

    kosuke "「やったー！！　美人の、しかも同じ大学の子が入居したー！！」"

    voice "audio/voice/op08/op08_0087.ogg"
    fauna 009 "「……え？」"

    kosuke "「いやー、大歓迎っすよホント！　つい感動を噛みしめちゃいました！」"

    voice "audio/voice/op08/op08_0088.ogg"
    fauna "「は、はあ……」"

    kosuke "「今まで俺と管理人のおばあちゃん２人だけだったから、もう寂しくて寂しくて！」"
    kosuke "「あ、俺、２階の３号室に住んでます！　留学じゃ何かと大変でしょう。困ったことがあったら何でも言って下さい。２４時間力になりますから！」"

    voice "audio/voice/op08/op08_0089.ogg"
    jordh 003 "「……信じたわ」"

    voice "audio/voice/op08/op08_0090.ogg"
    fauna 003 "「……やっぱりこの人……えっちだ……」"

    scene black
    with Dissolve(2)

    scene bg09
    with Dissolve(1)

    kosuke "「ささ、部屋にご案内しますよ。何号室ですか？　あ、荷物持ちましょうね、荷物。るるる〜ん♪」"

    show jor 000 at left
    show fau 012 at right
    with dissolve

    voice "audio/voice/op08/op08_0091.ogg"
    jordh "「……でも、いいヤツみたいだね」"

    voice "audio/voice/op08/op08_0092.ogg"
    fauna "「ふふっ。そうね」"

    kosuke "「さあ、早く早く」"

    voice "audio/voice/op08/op08_0093.ogg"
    fauna 000 "「あ、はい」"

    $ klotho_name = _("？？？")

    voice "audio/voice/op08/op08_0094.ogg"
    klotho "「ごめんくださーい」"

    kosuke "「あ、お客さんだ。ファウナ、悪いけど先に行ってて。俺、出るから」"

    voice "audio/voice/op08/op08_0095.ogg"
    fauna "「はい」"

    scene black
    with Dissolve(1)

    scene bg07
    with Dissolve(1)

    kosuke "「はーい、どちらさま……」"

    show kur 000 at center
    with dissolve

    kosuke "「（って、これまた美人！）」"

    voice "audio/voice/op08/op08_0096.ogg"
    klotho "「あら。あなたが川神幸介さんですね？」"

    kosuke "「え？　ええ、そうですけど……あなたは？」"

    show kur 000 at center
    with dissolve

    voice "audio/voice/op08/op08_0097.ogg"
    klotho "「申し遅れました。私、本日よりこの弁天荘の管理人を務めさせて頂く、黒崎なつきと申します。どうぞ宜しくお願いします」"

    kosuke "「え……管理人！？」"

    $ klotho_name = _("なつき")

    voice "audio/voice/op08/op08_0098.ogg"
    klotho 001 "「はい」"

    kosuke "「え、だって、じゃあ、今までいたキョウコばあちゃんは！？」"

    voice "audio/voice/op08/op08_0099.ogg"
    klotho 007 "「彼女は……クジで世界旅行が当たったとかで、今、旅の真っ最中です」"

    kosuke "「世界旅行！？」"

    voice "audio/voice/op08/op08_0100.ogg"
    klotho 000 "「そのような理由で、孫娘の私が代理で来たというわけです」"

    kosuke "「孫娘？」"

    voice "audio/voice/op08/op08_0101.ogg"
    klotho "「はい」"

    kosuke "「そういや確かに苗字が同じだ……」"
    kosuke "「でも、そんな話聞いてなかったけど……」"

    voice "audio/voice/op08/op08_0102.ogg"
    klotho 011 "「お疑いになられますか？」"

    kosuke "「いえ、そういうわけでは！」"
    kosuke "「（ちょっと怖い感じの人だな）」"
    kosuke "「（でも、美人だからいっか）」"

    voice "audio/voice/op08/op08_0103.ogg"
    klotho 000 "「管理人室はどちらです？」"

    kosuke "「あ、１階の奥の部屋です。案内します」"

    voice "audio/voice/op08/op08_0104.ogg"
    klotho 011 "「結構です。それより、荷物を運ぶの手伝って頂けないかしら」"

    kosuke "「荷物？」"

    voice "audio/voice/op08/op08_0105.ogg"
    klotho "「外に置きっぱなしになっていますので」"

    kosuke "「了解です。任せて下さい！」"

    voice "audio/voice/op08/op08_0106.ogg"
    klotho 000 "「割れ物も入っていますから、くれぐれも慎重に」"

    kosuke "「はいっ」"

    hide kur
    show fau 000 at center
    with dissolve

    voice "audio/voice/op08/op08_0107.ogg"
    fauna "「あのー幸介さん、ガスが出ないのですが……」"

    show fau 000 at left
    show kur 008 at right
    with dissolve

    voice "audio/voice/op08/op08_0108.ogg"
    klotho "「あっ！」"

    voice "audio/voice/op08/op08_0109.ogg"
    fauna "「……はい？　なんでしょう？」"

    voice "audio/voice/op08/op08_0110.ogg"
    klotho 000 "「あ、いえ、なんでもありません」"

    kosuke "「ああ、ファウナ。この人、新しい管理人さんだって」"

    voice "audio/voice/op08/op08_0111.ogg"
    fauna 012 "「そうでしたか。４号室のファウナです。宜しくお願い致します」"

    voice "audio/voice/op08/op08_0112.ogg"
    klotho 008 "「え？　住居人！？」"

    kosuke "「あれ？　知らなかったんですか？」"

    voice "audio/voice/op08/op08_0113.ogg"
    klotho 010 "「え、ええ。居住者はあなた一人だと……」"

    voice "audio/voice/op08/op08_0114.ogg"
    fauna 000 "「本日姉と共に引っ越して参りました」"

    voice "audio/voice/op08/op08_0115.ogg"
    klotho 009 "「そ、そうですか……」"

    scene bg07
    with dissolve

    show jor 000 at center
    with dissolve

    voice "audio/voice/op08/op08_0116.ogg"
    jordh "「ちょっと幸介ー、電気がさー……おっと、電気つかなーいでーす」"

    hide jor
    show kur 008 at center
    with dissolve

    voice "audio/voice/op08/op08_0117.ogg"
    klotho "「ひぃっ」"

    kosuke "「どうしたんです？」"

    voice "audio/voice/op08/op08_0118.ogg"
    klotho 009 "「い、いえ、なんでも……」"

    show fau 001 at left
    show kur 009 at right
    with dissolve

    voice "audio/voice/op08/op08_0119.ogg"
    fauna "「あ、ちょうどよかった。こちらが姉のヨルズです。姉さん、新しい管理人さんだって」"

    hide fau
    show jor 001 at left
    with dissolve

    voice "audio/voice/op08/op08_0120.ogg"
    jordh "「ああ、よろしくーでーす。シェイクハンド、シェイクハンド」"

    play sound "audio/sound/se075.ogg"

    show jor 008 at left
    show kur 008 at right
    # TODO: ^effect,Flash_$FFFFFFFF,500

    voice "audio/voice/op08/op08_0121.ogg"
    klotho "「きゃっ」"

    voice "audio/voice/op08/op08_0122.ogg"
    jordh "「うおっ、何だ！？」"

    "ヨルズが管理人さんの手に触れようとしたとき、突然強い静電気の様なものが二人の間で弾けた。"

    voice "audio/voice/op08/op08_0123.ogg"
    jordh 000 "「Ｏｈ！　エレクトリカルマジカルパレード！」"

    voice "audio/voice/op08/op08_0124.ogg"
    klotho 011 "「…………」"

    voice "audio/voice/op08/op08_0125.ogg"
    jordh 001 "「きっとミーとユーは電撃的な出会いなのでーす。これから一緒にラブラブな人生を歩むのでーす」"

    voice "audio/voice/op08/op08_0126.ogg"
    klotho "「お断りします」"

    voice "audio/voice/op08/op08_0127.ogg"
    jordh 009 "「Ｏｈ！　フラれてしまいまーした」"

    voice "audio/voice/op08/op08_0128.ogg"
    klotho 000 "「そんことより、川神さん、荷物の方お願いしますね」"

    voice "audio/voice/op08/op08_0129.ogg"
    jordh "「さらーっと流されてしまいまーした……」"

    kosuke "「あ、はい！」"

    hide jor
    show fau 000 at left
    with dissolve

    voice "audio/voice/op08/op08_0130.ogg"
    fauna "「あ、わたしも手伝います」"

    voice "audio/voice/op08/op08_0131.ogg"
    klotho "「あ、いいえ、重いものですから女性には無理です。結構です」"

    voice "audio/voice/op08/op08_0132.ogg"
    fauna 001 "「いえ、でも、このくらいでしたら法術で……」"

    scene bg07
    show jor 011 at center
    with dissolve

    voice "audio/voice/op08/op08_0133.ogg"
    jordh "「ファウナ！」"

    hide jor
    show fau 008 at left
    show kur 000 at right
    with dissolve

    voice "audio/voice/op08/op08_0134.ogg"
    fauna "「あっ……」"

    voice "audio/voice/op08/op08_0135.ogg"
    fauna 000 "「ほ……法事の時に良く運んでましたけど……あは、いえ、やっぱりお言葉に甘えて遠慮しておきます」"

    voice "audio/voice/op08/op08_0136.ogg"
    klotho 001 "「ええ、それがいいわ。おほほほほほ……」"

    voice "audio/voice/op08/op08_0137.ogg"
    fauna 001 "「おほほほほほ……」"

    scene bg07
    show jor 009 at center
    with dissolve

    voice "audio/voice/op08/op08_0138.ogg"
    jordh "「まったく……」"

    kosuke "「？？？」"

    stop music

    scene black
    with Dissolve(2)

    jump op09
