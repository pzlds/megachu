label op03:
    $ save_name = _("オープニング")

    play music "audio/bgm/bgm02.ogg"

    scene bg24
    with dissolve

    kosuke "「ううう……」"

    "結局抱き枕付きは買えなかった。俺の目の前で最後の一個が売れてしまった。"
    "俺っていっつもこう。とにかく運が悪い。"

    kosuke "「でもまぁ、女の子とエロゲーっぽいことができたし、今日は良しとするか」"

    stop music

    show fau 111 at center
    with dissolve

    kosuke "「あれ？　君はさっきの……」"

    $ fauna_name = _("女の子")

    voice "audio/voice/op03/op03_0000.ogg"
    fauna 110 "「…………」"

    "でも、さっきと全然雰囲気が違うな。別人……かな？"

    voice "audio/voice/op03/op03_0001.ogg"
    fauna 111 "「……川神幸介さんですね？」"

    kosuke "「へ？」"

    voice "audio/voice/op03/op03_0002.ogg"
    fauna "「川神幸介さんですね？」"

    kosuke "「はぁ、まぁ……」"
    kosuke "「（何で俺の名前知ってるんだろう？）」"
    kosuke "「あの、俺に何か……？」"

    voice "audio/voice/op03/op03_0003.ogg"
    fauna "「…………」"

    voice "audio/voice/op03/op03_0004.ogg"
    fauna 110 "「人間なんて、自分の事しか考えてない。アレが宿ってるなら善人なわけない……」"

    kosuke "「はい？」"

    voice "audio/voice/op03/op03_0005.ogg"
    fauna 111 "「突然ですが、天界憲法第３６条第３項の説明をします」"

    kosuke "「へ？」"

    voice "audio/voice/op03/op03_0006.ogg"
    fauna "「地球上に我が物顔で存在する本来干渉すべきでない人間に対し、監視を行いつつもこの者たちの中に我々天界の脅威となる存在が発見された場合……」"

    "な、なんだ？　この人、いきなりわけのわからんことを言い始めたぞ？"
    "変な服着てるし、何かのカルト教団かな……？　だったら、関わるとヤバそう……。"

    voice "audio/voice/op03/op03_0007.ogg"
    fauna "「よって、あなたはこれ以上この世界に存在し続けることができません」"

    kosuke "「……は？」"

    voice "audio/voice/op03/op03_0008.ogg"
    fauna "「以上の理由により……川神幸介さん。あなたを……デリートします」"

    kosuke "「へ？　デリートって……？」"

    play music "audio/bgm/bgm10.ogg"

    voice "audio/voice/op03/op03_0009.ogg"
    fauna 115 "『ファウナの名において命ずる。大気よ、激しく震え、その怒りを彼の者に向けて解き放て！』"
    # TODO: ^nature0, "雷弾単発"

    "なんだ？　彼女の周りに、蛍のような小さな発光体が集まりだした……！？"

    play sound "audio/sound/se039.ogg"

    # TODO:
    # ^filter,"\zoom,400,300,110,110 \blur,10,10 \color,$FFB40000,2",300
    # ^filter,,300

    "（ドクン……！）"

    kosuke "「うっ。何だこの気持ち悪さ……」"

    "その変化と呼応するように、俺の心の奥底からドス黒い何かが急に沸き上がってきた。"
    "体がピリピリと痺れだす。"

    # TODO:
    # ^nature0,"雷弾複数"
    # ^naturemotion0,"*Charge"

    voice "audio/voice/op03/op03_0010.ogg"
    fauna 114 "「お願い！　安らかに成仏してくださいっ！！"

    kosuke "「え？」"

    # TODO: ^naturemotion0, "*Shoot1"

    "状況を理解するより早く、彼女の手の平に出現した光の玉が、俺目掛けて一直線に飛んでくる！"

    scene white
    with ImageDissolve("images/wipe/08.png", 0.1)

    kosuke "「危ねぇ！！」"

    "考えるより早く体が動いた。弾かれるように俺の身体が横に跳ぶ。"
    "刹那、光の玉が今まで俺のいた場所を高速で通過していった。"
    "光は後ろのブロック塀に当り、弾けた。"

    play sound "audio/sound/se069.ogg"

    "瞬間、身の毛のよだつ鋭い音が鳴り響き、塀が弾け飛んだ。"

    scene bg24
    show fau 108 at center
    with dissolve

    voice "audio/voice/op03/op03_0011.ogg"
    fauna "「外れた！？」"

    kosuke "「ちょ、ちょっと待て！　なんだ今のは！？」"

    voice "audio/voice/op03/op03_0012.ogg"
    fauna 102 "「超高圧１００メガボルトの雷弾です」"

    kosuke "「１００メガショック！？　って、ええ！？」"

    voice "audio/voice/op03/op03_0013.ogg"
    fauna "「次は外しません」"

    kosuke "「い、いや、ちょっと、ちょっと待って！　話せばわかる！」"

    voice "audio/voice/op03/op03_0014.ogg"
    fauna "「安心してください！　苦しまないように一撃で仕留めますから！」"

    kosuke "「そういう問題じゃないでしょ！」"

    voice "audio/voice/op03/op03_0015.ogg"
    fauna 115 "『雷弾よ、彼の者を打ち抜け！』"
    # TODO: ^nature0,"雷弾単発"

    # TODO:
    # ^nature0,"雷弾複数"
    # ^naturemotion0,"*Charge"

    kosuke "「聞いてねえし！」"

    # TODO: ^naturemotion0,"*Shoot1"

    voice "audio/voice/op03/op03_0016.ogg"
    fauna 114 "「えいっ！」"

    kosuke "「ひええええええ！！」"

    scene white
    with ImageDissolve("images/wipe/08.png", 0.1)

    play sound "audio/sound/se069.ogg"

    scene bg24
    show fau 113 at center
    with Dissolve(0.5)

    voice "audio/voice/op03/op03_0017.ogg"
    fauna "「ええい！　わたしの攻撃を２度もかわさないでください！」"

    kosuke "「ばか！　やめろって！　死ぬって！　そんなの当たったらシャレにならねーって！」"

    voice "audio/voice/op03/op03_0018.ogg"
    fauna 102 "「ですから、あなたをデリートするんです！」"

    kosuke "「すんなよ！　一体何なんだよ、君は！？」"

    voice "audio/voice/op03/op03_0019.ogg"
    fauna 111 "「わたしは女神です！」"

    kosuke "「女神ぃ……！？」"
    kosuke "「あーっはっはっはっはー」"

    voice "audio/voice/op03/op03_0020.ogg"
    fauna 108 "「な、何がおかしいんです！？」"

    kosuke "「女神がそんなヘンな格好なんかしてるわけないだろ！　エロゲーじゃあるまいし！」"

    voice "audio/voice/op03/op03_0021.ogg"
    fauna 102 "「ヘンとは何ですかヘンとは！　女神を侮辱しないでください！　『八つ裂きにしちゃう光輪』を浴びせますよ！？」"

    kosuke "「へん。大体、ホントに女神だったとして、何で俺が殺されなけりゃならないのさ！？」"

    voice "audio/voice/op03/op03_0022.ogg"
    fauna "「ですから！　あなたの存在はこの地球にとって危険なんです！　何も言わず、大人しく殺されてください！」"

    kosuke "「冗談じゃない！　マジでそんなこと言ってんのかよ！」"

    voice "audio/voice/op03/op03_0023.ogg"
    fauna 114 "「本気です！　真剣です！　わたし、大マジです！　ですから……えいっ！」"

    # TODO: ^naturemotion0, "*Shoot3"

    kosuke "「だからやめろって……わっ！」"

    play sound "audio/sound/se069.ogg"

    # TODO: ^effect,Flash_$FFFFFFFF,500

    kosuke "「危ないってば！」"

    voice "audio/voice/op03/op03_0024.ogg"
    fauna 102 "「避けると苦しみが増すだけです！　避けないでください！」"

    kosuke "「できっかよ！」"

    voice "audio/voice/op03/op03_0025.ogg"
    fauna "「ならば、これでどうです！」"

    # TODO: ^naturemotion0,"*Shoot2"

    show fau 114

    "多数の雷弾が俺に迫る！"
    "でも……これなら避けられる―――！　……？"

    play sound "audio/sound/se069.ogg"
    # TODO: ^effect,Flash_$FFFFFFFF,500

    kosuke "「よっ！」"

    play sound "audio/sound/se069.ogg"
    # TODO: ^effect,Flash_$FFFFFFFF,500

    kosuke "「はっ！」"

    play sound "audio/sound/se069.ogg"
    # TODO: ^effect,Flash_$FFFFFFFF,500

    kosuke "「ほっ！」"

    play sound "audio/sound/se069.ogg"
    # TODO: ^effect,Flash_$FFFFFFFF,500

    kosuke "「なんとっ！」"

    "最後の一発も難なく空中でかわし、俺は一回転をして両足を揃えて着地した。"

    kosuke "「１０．０！」"

    voice "audio/voice/op03/op03_0026.ogg"
    fauna 108 "「なんでそんなに運動神経良いんですか！？　というか、明らかに物理法則を無視してますよ、今の！」"

    kosuke "「知るかよ！　何故か勝手に体が動いちゃうんだっ！」"

    voice "audio/voice/op03/op03_0027.ogg"
    fauna 111 "「じゃあ、これなら……！」"

    kosuke "「今度はなんだ！？」"

    voice "audio/voice/op03/op03_0028.ogg"
    fauna 114 "「エネルギー収束！　ドドンと一発！　ええーいっ！！」"

    # TODO: ^naturemotion0,"*Shoot2"

    kosuke "「来る！　左と右から、ほぼ同時に１２０発……！」"
    kosuke "「（……え？　何で俺そんなことわかるんだ！？）」"

    scene white
    with dissolve

    play sound "audio/sound/se069.ogg"

    scene bg24
    show fau 108
    with Dissolve(2)

    play sound "audio/sound/se072.ogg"

    voice "audio/voice/op03/op03_0029.ogg"
    fauna "「……！！」"

    kosuke "「はぁ……はぁ……はぁ……」"

    voice "audio/voice/op03/op03_0030.ogg"
    fauna "「全弾……避けた……！？」"

    kosuke "「すっげー。俺、こんなに運動神経良かったんだ……！」"

    voice "audio/voice/op03/op03_0031.ogg"
    fauna 111 "「……なるほど。これも、あの力の影響だって言うんですね」"

    kosuke "「え？　あの力？」"

    voice "audio/voice/op03/op03_0032.ogg"
    fauna "「あなたの中に眠っているモノの力です」"

    kosuke "「眠っているもの……？　俺の中に何が眠ってるって言うんだ！？」"

    voice "audio/voice/op03/op03_0033.ogg"
    fauna "「……そうですね。あなたには知る権利があります」"

    voice "audio/voice/op03/op03_0034.ogg"
    fauna "「いいでしょう。お話しします。あなたの体内には、実は……」"

    kosuke "「秘技・逃げるが勝ち！　……ターボダッシュ！」"

    play sound "audio/sound/se030.ogg"

    voice "audio/voice/op03/op03_0035.ogg"
    fauna 108 "「ああっ！　語らせている隙に逃げるとは、なんて卑怯な！」"

    voice "audio/voice/op03/op03_0036.ogg"
    fauna 110 "「（やっぱり人間は姑息で卑怯者です！）」"

    voice "audio/voice/op03/op03_0037.ogg"
    fauna 102 "「待ちなさい！」"

    scene black
    with Dissolve(1)

    jump op04
