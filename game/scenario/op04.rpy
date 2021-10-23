label op04:
    $ save_name = _("オープニング")

    scene bg13
    with Dissolve(1)

    kosuke "「はあ……はあ……はあ……」"
    kosuke "「何だったんだ、さっきのは……？」"

    "あの子が出したモノ……雷弾とか言ってたか？　あれは確かに、俺の後ろのブロックを破壊していた。"
    "あれは手品なんかじゃない。もちろん特殊撮影でもない。すると……"

    menu:
        "夢？":
            "夢？"

            kosuke "「うん。夢ならありうる」"

            "俺は思いっきり頬をつねってみた。"

            kosuke "「イテテ！！」"

            "夢じゃない……みたいだ。信じられないけど。"

        "現実？":
            "現実？"
            "もしかして、女神とチョメチョメする妄想ばかりしてたから、怒って天罰を与えに来たとか……？"

            kosuke "「まさかな」"

            "…………。"
            "ありえるかも。"

    kosuke "「それにしてもあいつ……本当に女神なのか？　いきなり襲って来たりして、死神の間違いじゃないのか？」"

    show fau 102 at center

    voice "audio/voice/op04/op04_0000.ogg"
    fauna "「失礼な。わたしは正真正銘、女神です！」"

    kosuke "「わ！」"

    voice "audio/voice/op04/op04_0001.ogg"
    fauna "「逃げても無駄です。あなたは絶対に逃げられないんですから」"

    kosuke "「逃げてやるさ！　……あ！　空飛ぶ飛行機！！」"

    voice "audio/voice/op04/op04_0002.ogg"
    fauna 108 "「え！？　どこどこ！？」"

    voice "audio/voice/op04/op04_0003.ogg"
    fauna 111 "「って、飛行機が空を飛ぶのは当たり前……」"

    play sound "audio/sound/se030.ogg"

    voice "audio/voice/op04/op04_0004.ogg"
    fauna 108 "「ああっ！？」"

    voice "audio/voice/op04/op04_0005.ogg"
    fauna 110 "「こ、こんな単純な手に引っかかるなんてぇ〜っ」"

    scene black
    with Dissolve(0.5)

    kosuke "「クソ！　なんだってんだ！　俺、なんか悪い事したのか！？」"
    kosuke "「俺はごくごく平凡な大学生で、どう考えても恨まれるような生き方はしてないはずだぞ？　なのに、なんでこんな目にあわなきゃならないんだ！？」"

    "死に直面し、事態のわけわからなさと不条理さで余計頭に来てる。"
    "本当はもっと詳しくあいつに訊かなきゃいけない気がするけど、聞いた瞬間殺されそうで怖い。"

    kosuke "「ホントにあいつ、俺を殺そうとしてるのか……？」"
    kosuke "「嫌だ！　殺されるなんて冗談じゃない！　積んだままのエロゲーだってまだ沢山あるってのに！」"

    play sound "audio/sound/se119.ogg"

    scene bg25
    with ImageDissolve("images/wipe/06.png", 0.5)

    kosuke "「はあ……はあ……はあ……はあ……ここまで来れば……」"

    show fau 102 at center
    with Dissolve(0.5)

    voice "audio/voice/op04/op04_0006.ogg"
    fauna "「逃げても無駄ですってば」"

    kosuke "「わっ」"
    kosuke "「なんて、驚くとでも思ったのか？」"

    voice "audio/voice/op04/op04_0007.ogg"
    fauna 107 "「え？」"

    kosuke "「ここには人が沢山いる！　俺を攻撃したら周りにも被害が行くんだぜ？　アンタが本当に女神なら、そんなことできないはずだ！」"

    voice "audio/voice/op04/op04_0008.ogg"
    fauna 115 "『ファウナの名において命ず……』"
    # TODO: ^nature0,"雷弾単発"

    # TODO: ^naturemotion0,"*Charge"

    kosuke "「って無視かよ！　お前ホントに女神かよ！？」"

    # TODO: ^naturemotion0,"*Shoot1"

    voice "audio/voice/op04/op04_0009.ogg"
    fauna 114 "「一点集中！！」"

    kosuke "「上からか！」"

    play sound "audio/sound/se059.ogg"

    # TODO: ^effect,Flash_$FFFFFFFF,1000

    kosuke "「わっ！」"

    voice "audio/voice/op04/op04_0010.ogg"
    fauna 111 "「くっ……。精神体への攻撃もやっぱり当たらない」"

    kosuke "「まったく！　無差別攻撃なら、こんなとこにいたら被害が広がっちまう！」"

    play sound "audio/sound/se030.ogg"

    voice "audio/voice/op04/op04_0011.ogg"
    fauna 102 "「あっ、待ちなさい！」"

    scene bg13
    with ImageDissolve("images/wipe/06.png", 0.5)

    kosuke "「はあ……はあ……はあ……。そろそろキツイなっ！　入学してから全然運動してなかったからなっ……はあっ……」"

    voice "audio/voice/op04/op04_0012.ogg"
    "男" "「よお、川神」"

    kosuke "「おっ……」"
    kosuke "「（えっとこいつは、同じ学科の……顔は覚えてるけど、誰だっけ……？）」"

    voice "audio/voice/op04/op04_0013.ogg"
    "男" "「どーした？　マラソンか？」"

    kosuke "「ああ……あ！　ちょっとこの自転車借りるな？」"

    voice "audio/voice/op04/op04_0014.ogg"
    "男" "「え？　あ、まあいいけど……」"

    kosuke "「悪い！　学校で返すから！」"

    voice "audio/voice/op04/op04_0015.ogg"
    "男" "「おお……。ってお前！　後期始まるまでまだ２カ月あるよ！　お〜い！」"

    kosuke "「（恩に着るぜ！　……誰だか思い出せない友人よ！）」"

    scene black
    with Dissolve(0.5)

    kosuke "「よし、機動力アップだ！」"
    kosuke "「子供の頃、『疾風のコウちゃん』と呼ばれてた俺の自転車テクを見せてやるぜ！」"
    kosuke "「女神だろうが死神だろうが、ぶっちぎってやる！」"

    scene bg24s
    with ImageDissolve("images/wipe/08.png", 0.5)

    voice "audio/voice/op04/op04_0016.ogg"
    fauna 102 "「だから女神ですってばー」"

    kosuke "「うわ！　なんで全力で走ってる自転車についてきてるんだよ！　しかも後向きで走ってるし！」"

    voice "audio/voice/op04/op04_0017.ogg"
    fauna 111 "「こんなの、女神の常識です！」"

    kosuke "「嘘つけ！」"

    stop music

    voice "audio/voice/op04/op04_0018.ogg"
    fauna 111 "「とにかく、そろそろ命を……あっ！」"

    kosuke "「うわっ！　猫が目の前に！　ぶつかる！！」"

    voice "audio/voice/op04/op04_0019.ogg"
    fauna 108 "「だめ！　術が間に合わない……！！」"

    kosuke "「こなくそ！」"

    "俺は地面を思いっきり蹴り、車体を傾けて強引に進路を変えた。"

    play sound "audio/sound/se111.ogg"

    "転倒寸前の俺の前に、今度は電柱が迫る。"

    kosuke "「わわわわわわわわ！！！！！」"

    play sound "audio/sound/se073.ogg"

    # TODO: ^effect,Quake,1000

    scene bg24
    with Dissolve(1)

    show fau 109 at center
    with Dissolve(1)

    voice "audio/voice/op04/op04_0020.ogg"
    fauna "「え……？」"

    kosuke "「……痛っ……ててててて……」"

    voice "audio/voice/op04/op04_0021.ogg"
    fauna 110 "「（わざと転倒して……猫を……避けたの？　……あのまま走っていたら猫を轢いてしまったから？）」"

    kosuke "「ぐっ、体中が痛ぇ……。腕と膝から血が出てやがる……」"

    voice "audio/voice/op04/op04_0022.ogg"
    fauna "「（でも、あのスピードで転倒すれば自分がこうなることはわかっていたはず……。それでもこの人は、猫を助けようとしたの……？）」"

    # TODO: ^chara,fau

    kosuke "「……はっ、猫は！？」"

    voice "audio/voice/op04/op04_0023.ogg"
    "ねこ" "「にゃー」"

    kosuke "「ふぅ……無事か……」"

    voice "audio/voice/op04/op04_0024.ogg"
    fauna 109 "「…………」"

    voice "audio/voice/op04/op04_0025.ogg"
    fauna 110 "「（本当にこの人は悪い人なの……？　残虐で身勝手な人間なの……？）」"

    # TODO: ^chara,fau

    kosuke "「あっ、逃げなきゃ！　くっ……！　足が痺れてる！」"
    kosuke "「自転車は……チェーンが外れてるのか！　クソ！　どこまで俺はツイてないんだ！」"
    kosuke "「でも、諦めるもんか……！」"

    play sound "audio/sound/se031.ogg"

    voice "audio/voice/op04/op04_0026.ogg"
    fauna 109 "「…………」"

    voice "audio/voice/op04/op04_0027.ogg"
    fauna "「あの人は……。人間は、もしかして……」"

    play sound "audio/sound/se042.ogg"

    voice "audio/voice/op04/op04_0028.ogg"
    fauna 100 "「あ、はい……」"

    $ jordh_name = _("？？？")

    voice "audio/voice/op04/op04_0029.ogg"
    jordh "「ファウナ？　どう？　そっちの具合は」"

    voice "audio/voice/op04/op04_0030.ogg"
    fauna 109 "「あ、うん……えと、突破された」"

    voice "audio/voice/op04/op04_0031.ogg"
    jordh "「ええ、アンタが！？」"

    voice "audio/voice/op04/op04_0032.ogg"
    jordh "「フフフ、あいつなかなかやるわね。なんだか燃えてきたわ」"

    voice "audio/voice/op04/op04_0033.ogg"
    fauna "「姉さん？」"

    voice "audio/voice/op04/op04_0034.ogg"
    jordh "「絶対……私の手でデリートしてやるから覚悟なさい！」"

    voice "audio/voice/op04/op04_0035.ogg"
    fauna 108 "「ちょ、ちょっとヨルズ！？」"

    voice "audio/voice/op04/op04_0036.ogg"
    jordh "「おっと、波動パターン感知、ターゲットがこっち来たわ。じゃあね！」"

    voice "audio/voice/op04/op04_0037.ogg"
    fauna "「あ！　ヨルズ！　待って……！」"

    voice "audio/voice/op04/op04_0038.ogg"
    fauna 110 "「…………」"

    voice "audio/voice/op04/op04_0039.ogg"
    fauna "「ううん。これは任務なのよ。私情を挟んではだめ」"

    voice "audio/voice/op04/op04_0040.ogg"
    fauna 111 "「わたしも……行かなくちゃ！」"

    scene black
    with Dissolve(2)

    jump op05
