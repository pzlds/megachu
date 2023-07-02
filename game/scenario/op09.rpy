label op09:
    $ save_name = _("オープニング")

    scene bg01
    with Dissolve(2)

    play music "audio/bgm/bgm02.ogg"

    "あれから３時間経った。"
    "結局、管理人さんに続いてファウナ達の引っ越しまで手伝わされてしまった。"

    kosuke "「明日筋肉痛かな……」"

    "畳に座り、少し張った感じのある腕を揉みほぐす。"
    "ファウナはまだ良かったけど、あのお姉さんの方が大変だった。"
    "こんな狭い部屋にどうやって入れるの？　ってくらいの荷物の量だった。"
    "段ボール箱を天井まで積み上げて、なんとか全部入ったけど……。"
    "あの荷物は何だったんだろう。訊いても教えてくれなかった。"

    play sound "audio/sound/se038.ogg"

    "（ぐぅ）"

    kosuke "「腹減ったなぁ。カップラーメンでも食うか」"
    kosuke "「…………」"
    kosuke "「体が疲れてて、お湯沸かすのもだるいー」"

    "テーブル代わりのこたつの上にあるチョコを１つ掴み、口に放り込む。"

    kosuke "「もう少し休んでから飯にしよう……」"

    "ぐぐーっと背伸びをし、そのまま床に倒れ込んだ。"

    kosuke "「それにしても凄いことになったよなぁ」"
    kosuke "「美人姉妹と美人管理人……」"
    kosuke "「あんな綺麗な人たちと、これから同じ屋根の下で暮らしていくんだ……」"

    stop music

    kosuke "「なんか急にツキ出してない？　俺」"

    # TODO: ^bg0,BG01,overlap,1000,,"\color,$CCFF8AFF,2\blur,10,10"
    show bg01
    with Dissolve(1)

    play music "audio/bgm/bgm09.ogg"

    kosuke "「困ったときはいつでも俺を頼りにしてくれ。フッ」"

    voice "audio/voice/op09/op09_0000.ogg"
    fauna "「まぁ、なんて男らしい……」"

    voice "audio/voice/op09/op09_0001.ogg"
    jordh "「私、一生あなたについて行きまーすっ」"

    voice "audio/voice/op09/op09_0002.ogg"
    klotho "「あなたになら、私の全てをあげても良いわ……」"

    kosuke "「フッ、仕方ねぇなぁ。全員まとめて面倒みてやるぜ！」"

    show bg01
    with Dissolve(1)

    stop music

    kosuke "「なーんてなぁ」"
    kosuke "「ああ、誰かひとりくらい、俺と萌え萌えヌルヌルアハ\nハ〜ンな関係になったりしないかなぁ〜！」"

    play sound "audio/sound/se000.ogg"

    kosuke "「あ、はい！」"

    voice "audio/voice/op09/op09_0003.ogg"
    fauna "「ファウナです」"

    kosuke "「（うわっ、妄想した途端に彼女の方からやってき\nた！？）」"
    kosuke "「ちょ、ちょっと待って」"

    stop music

    show black
    with Dissolve(2)

    play sound "audio/sound/se003.ogg"

    play music "audio/bgm/bgm15.ogg"

    # TODO: ^bg0,BG08,overlap,
    scene bg08
    with dissolve

    show fau 000 at center
    with dissolve

    voice "audio/voice/op09/op09_0004.ogg"
    fauna "「こんにちは」"

    kosuke "「こ、こんにちは」"

    "なんだかドキドキする。本当に綺麗な子だな。"

    show fau 000 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0005.ogg"
    jordh "「私もいるよー」"

    kosuke "「あ、どうも」"

    voice "audio/voice/op09/op09_0006.ogg"
    jordh "「ねえねえ、幸介。私、さっきと何か違わない？」"

    kosuke "「え？　さっきと……？」"

    "頭の先から爪先まで、ゆっくりと視線を動かした。"
    "うーん？　何が違うんだろう。服はさっきと同じだし……胸の大きさが変わるわけないし……。"
    "それにしても良いプロポーションだな。モデルさんみたいだ。"

    voice "audio/voice/op09/op09_0007.ogg"
    jordh 003 "「ねえねえ、幸介。私、さっきと何か違わない？」"

    kosuke "「え？　そ、その、さっきと大きさ違うかもなーっなん\nて……」"

    voice "audio/voice/op09/op09_0008.ogg"
    jordh 013 "「あら、残念だけど変わってないわよ？　触ってみる？」"

    kosuke "「え？　いいの！？」"

    voice "audio/voice/op09/op09_0009.ogg"
    fauna 008 "「ね、姉さん！」"

    voice "audio/voice/op09/op09_0010.ogg"
    jordh 000 "「冗談よ。そんなことしたら銀河の中心までぶっ飛ばすからね」"

    show fau 000 at right
    with dissolve

    kosuke "「は、はあ……」"

    voice "audio/voice/op09/op09_0011.ogg"
    jordh "「で、お答えは？」"

    kosuke "「うーん……妊娠したとか？」"

    voice "audio/voice/op09/op09_0012.ogg"
    jordh 012 "「そんなワケないでしょ。もう、バカね」"

    # TODO: ^se0,se027,255,0,0
    play sound "audio/sound/se027.ogg"

    "ピンッとヨルズが俺のおでこを指で弾いた。"

    kosuke "「ごめん。全然わからないや。正解は何？」"

    voice "audio/voice/op09/op09_0013.ogg"
    jordh 001 "「じゃーん、言葉が流暢になりました〜」"

    kosuke "「おおっ、そう言えば確かに！」"

    voice "audio/voice/op09/op09_0014.ogg"
    jordh "「幸介さんといっぱいお話がしたくってぇ、ヨルズ、必死にこの国の言葉を練習しちゃったのぉ〜。すりすり」"

    kosuke "「お、俺と！？」"

    voice "audio/voice/op09/op09_0015.ogg"
    fauna 010 "「（あの喋り方が面倒くさくなったのね……）」"

    kosuke "「え？」"

    voice "audio/voice/op09/op09_0016.ogg"
    fauna 001 "「あ、いえ、なんでも……ほほほ」"

    kosuke "「でも、たった３時間で……？　それはいくらなんでも有り得な……」"

    hide fau

    show jor 016 at center
    with dissolve

    "突然ヨルズの手が俺の頬に伸び、そっと撫で始める。"

    kosuke "「あ、あう？」"

    "とってもくすぐったくて、股間がピクンと反応した。"

    voice "audio/voice/op09/op09_0017.ogg"
    jordh "「ねえ、私の言ったこと、信じてくれるわよね〜？」"

    # TODO: ^se0,se040,255,0,0
    play sound "audio/sound/se040.ogg"

    "（ぷにょん）"

    kosuke "「む、胸が当たってますよ？」"

    voice "audio/voice/op09/op09_0018.ogg"
    jordh "「バカね」"

    voice "audio/voice/op09/op09_0019.ogg"
    jordh "「わざと当ててるの」"

    kosuke "「ふおーっ！？」"

    voice "audio/voice/op09/op09_0020.ogg"
    jordh 003 "「ね？　信じる？」"

    kosuke "「ももも、もちろん！」"

    voice "audio/voice/op09/op09_0021.ogg"
    jordh 016 "「幸介って、いい子ねぇ。なでなで。ちゅっ」"

    kosuke "「でへ〜〜〜〜」"

    hide jor
    show fau 002 at center
    with dissolve

    voice "audio/voice/op09/op09_0022.ogg"
    fauna "「むぅ〜〜っ」"

    voice "audio/voice/op09/op09_0023.ogg"
    fauna "「（やっぱりえっちだ、この人っ）」"

    voice "audio/voice/op09/op09_0024.ogg"
    fauna 011 "「んっんんっ！　お取り込み中失礼します」"

    voice "audio/voice/op09/op09_0025.ogg"
    fauna "「幸介さん、あの、今ってお暇ですか？」"

    kosuke "「あ、うん、とっても〜」"

    voice "audio/voice/op09/op09_0026.ogg"
    fauna 000 "「幸介さんのお部屋に、少しお邪魔しても良いですか？」"

    kosuke "「いいよ、いいよ。ゆっくりしていって〜」"

    show fau 011 at right
    show jor 016 at left
    with dissolve

    voice "audio/voice/op09/op09_0027.ogg"
    jordh "「な〜でな〜で」"

    kosuke "「えへへ〜〜」"

    voice "audio/voice/op09/op09_0028.ogg"
    fauna 002 "「って、いつまでそうしてるの、姉さんは！」"

    voice "audio/voice/op09/op09_0029.ogg"
    jordh 001 "「やーん、ファウナちゃんコワーイ。ね〜え？　なでな\nで〜」"

    kosuke "「ほわーん。ここは天国〜」"

    voice "audio/voice/op09/op09_0030.ogg"
    fauna "「幸介さん！　もう、離れてください！」"

    kosuke "「え、あ、うんっ」"

    "あまりにも気持ち良くて、つい、違う世界にイッちゃってた。"

    show fau 002 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0031.ogg"
    jordh "「じゃ、お邪魔するわね」"

    kosuke "「どうぞ」"

    voice "audio/voice/op09/op09_0032.ogg"
    fauna 000 "「おじゃましまーす」"

    stop music

    scene black
    with Dissolve(2)

    play sound "audio/sound/se004.ogg"

    scene bg01
    show fau 000 at right
    show jor 000 at left
    with Dissolve(2)

    play music "audio/bgm/bgm15.ogg"

    voice "audio/voice/op09/op09_0033.ogg"
    jordh "「ふーん、これが幸介の部屋かぁ」"

    "俺の部屋に女の子のいい匂いが広がった。"
    "そういやこの部屋、女の人が遊びに来たことって今まで一度もないんだよなぁ……。前管理人のキョウコばあちゃん以外は。"
    "なんか、ドキドキしてきたぞ。"

    voice "audio/voice/op09/op09_0034.ogg"
    fauna 011 "「姉さん、人の部屋をそんなにジロジロ見たら失礼よ」"

    voice "audio/voice/op09/op09_0035.ogg"
    jordh "「いいじゃない。アンタだって男の部屋に入るの初めてでしょ。せっかくだから、もっと良く観察しなさい」"

    voice "audio/voice/op09/op09_0036.ogg"
    fauna 010 "「え、でも……」"

    voice "audio/voice/op09/op09_0037.ogg"
    jordh 001 "「うわ、ねぇこれフィギュアって言うんでしょ？　すっごい、初めて見た。いっぱい持ってるわね〜」"

    kosuke "「まぁ、いつの間にやら増えちゃってねぇ」"

    voice "audio/voice/op09/op09_0038.ogg"
    jordh "「お、ファウナ見て見て。ほら、この天使のフィギュア、白い水着がスケスケ」"

    voice "audio/voice/op09/op09_0039.ogg"
    fauna 008 "「きゃっ！」"

    kosuke "「ああ、それは限定カラーバージョンで、販売からたったの数時間で売り切れ……」"

    voice "audio/voice/op09/op09_0040.ogg"
    fauna 003 "「……えっち」"

    kosuke "「うがっ」"

    voice "audio/voice/op09/op09_0041.ogg"
    jordh "「おっ、こっちは戦艦のプラモデル！　かぁっこいい〜！」"

    voice "audio/voice/op09/op09_0042.ogg"
    jordh "「ほらほら、戦艦戦艦」"

    # TODO: ^se0,se075,255,0,0
    play sound "audio/sound/se075.ogg"

    "（バキッ）"

    show fau 008 at right
    show jor 007 at left
    with dissolve

    voice "audio/voice/op09/op09_0043.ogg"
    jordh "「あっ、底の固まりが取れちゃった……」"

    voice "audio/voice/op09/op09_0044.ogg"
    fauna "「姉さんったらっ！」"

    voice "audio/voice/op09/op09_0045.ogg"
    fauna 009 "「ごめんなさい、幸介さん。姉さんがとんでもないこと\nを……」"

    voice "audio/voice/op09/op09_0046.ogg"
    jordh 009 "「ごめーん」"

    kosuke "「いいっていいって。すぐ取れるんだよ、第三艦橋」"
    kosuke "「それよりさ、立ってないで座って」"

    "こんなこともあろうかと……女の子が部屋に来る日を想定して買っておいた、真新しい座布団を２つ敷いた。"

    show fau 000 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0047.ogg"
    fauna "「ありがとうございます」"

    voice "audio/voice/op09/op09_0048.ogg"
    jordh "「気が利くじゃない。あ、そうだ。これ、食料の差し入れ」"

    kosuke "「え？　マジ？」"

    voice "audio/voice/op09/op09_0049.ogg"
    jordh "「５０万円ね」"

    kosuke "「ナヌ！？」"

    voice "audio/voice/op09/op09_0050.ogg"
    jordh "「うそうそ。もちろんタダよ」"

    kosuke "「ありがとう！」"

    voice "audio/voice/op09/op09_0051.ogg"
    jordh 013 "「でも、タダ程怖いものはないのよね……」"

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0052.ogg"
    fauna 010 "「冗談ですよ。もう、姉さんったら」"

    voice "audio/voice/op09/op09_0053.ogg"
    jordh 001 "「あはは。悪い悪い」"

    show fau 000 at right
    with dissolve

    kosuke "「あはは……」"
    kosuke "「（わーい、女の子から生まれて初めて差し入れ貰った\nぞぉ〜！）」"
    kosuke "「って、餅！？」"

    voice "audio/voice/op09/op09_0054.ogg"
    jordh 000 "「そうよ。で、はい」"

    show fau 007 at right
    with dissolve

    kosuke "「……？　はいって……その手は何？」"

    voice "audio/voice/op09/op09_0055.ogg"
    jordh 001 "「ギブミー善意」"

    kosuke "「は？」"

    voice "audio/voice/op09/op09_0056.ogg"
    jordh "「あなたの善意を募金プリーズ」"

    kosuke "「募金って……金取んのかよ！」"

    voice "audio/voice/op09/op09_0057.ogg"
    jordh 003 "「当然でしょ？　わざわざ買ってきてやったんだから」"

    kosuke "「タダって言ったじゃん！」"

    voice "audio/voice/op09/op09_0058.ogg"
    jordh "「送料、手数料は別となっております」"

    kosuke "「悪徳商法だなぁ……」"

    voice "audio/voice/op09/op09_0059.ogg"
    jordh 013 "「ねぇ、ちょうだーい？　あなたと私の仲じゃない。\nねぇ〜？」"

    "ヨルズがうっとりした目を俺に近づけ、つーっと、俺の顔の輪郭を人指し指でなぞった。"

    kosuke "「あ、あうう」"

    voice "audio/voice/op09/op09_0060.ogg"
    jordh "「なんだったら、またファウナのパンツ見せてあげるか\nらぁ」"

    kosuke "「マジ！？」"

    voice "audio/voice/op09/op09_0061.ogg"
    fauna 002 "「イ・ヤ・で・す！」"

    voice "audio/voice/op09/op09_0062.ogg"
    jordh "「じゃあ、私と、イ・イ・コ・トしちゃう？」"

    kosuke "「うへっ！？」"

    voice "audio/voice/op09/op09_0063.ogg"
    jordh "「私、幸介みたいな男の子、好みかも」"

    kosuke "「ままま、マジっすか！？」"

    voice "audio/voice/op09/op09_0064.ogg"
    fauna 013 "「姉さん！」"

    voice "audio/voice/op09/op09_0065.ogg"
    jordh 001 "「あはは。冗談よ。冗談」"

    kosuke "「（冗談かよ……ちぇっ）」"

    voice "audio/voice/op09/op09_0066.ogg"
    fauna 002 "「むぅ〜〜っ」"

    voice "audio/voice/op09/op09_0067.ogg"
    jordh 012 "「ファウナちゃん、そんなおっかない顔しちゃだめよ？　嫉妬してるみたい」"

    voice "audio/voice/op09/op09_0068.ogg"
    fauna 009 "「嫉っ……そ、そんなことは無いわ！？　なんでわたしが、そ、そんな感情……！」"

    voice "audio/voice/op09/op09_0069.ogg"
    jordh "「クックック……」"

    voice "audio/voice/op09/op09_0070.ogg"
    fauna "「もう、何がおかしいのよ！」"

    voice "audio/voice/op09/op09_0071.ogg"
    jordh 000 "「なーんでもない。ほら、それより、アンタ麦茶持ってきたんでしょ？　注いで注いで」"

    voice "audio/voice/op09/op09_0072.ogg"
    fauna "「……もうっ」"

    hide fau

    "多少不機嫌そうにファウナは立ち、袋から麦茶が入ってるらしい水筒とコップを取り出した。"

    show fau 000 at right
    with dissolve

    "ちなみに、この部屋には俺用の１セットの食器しかない。"

    # TODO: ^se0,se018,255,0,0
    play sound "audio/sound/se018.ogg"

    "（とぽとぽとぽ）"

    voice "audio/voice/op09/op09_0073.ogg"
    fauna 002 "「はい、姉さん」"

    voice "audio/voice/op09/op09_0074.ogg"
    jordh "「あんがと」"

    voice "audio/voice/op09/op09_0075.ogg"
    fauna 009 "「……！」"

    "（そお〜っ）"

    voice "audio/voice/op09/op09_0076.ogg"
    fauna "「ど、どうぞ」"

    kosuke "「あ、ありがとう」"

    "ヨルズが変なことを言うから、お互い意識してしまう。"

    voice "audio/voice/op09/op09_0077.ogg"
    jordh 007 "「あら？　私とは随分態度か違うわね。やっぱりあな\nた……」"

    voice "audio/voice/op09/op09_0078.ogg"
    fauna "「ち、違うって言ってるでしょ！」"

    voice "audio/voice/op09/op09_0079.ogg"
    jordh 003 "「焦るのが怪しい」"

    voice "audio/voice/op09/op09_0080.ogg"
    fauna 010 "「んも〜っ！」"

    voice "audio/voice/op09/op09_0081.ogg"
    fauna "「姉さん。今日からごはん、自分で作って食べてね？」"

    voice "audio/voice/op09/op09_0082.ogg"
    jordh 007 "「へ？」"

    voice "audio/voice/op09/op09_0083.ogg"
    fauna "「わたし、もう作らないから」"

    voice "audio/voice/op09/op09_0084.ogg"
    jordh 009 "「わ、ファウナ、機嫌直して？　私が悪かったから。ね？　ね？　ね？」"

    voice "audio/voice/op09/op09_0085.ogg"
    fauna "「知りませんっ」"

    kosuke "「（ファウナが料理担当なのか）」"

    voice "audio/voice/op09/op09_0086.ogg"
    jordh 004 "「ファウナちゃ〜ん……」"

    "ぷくっとファウナの頬が膨れた。"

    stop music

    scene white
    with Dissolve(1)

    play sound "audio/sound/se050.ogg"

    play music "audio/bgm/bgm02.ogg"

    scene bg02
    with ImageDissolve("images/wipe/16.png", 1.5)

    show jor 003 at center
    with dissolve

    voice "audio/voice/op09/op09_0087.ogg"
    jordh "「しっかし、この部屋も暑いわね。汗出てくるわ」"

    kosuke "「このアパート、昼も夜も全体的に暑いんだよ。それに、冷房設備なんてものはどの部屋にも無いし」"

    voice "audio/voice/op09/op09_0088.ogg"
    jordh "「管理人の部屋も？」"

    kosuke "「昨日までいたキョウコばーちゃんはクーラーが大嫌いだったからね。『夏は暑くて当たり前』、なんて良く言ってたよ」"
    kosuke "「あ、そうだ。扇風機なら一階の居間にあるよ。行ってみたら？」"

    voice "audio/voice/op09/op09_0089.ogg"
    jordh 009 "「移動するまでが暑い。持って来てー」"

    kosuke "「あれ移動禁止なんだよ。運んだら罰金取られるよ」"

    voice "audio/voice/op09/op09_0090.ogg"
    jordh "「ぐっ……。アンタ、扇風機くらい買いなさいよね」"

    kosuke "「そんな金あったらエロゲー買うって」"

    voice "audio/voice/op09/op09_0091.ogg"
    jordh 007 "「エロ……え……何？」"

    kosuke "「あ、いや、なんでもないなんでもない。あはははは\nは……」"

    play sound "audio/sound/se050.ogg"

    voice "audio/voice/op09/op09_0092.ogg"
    jordh 009 "「あーもぉ、暑いなぁ。シャワーでも浴びようかしら」"

    voice "audio/voice/op09/op09_0093.ogg"
    jordh "「ね？　風呂はいつでも入れるんでしょ？」"

    kosuke "「うん。風呂もトイレも１階の台所も共同だから、勝手に使っていい……おっ？」"

    "ヨルズが服の胸元を掴み、パタパタと扇いでいる。"
    "服の動きに合わせ、胸の谷間の形が変化した。"

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0094.ogg"
    jordh 013 "「ん？　なに？　私の胸の谷間、気になる？」"

    kosuke "「あぐっ……。い、いや、そういうわけでは！」"

    voice "audio/voice/op09/op09_0095.ogg"
    jordh 001 "「フフッ。遠慮しなくて良いのに。ほらほら、谷間谷間ー」"

    kosuke "「わわっ、見せなくていいから！」"

    voice "audio/voice/op09/op09_0096.ogg"
    jordh "「あははっ。幸介は面白いなー」"

    kosuke "「からかうなっての！」"

    show fau 003 at right
    show jor 001 at left
    with dissolve

    stop music

    voice "audio/voice/op09/op09_0097.ogg"
    fauna "「……えっち」"

    kosuke "「あう」"

    show fau 011 at right
    with dissolve

    play music "audio/bgm/bgm01.ogg"

    voice "audio/voice/op09/op09_0098.ogg"
    fauna "「コホン。ところで幸介さん」"

    kosuke "「はい？」"

    voice "audio/voice/op09/op09_0099.ogg"
    fauna "「少し、質問しても宜しいでしょうか？」"

    kosuke "「いいけど……。何？　改まって」"

    show jor 011 at left
    with dissolve

    "ファウナとヨルズが小さく頷き合った。"

    voice "audio/voice/op09/op09_0100.ogg"
    fauna "「幸介さんって独り暮らしですよね？」"

    kosuke "「うん」"

    voice "audio/voice/op09/op09_0101.ogg"
    fauna "「もうずっとここに住んでるんですか？」"

    kosuke "「いや、春にここに引っ越してきたばかり。春に大学に受かって、それから」"

    voice "audio/voice/op09/op09_0102.ogg"
    fauna "「その間、このアパートには幸介さんと管理人さんだけって言ってましたよね」"

    kosuke "「うん。完全に二人だけ」"

    voice "audio/voice/op09/op09_0103.ogg"
    fauna 002 "「（やっぱり、彼らはまだ……）」"

    voice "audio/voice/op09/op09_0104.ogg"
    jordh "「（みたいね）」"

    kosuke "「それが何か？」"

    show fau 000 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0105.ogg"
    fauna "「え？　あ、いえ、こんな安いアパートなのに、なんで人がいないのかなぁって」"

    kosuke "「うーん、管理人さんが気に入った人じゃないと入居させないとかいう話は不動産屋から聞いたけど」"

    voice "audio/voice/op09/op09_0106.ogg"
    fauna "「そうなんですか」"

    kosuke "「お化けでも出るかと思った？」"

    voice "audio/voice/op09/op09_0107.ogg"
    fauna 007 "「い、いえ、そんなことは……」"

    voice "audio/voice/op09/op09_0108.ogg"
    jordh 007 "「幸介、アンタはどこが気に入られたの？」"

    kosuke "「う……。不運そうな顔が死んだ夫にそっくりだって」"

    voice "audio/voice/op09/op09_0109.ogg"
    jordh 012 "「クックックッ」"

    voice "audio/voice/op09/op09_0110.ogg"
    fauna 000 "「わ、笑っちゃ失礼よ」"

    voice "audio/voice/op09/op09_0111.ogg"
    jordh "「悪い悪い。でも、不運そうな顔ってのは当たってるわ」"

    voice "audio/voice/op09/op09_0112.ogg"
    fauna "「もう。ごめんなさいね、幸介さん」"

    kosuke "「いや。でも確かに俺って不運な場面が多いんだよなぁ。昨日はゲーム買えなかったし。なんでだろう」"

    voice "audio/voice/op09/op09_0113.ogg"
    jordh 000 "「それはね……」"

    hide jor
    show fau 012 at center
    with dissolve

    voice "audio/voice/op09/op09_0114.ogg"
    fauna "「大丈夫」"

    "（にぎっ）"

    kosuke "「へっ？」"

    "何か言おうとしたヨルズを遮り、ファウナが優しく俺の手を握った。"

    voice "audio/voice/op09/op09_0115.ogg"
    fauna "「あなたはこれからきっと、不運だった分も幸運に恵まれますよ。だから、大丈夫です」"

    kosuke "「（温かくて柔らかい手だな……）」"

    voice "audio/voice/op09/op09_0116.ogg"
    fauna "「わたしたちがきっとお護りしますから。幸介さんは、何も心配せずにいてください」"

    kosuke "「う、うん……？」"
    kosuke "「（……護るってなんだろう。まぁいいや。女の子に手を握ってもらえてるし……）」"
    kosuke "「（あ、でも……。この手の温もり、前にもどこか\nで……）」"

    show fau 012 at right
    show jor 011 at left
    with dissolve

    voice "audio/voice/op09/op09_0117.ogg"
    jordh "「…………」"

    voice "audio/voice/op09/op09_0118.ogg"
    jordh "「（でも、なにも住人として近づくとは限らない……）」"

    voice "audio/voice/op09/op09_0119.ogg"
    jordh "「ねえ幸介、ちょっと押し入れの中、見させてね」"

    kosuke "「うん……」"
    kosuke "「って、ああ！　そこは開けちゃダメ……！」"

    play sound "audio/sound/se008.ogg"

    voice "audio/voice/op09/op09_0120.ogg"
    jordh 008 "「ダメって……。ぶわっ！　なんか出てきた！」"

    voice "audio/voice/op09/op09_0121.ogg"
    fauna 008 "「きゃっ！」」"

    play sound "audio/sound/se098.ogg"

    "大量に押し入れに入れておいた『あるモノ』が雪崩を起こし、押し入れの前にいた彼女たちを襲った。"

    voice "audio/voice/op09/op09_0122.ogg"
    jordh "「うわ、なによこれ……」"

    voice "audio/voice/op09/op09_0123.ogg"
    fauna 007 "「女の子の絵が描かれた……枕？」"

    kosuke "「その……抱き枕」"

    voice "audio/voice/op09/op09_0124.ogg"
    fauna 007 "「抱き枕？」"

    kosuke "「いやその、ゲームの予約特典とか即売会とかで、貰ったり買ったりデスネ……」"

    voice "audio/voice/op09/op09_0125.ogg"
    fauna "「これを……抱いて寝るんですか？」"

    kosuke "「う、……うん」"

    show fau 003 at right
    show jor 003 at left
    with dissolve

    voice "audio/voice/op09/op09_0126.ogg"
    jordh "「…………」"

    voice "audio/voice/op09/op09_0127.ogg"
    fauna "「…………」"

    voice "audio/voice/op09/op09_0128.ogg"
    jordh "「マジ？」"

    kosuke "「い、一応マジ」"

    voice "audio/voice/op09/op09_0129.ogg"
    jordh "「アンタ……」"

    voice "audio/voice/op09/op09_0130.ogg"
    fauna "「…………」"

    "あう。哀れむような視線が辛い。"

    voice "audio/voice/op09/op09_0131.ogg"
    jordh "「でも、折角だから寝てみる？」"

    voice "audio/voice/op09/op09_0132.ogg"
    fauna "「そ、そうね」"

    kosuke "「マジ！？」"

    scene bg02
    with dissolve

    voice "audio/voice/op09/op09_0133.ogg"
    jordh "「…………」"

    voice "audio/voice/op09/op09_0134.ogg"
    fauna "「…………」"

    show fau 000 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0135.ogg"
    jordh "「セーフ。いい感じ」"

    voice "audio/voice/op09/op09_0136.ogg"
    fauna "「そうね。いい感じ」"

    kosuke "「マジ？」"

    voice "audio/voice/op09/op09_0137.ogg"
    jordh "「良かったわね。変態判定は付かなかったわ」"

    voice "audio/voice/op09/op09_0138.ogg"
    fauna "「なんだか、新しい世界が開けた気分です」"

    kosuke "「そ、それはよかった」"

    voice "audio/voice/op09/op09_0139.ogg"
    jordh 003 "「でも、このシマシマはアウト」"

    kosuke "「へ？」"

    "ヨルズが、押し入れから落ちた俺のパンツを見つけた。"

    voice "audio/voice/op09/op09_0140.ogg"
    fauna 007 "「お、男物の……パンツ？」"

    voice "audio/voice/op09/op09_0141.ogg"
    jordh 009 "「うっ……ちょっと、これ、ちゃんと洗濯してんの？　匂うわよ？」"

    kosuke "「いやー、今度やろう今度やろうと思ってるうちに……\nねぇ」"

    voice "audio/voice/op09/op09_0142.ogg"
    jordh 013 "「うわ、押し入れの中にいっぱいある！　ファウナ、\nそらっ！」"

    stop music

    "ヨルズが、大量のパンツをファウナに向かって放った。"

    play music "audio/bgm/bgm19.ogg"

    voice "audio/voice/op09/op09_0143.ogg"
    fauna 008 "「きゃあっ！！」"

    "俺のパンツにまみれるファウナ。"

    voice "audio/voice/op09/op09_0144.ogg"
    fauna 009 "「あ、あぅっ……」"

    "あまりの出来事に、言葉を失っている。"

    kosuke "「ファ、ファウナ大丈夫？」"

    voice "audio/voice/op09/op09_0145.ogg"
    fauna 005 "「ううっ、わたし、男の人の使用済みパンツまみれに……くすん」"

    kosuke "「ご、ごめん」"

    hide jor
    with dissolve

    play music "audio/bgm/bgm01.ogg"

    voice "audio/voice/op09/op09_0146.ogg"
    fauna 002 "「幸介さん！」"

    kosuke "「はい！」"

    voice "audio/voice/op09/op09_0147.ogg"
    fauna "「わたし、全部お洗濯しますから、洗い物をまとめておいてください！」"

    kosuke "「え、そんな、悪いよ」"

    voice "audio/voice/op09/op09_0148.ogg"
    fauna "「こんなに溜めておいたら非衛生的です！　病気になります！　きのこ生えます！　アパート中！　壁を伝って！」"

    kosuke "「は、はあ……」"

    voice "audio/voice/op09/op09_0149.ogg"
    fauna "「わたし、全部完ッ璧に洗ってみせますから！」"

    show fau 011 at right
    show jor 000 at left
    with dissolve

    voice "audio/voice/op09/op09_0150.ogg"
    jordh "「ファウナって洗濯大好きっ子だから、やらせてあげて」"

    kosuke "「そ、そうなんだ。じゃあ、お願いするよ」"

    voice "audio/voice/op09/op09_0151.ogg"
    fauna 002 "「任せてくださいっ！」"

    kosuke "「（うーん、女の子が俺のパンツを洗ってくれるのか……。か、感動だ！）」"
    kosuke "「よーし、じゃあ、代わりに俺が、ファウナのパンツを洗ってあげるよ！」"

    stop music

    hide jor
    show fau 003 at center
    with dissolve

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0153.ogg"
    fauna "「えっち」"

    kosuke "「ごめんなさい」"

    play music "audio/bgm/bgm01.ogg"

    show jor 001 at left
    show fau 003 at right
    with dissolve

    voice "audio/voice/op09/op09_0154.ogg"
    jordh "「ねえねえ幸介」"

    kosuke "「え？」"

    voice "audio/voice/op09/op09_0155.ogg"
    jordh "「押し入れの下の段ボールに、なんか箱がいっぱい詰まってるよ？」"

    voice "audio/voice/op09/op09_0156.ogg"
    fauna 007 "「……？」"

    kosuke "「わあ！　それも出しちゃダメ！！」"

    voice "audio/voice/op09/op09_0157.ogg"
    jordh 003 "「えーなになに？　『調教天使ヌキエール』？」"

    voice "audio/voice/op09/op09_0158.ogg"
    fauna 001 "「まぁ、可愛い絵」"

    kosuke "「あぅ……」"

    show jor 000 at center
    hide fau
    with dissolve

    voice "audio/voice/op09/op09_0159.ogg"
    jordh "「ん……？？　なにこれ。天使がどうしたって？」"

    kosuke "「ええっと、それはですねえ……つまり、１８歳未満はお断りのパソコンゲームでして……」"

    voice "audio/voice/op09/op09_0160.ogg"
    jordh "「ああ、パソコンのゲームか。ちょっと動かしてみるかね」"

    kosuke "「え？　いや、動かさなくていいから！」"

    voice "audio/voice/op09/op09_0161.ogg"
    jordh "「いいじゃないの堅い事言わないの」"

    kosuke "「で、でも……」"

    voice "audio/voice/op09/op09_0162.ogg"
    jordh 001 "「私、ゲームには煩いわよ？　シューティングゲームの大会で優勝したこともあるんだから」"

    kosuke "「いや、それはその、そういうゲームとはちょっとというか、かなり違うものでありまして……」"

    voice "audio/voice/op09/op09_0163.ogg"
    jordh 000 "「ＣＤ認識。ダブルクリックで起動っと」"

    kosuke "「聞いちゃいねえ！」"

    # TODO: ^music,bgm19,255,0
    play music "audio/bgm/bgm19.ogg"

    voice "audio/voice/op09/op09_0164.ogg"
    "ゲーム" "『やーん、お兄ちゃんのえっち』"

    voice "audio/voice/op09/op09_0165.ogg"
    jordh 008 "「うわ、すっごい。なにこれ？　女の子が服脱いでるよ？　へんなゲーム！」"

    kosuke "「い、いやその……」"

    voice "audio/voice/op09/op09_0166.ogg"
    "ゲーム" "『いきなりそんなとこ入れちゃだめえ！』"

    voice "audio/voice/op09/op09_0167.ogg"
    jordh 013 "「んー？　そんなとこってどこなのかなぁ……？　ここか？　ここがええんか？」"

    kosuke "「って、順応するなよ！」"

    voice "audio/voice/op09/op09_0168.ogg"
    "ゲーム" "『はぁ……はぁ……凄いの！　お兄ちゃん凄いのぉ！　わたし頭おかしくなっちゃう！』"

    voice "audio/voice/op09/op09_0169.ogg"
    jordh 001 "「うおー、エロー！　エロエロよー！　こんなゲームも世の中にあるのかー！」"

    kosuke "「…………」"

    show fau 003 at right
    show jor 001 at left
    with dissolve

    voice "audio/voice/op09/op09_0170.ogg"
    fauna "「…………！！」"

    kosuke "「わっ！」"

    voice "audio/voice/op09/op09_0171.ogg"
    fauna "「えっちです！」"

    kosuke "「あう……」"

    voice "audio/voice/op09/op09_0172.ogg"
    jordh "「この後どうなるのかなぁ。おお！　咥えた！！」"

    kosuke "「いや、もうやらなくていいから！」"

    voice "audio/voice/op09/op09_0173.ogg"
    fauna "「えっちです。えっちです。えっちです。えっちです」"

    kosuke "「（そう言いながら、画面凝視してるよな……）」"

    voice "audio/voice/op09/op09_0174.ogg"
    jordh "「うわっ、すっごい。全身ドロドロになっちゃった」"

    voice "audio/voice/op09/op09_0175.ogg"
    fauna "「えっちです。えっちです。えっちです。えっちです」"

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0176.ogg"
    jordh 007 "「幸介、こんなゲームばっかりやってると、脳味噌海綿体になっちゃうよ？」"

    kosuke "「ごめん」"

    voice "audio/voice/op09/op09_0177.ogg"
    jordh 013 "「んー。つまり幸介君は、この二次元美少女の恥ずかしがりながらも内心喜んでる顔がタマランのだね？」"

    kosuke "「いや、まあ……」"

    voice "audio/voice/op09/op09_0178.ogg"
    fauna "「えっちです。えっちです。えっちです。えっちです。えっちです」"

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0179.ogg"
    "ゲーム" "『わたし、お兄ちゃんじゃないと、もう感じなくなっちゃった……』"

    voice "audio/voice/op09/op09_0180.ogg"
    jordh 001 "「よっしゃ！　調教完了！　次のステップ行くぞー！」"

    voice "audio/voice/op09/op09_0181.ogg"
    fauna "「えっちです。えっちです。えっちです。えっちです。えっちです。えっちです。んまっ、こんな絵まで……！」"

    kosuke "「二人とも熱中しとるがな……」"

    scene black
    with Dissolve(2)

    stop music

    play music "audio/bgm/bgm01.ogg"

    scene bg01e
    show jor 001 at left
    show fau 003 at right
    with ImageDissolve("images/wipe/16.png", 1.5)

    voice "audio/voice/op09/op09_0182.ogg"
    jordh "「ああ、面白かった。もっと無いかなー」"

    kosuke "「わあっ！　もう探さなくていいから！」"

    voice "audio/voice/op09/op09_0183.ogg"
    jordh 013 "「おーっと、今度はえっちな本発見ー！　びろーん」"

    voice "audio/voice/op09/op09_0184.ogg"
    fauna 008 "「きゃっ」"

    voice "audio/voice/op09/op09_0185.ogg"
    jordh 007 "「すっげ、薄消し！」"

    kosuke "「だ、だから、なんでそんな簡単に見つけるんだよ！　すっごい隠してるのに！」"

    voice "audio/voice/op09/op09_0186.ogg"
    jordh 013 "「びろーん」"

    kosuke "「広げなくていいから！」"

    voice "audio/voice/op09/op09_0187.ogg"
    jordh 007 "「あーでも、この子よりファウナの方が胸の形良いよ？」"

    kosuke "「え？　そうなんだ……？」"

    voice "audio/voice/op09/op09_0188.ogg"
    fauna 002 "「ね、姉さん！」"

    voice "audio/voice/op09/op09_0189.ogg"
    jordh 013 "「ふふ、ほら、見てごらん？　ファウナはここがもっと張ってるだろ？」"

    kosuke "「どれどれ……。じー」"

    voice "audio/voice/op09/op09_0190.ogg"
    fauna 009 "「はっ」"

    "さっと胸を隠すファウナ。"

    voice "audio/voice/op09/op09_0191.ogg"
    fauna "「み、見ないでくださいっ」"

    kosuke "「ご、ごめんっ。つい……」"

    voice "audio/voice/op09/op09_0192.ogg"
    fauna 003 "「えっち」"

    voice "audio/voice/op09/op09_0193.ogg"
    jordh 001 "「まあまあ、男なんだからしょーがないって。ねー？」"

    kosuke "「って、ヨルズが誘導したんじゃないか！」"

    voice "audio/voice/op09/op09_0194.ogg"
    fauna "「えっちです。この人えっちです。えっちです。えっちです。えっちです。えっちです。えっちです。えっちです」"

    kosuke "「こ、こわいんですけど……」"

    stop music

    play sound "audio/sound/se000.ogg"

    voice "audio/voice/op09/op09_0195.ogg"
    klotho "「黒崎です。川神さん、宜しいかしら？」"

    kosuke "「あ、管理人さん。どうぞ」"

    scene black
    with Dissolve(1)

    play sound "audio/sound/se003.ogg"

    scene bg08c
    with Dissolve(1)

    show kur 008 at center
    with dissolve

    play music "audio/bgm/bgm15.ogg"

    voice "audio/voice/op09/op09_0196.ogg"
    klotho "「失礼しま……ひっ！」"

    kosuke "「え？」"

    "管理人さんが後ろの女子２人を見て固まった。"

    kosuke "「どうしました？」"

    voice "audio/voice/op09/op09_0197.ogg"
    klotho 009 "「い、いえ、なんでも」"

    voice "audio/voice/op09/op09_0198.ogg"
    klotho 000 "「これ、回覧板です。そちらの二人にも回してください」"

    kosuke "「はい」"

    voice "audio/voice/op09/op09_0199.ogg"
    klotho "「では、失礼します」"

    hide kur
    with dissolve

    stop music

    play sound "audio/sound/se004.ogg"

    scene black
    with Dissolve(2)

    scene bg01e
    with Dissolve(1)

    play music "audio/bgm/bgm01.ogg"

    show fau 000 at right
    show jor 000 at left
    with dissolve

    kosuke "「…………」"
    kosuke "「なんで管理人さん、２人を見て驚くんだろう？」"

    voice "audio/voice/op09/op09_0200.ogg"
    jordh "「そんなの決まってるじゃないの」"

    kosuke "「え？」"

    voice "audio/voice/op09/op09_0201.ogg"
    jordh "「あまりの美人さに、息をのんでしまったのよ」"

    kosuke "「…………」"

    voice "audio/voice/op09/op09_0202.ogg"
    jordh 003 "「なんで黙んのよ？」"

    kosuke "「え、いやっ」"

    voice "audio/voice/op09/op09_0203.ogg"
    jordh 003 "「なんで？」"

    kosuke "「いやそのっ」"

    voice "audio/voice/op09/op09_0204.ogg"
    jordh 011 "「私たちが美人じゃないとでも？」"

    kosuke "「い、いや、そういう意味では決して……！」"

    voice "audio/voice/op09/op09_0205.ogg"
    jordh 002 "「このっ、このこのこのっ！」"

    play sound "audio/sound/se029.ogg"

    kosuke "「くっ……ヨルズ……！　ち、ちがうんだ！　くっ……首を……首を絞めないで……！」"

    voice "audio/voice/op09/op09_0206.ogg"
    fauna 011 "「ひょっとして、女性恐怖症とか？」"

    kosuke "「お、落ち着いて答えてないで、なんとかしてっ！　苦しいんですけどっ！」"

    voice "audio/voice/op09/op09_0207.ogg"
    fauna 008 "「あ、ごめんなさいっ。ヨルズ、やめて」"

    voice "audio/voice/op09/op09_0208.ogg"
    jordh 011 "「わかったわよ」"

    kosuke "「ぷはっ。ごほごほっ」"

    voice "audio/voice/op09/op09_0209.ogg"
    fauna "「だ、大丈夫ですか？」"

    kosuke "「う、うん」"

    show fau 000 at right
    with dissolve

    kosuke "「（はあ。首、取れるかと思った……）」"

    voice "audio/voice/op09/op09_0210.ogg"
    jordh 007 "「でも、女なのに女性恐怖症は無いんじゃない？」"

    kosuke "「人そのものが怖いとか」"

    voice "audio/voice/op09/op09_0211.ogg"
    jordh "「アンタに対しては平気じゃない」"

    kosuke "「きっとカッコイイ男なら平気なのさっ。フッ」"

    voice "audio/voice/op09/op09_0212.ogg"
    jordh 002 "「なーに言ってんのよ！　こいつめっ！　こいつめっ！」"

    play sound "audio/sound/se029.ogg"

    kosuke "「だ、だから技かけないで……しかも楽しそうに……！　ギブギブ！　息……息が！！」"

    voice "audio/voice/op09/op09_0213.ogg"
    fauna 002 "「姉さんっ」"

    voice "audio/voice/op09/op09_0214.ogg"
    jordh 000 "「はいはい」"

    kosuke "「はぁ……まったく」"

    # TODO: ^se0,se038,255,0,0
    play sound "audio/sound/se038.ogg"

    "（ぐうー）"

    kosuke "「あう。お腹鳴った」"

    show fau 000 at right
    show jor 009 at left
    with dissolve

    voice "audio/voice/op09/op09_0215.ogg"
    jordh "「そういやお腹すいたわね」"

    voice "audio/voice/op09/op09_0216.ogg"
    fauna "「そうね。いつの間にか夕方だし」"

    voice "audio/voice/op09/op09_0217.ogg"
    jordh 000 "「幸介、なんか作ってよ」"

    kosuke "「作るって、なにを？」"

    voice "audio/voice/op09/op09_0218.ogg"
    jordh "「料理」"

    kosuke "「無理」"

    voice "audio/voice/op09/op09_0219.ogg"
    jordh 007 "「アンタ、まさか料理できないの？」"

    kosuke "「そのまさかだ」"

    show jor 000 at left
    show fau 007 at right
    with dissolve

    voice "audio/voice/op09/op09_0220.ogg"
    fauna "「独り暮らしなのに、どうやって食事をしてるんです？」"

    kosuke "「主にコンビニ弁当だね。あとはカップラーメン」"

    voice "audio/voice/op09/op09_0221.ogg"
    fauna "「コンビニ弁当……？　ラーメン……？」"

    kosuke "「あ、知らない？　コンビニエンスストアで売ってる弁当か、そこに積んであるインスタントラーメン」"

    voice "audio/voice/op09/op09_0222.ogg"
    fauna "「……毎日それだと、栄養が偏りませんか？」"

    kosuke "「仕方ないよ、作れないし。足りない分はサプリメントで補給」"

    voice "audio/voice/op09/op09_0223.ogg"
    fauna 010 "「そんな、不健康な……」"

    voice "audio/voice/op09/op09_0224.ogg"
    fauna 011 "「わかりました」"

    kosuke "「え？」"

    voice "audio/voice/op09/op09_0225.ogg"
    fauna "「明日から、わたしが幸介さんの食事を作ります！」"

    kosuke "「え、マジ？」"

    voice "audio/voice/op09/op09_0226.ogg"
    fauna 000 "「はい。こんなものばかり食べていたら、絶対体に悪いですから！」"

    kosuke "「そんな、嬉しいけど悪いよ。嬉しいけど。うん、嬉しいな」"

    voice "audio/voice/op09/op09_0227.ogg"
    fauna "「わたしと姉さんの分は作ることになりますから、２人分も３人分も変わりません」"

    kosuke "「そっか……。じゃあ、お願いしようかな」"

    voice "audio/voice/op09/op09_0228.ogg"
    fauna 001 "「はい、喜んで！」"

    kosuke "「（凄い嬉しそうな顔……。料理も好きなのかな？）」"
    kosuke "「あれ？　でも、なんで明日から？　二人とも、夜はどうするの？」"

    voice "audio/voice/op09/op09_0229.ogg"
    fauna 010 "「あ、その、人間の食べ物の研究を先にしないと、味の付け方に差がありそうなので……」"

    kosuke "「へ？」"

    voice "audio/voice/op09/op09_0230.ogg"
    jordh 008 "「ファウナ！」"

    voice "audio/voice/op09/op09_0231.ogg"
    fauna 008 "「えっ、えと、この国の料理を今日は研究したいと思いますので。はい！」"

    kosuke "「ふーん……」"

    show fau 000 at right
    show jor 001 at left
    with dissolve

    voice "audio/voice/op09/op09_0232.ogg"
    jordh "「寿司！」"

    kosuke "「は？」"

    voice "audio/voice/op09/op09_0233.ogg"
    jordh "「今は寿司食べよう！　そう、寿司って食べてみたかったのよ！　寿司寿司！　へいらっしゃいっ！　幸介、出前\n頼んで！」"

    show fau 007 at right
    with dissolve

    kosuke "「お、良いね。ヨルズの奢り？」"

    voice "audio/voice/op09/op09_0234.ogg"
    jordh "「幸介の！」"

    kosuke "「そんな金ねぇ！」"

    voice "audio/voice/op09/op09_0235.ogg"
    jordh 003 "「何よ甲斐性なし」"

    kosuke "「ぐあっ」"

    voice "audio/voice/op09/op09_0236.ogg"
    jordh "「わたしたちに散々ゲームで羞恥プレイさせておいて、奢りもしないっての？」"

    kosuke "「勝手にやってたんじゃんか！　しかも熱中して！」"

    voice "audio/voice/op09/op09_0237.ogg"
    jordh 016 "「ねぇ、奢ってぇ？　あなたと私の仲じゃない。ね？」"

    kosuke "「け、けど……」"

    voice "audio/voice/op09/op09_0238.ogg"
    jordh 017 "「なんだったら、またファウナのパンツ見せてあげるから」"

    kosuke "「マジ！？」"
    kosuke "「って、またこの展開かよ！」"

    stop music

    scene black
    with Dissolve(2)

    jump op10
