label op05:
    $ save_name = _("オープニング")

    play music "audio/bgm/bgm12.ogg"

    scene bg15c
    with dissolve

    kosuke "「はあ……はあ……はあ……。やばい、マジでどうしよう」"

    "このままじゃ、いつか追い詰められてしまう"

    kosuke "「あ！　あの後ろ姿はお巡りさん！」"
    kosuke "「よし、こうなったら国家権力に助けてもらおう！」"
    kosuke "「あの、お巡りさん！」"

    "お巡りさん" "「…………」"

    kosuke "「？」"

    "聞こえてないのかな？"

    kosuke "「あの！」"

    "お巡りさん" "「…………」"

    kosuke "「……？　あのぉ……？」"

    "不審に思って、前に回ってみた。"

    kosuke "「わっ！　し……死んでる！？」"

    "いや、死んでるというより、止まってるといったほうが正確かもしれない。"
    "うまく言えないけど、まるでお巡りさんの時間が止まってしまったような、そんな感じに体が固まっている。"
    "とにかく異常事態だ。誰か助けを呼ぼう！"
    "よし、あのおじさんに……"

    kosuke "「あ、すみません！　そこのお巡りさんが……、わ！」"
    kosuke "「……この人も……固まってる……？」"
    kosuke "「まさか……！」"

    "辺りを見渡すと、皆、写真のように動きの途中の体勢で止まっていた。"

    kosuke "「……どっきり？」"

    "もしやと思い、近くの女の子の鼻をつまんでみた。"
    "反応無し。"
    "本当にみんな固まってしまっている。"

    kosuke "「ということは……。おっぱい揉んでも気付かれない\nな……」"
    kosuke "「なんて、バカ言ってる場合じゃない！」"
    kosuke "「どうなってんだ！？　まさか、これもあいつの仕業なのか！？」"

    $ jordh_name = "？？？"

    voice "audio/voice/op05/op05_0002.ogg"
    jordh "「その通りよ」"

    kosuke "「え？」"

    show jor 100 at center
    with dissolve

    kosuke "「わあっ！　だ、誰だお前！？」"

    $ jordh_name = _("お姉さん")

    voice "audio/voice/op05/op05_0003.ogg"
    jordh "「知る必要は無いわ。だってアンタ、もうすぐ死ぬんだから」"

    kosuke "「ひっ……！」"

    voice "audio/voice/op05/op05_0004.ogg"
    jordh 113 "「ふふ。私はあの子みたいに生易しくないわよ？　ヒィヒィ言わせてやるから覚悟なさい？」"

    # TODO: ^nature0,"炎魔法"

    voice "audio/voice/op05/op05_0005.ogg"
    jordh 114 "『イレ、イグニス、クレマーレ、太古の命約に基づき、火の精霊よ、彼の穢れを焼き尽くせ！』"

    # TODO: ^naturemotion0,"*Shoot"

    kosuke "「くそ！　俺がいつまでも逃げると思うなよっ」"

    # TODO: ^nature0

    play sound "audio/sound/se069.ogg"

    # TODO: ^effect,Flash_$C0FF5600,500

    "（どどーん！）"

    kosuke "「うわーんっ！　やっぱダメかぁ！」"

    voice "audio/voice/op05/op05_0006.ogg"
    jordh 113 "「ついでに、それっ」"

    # TODO: ^effect,stop
    # TODO: ^chara,jor

    # TODO: ^nature0,"炎魔法"
    # TODO: ^naturemotion0,"*Round2"
    # TODO: ^effect,Overlap

    play sound "audio/sound/se191.ogg"

    # TODO: ^effect,Flash_$C0FF5600,500

    "３つの火の玉が突然現れ、俺を取り囲むように、ゆっくりと揺らぎながら廻っている。"

    voice "audio/voice/op05/op05_0007.ogg"
    jordh 117 "「そーれそーれ、逃げないとまっ黒こげよぉー？」"

    kosuke "「逃げるったって……」"

    "不意に、３つの火の玉の位置が重なった。"

    kosuke "「（そうか、廻ってる速度が違うから……！）」"
    kosuke "「…………」"
    kosuke "「それ！」"

    # TODO: ^nature0

    "俺はその一瞬を狙って包囲網を突破し、全速力で逃げた。"

    play sound "audio/sound/se030.ogg"

    voice "audio/voice/op05/op05_0008.ogg"
    jordh 100 "「そうそう、そっちしか逃げられないものね。フフフ\nフ……」"

    # TODO: ^effect,stop,,1
    # TODO: ^chara,jor

    scene bg17c
    with dissolve

    kosuke "「はあ……はあ……はあ……」"
    kosuke "「あれ？　いつの間にか追ってきた火の玉が消えて\nる……？」"

    voice "audio/voice/op05/op05_0009.ogg"
    "？？？" "「やっと着いたわね」"

    kosuke "「あっ！」"

    voice "audio/voice/op05/op05_0010.ogg"
    jordh 111 "「フッフッフッフッフ。罠とも知らず、追いかけられるままにここに来るとは、愚かね、川神幸介！」"

    kosuke "「罠！？」"

    voice "audio/voice/op05/op05_0011.ogg"
    jordh 113 "「ここが貴様の墓場となるのだ！」"

    $ fauna_name = _("女の子")

    voice "audio/voice/op05/op05_0012.ogg"
    fauna "「姉さん、それ、悪人のセリフ……」"

    hide jor
    show fau 103 at center
    with dissolve

    "声に振り向くと、さっきの女の子が立っていた。"

    kosuke "「お前は！」"

    voice "audio/voice/op05/op05_0013.ogg"
    fauna 109 "「…………」"

    hide fau
    show jor 102 at center
    with dissolve

    voice "audio/voice/op05/op05_0014.ogg"
    jordh "「さあ、観念なさい。女神二人を相手に勝てるはずは無いわ！」"

    kosuke "「女神？　まだそんなこと言ってるのか、この悪魔め！」"

    voice "audio/voice/op05/op05_0015.ogg"
    jordh 115 "「ふっ？　よ、よりにもよって私達が悪魔だと……？」"

    kosuke "「それに、お前たちの攻撃は今まで全部かわしてるぜ！　何をやっても無駄さ！」"

    voice "audio/voice/op05/op05_0016.ogg"
    jordh 103 "「かわしてるって、そりゃ魔王の力のお陰じゃないの」"

    kosuke "「魔王……？　何を言って……」"

    voice "audio/voice/op05/op05_0017.ogg"
    jordh 100 "「アンタは知らなくて良い事よ」"

    kosuke "「言っとくけどな、俺は人間でただの大学生だ！　女神だかなんだか知らねーけど、お前らに命を狙われる覚えは\nねーぞ！」"

    voice "audio/voice/op05/op05_0018.ogg"
    jordh 103 "「ふっ。ただの人間……？　だったら何でアンタここにいるのよ？」"

    kosuke "「え？」"

    voice "audio/voice/op05/op05_0019.ogg"
    jordh "「見たでしょう？　街の人間たちの様子を」"

    kosuke "「あ……」"
    kosuke "「あれはまさかお前たちが！」"

    voice "audio/voice/op05/op05_0020.ogg"
    jordh 100 "「そう。その子はね、時間を止めることができるの」"

    # TODO: ^effect,stop

    hide jor
    show fau 109 at center
    with dissolve

    kosuke "「時間を！？」"

    hide fau
    show jor 100 at center
    with dissolve

    voice "audio/voice/op05/op05_0021.ogg"
    jordh "「時を管理する女神だからね。そして、その時間操作によって影響を受けるのは、この人間界の生き物だけ……」"

    voice "audio/voice/op05/op05_0022.ogg"
    jordh 111 "「つまり、今この瞬間行動が可能なのは、神族と魔族だけなのよ！」"

    kosuke "「そんな……。じゃあ、俺は一体……！？」"

    voice "audio/voice/op05/op05_0023.ogg"
    fauna "「姉さん……そろそろ私、力が……」"

    voice "audio/voice/op05/op05_0024.ogg"
    jordh 109 "「あ、ごめんごめん。さっさと片付けるわ」"

    voice "audio/voice/op05/op05_0025.ogg"
    jordh 100 "「アンタ、私のマリアナ海溝より深い慈悲の心で、なるべく楽に死なせてあげるから」"

    kosuke "「死なない方に慈悲をかけてくれませんかねぇ……？」"

    show jor 114
    with dissolve

    # TODO: ^nature0,"魔法"
    # TODO: ^naturemotion0,"*wind4"

    voice "audio/voice/op05/op05_0026.ogg"
    jordh "『グラビティキャンセル。ヨルズの名において、鉄骨よ重力の呪縛を解き放て！』"

    hide jor
    with dissolve

    # TODO: ^nature0

    kosuke "「やっぱり聞いちゃいねえ！　……って、うわっ、何\nだ！？」"

    "工事現場に積まれた鉄骨が次々と宙を舞い、そのひとつがもの凄いスピードで俺を目指して飛んできた！"

    play sound "audio/sound/se199_2.ogg"

    scene white
    with ImageDissolve("images/wipe/08.png", 2)

    kosuke "「うおっ！？」"

    scene bg17c
    with dissolve

    "俺は瞬間的に体捌きでそれを避けた。同時に、鉄骨はド\nスンという重い音を立てて地面に突き刺さる。"

    # TODO: ^effect,Quake,500

    kosuke "「おっとっと……」"

    "大きな振動が起きた。"

    show jor 100 at center
    with dissolve

    voice "audio/voice/op05/op05_0027.ogg"
    jordh "「ふ〜ん。今のを避けるなんて、さっすがねー。フフフ、久々に本気を出せそうだわ！」"

    voice "audio/voice/op05/op05_0028.ogg"
    jordh 101 "「そ〜れ！　ものどの、かかれー！！」"

    hide jor
    with dissolve

    kosuke "「わっ！」"

    play sound "audio/sound/se199_2.ogg"

    scene white
    with ImageDissolve("images/wipe/08.png", 0.3)

    play sound "audio/sound/se116.ogg"

    # TODO: ^effect,Quake,1000

    "空中に浮いていた鉄骨が連続で俺に襲い来る。俺は必死に回避運動を行い、ひらひらと鉄骨をかわしていった。"

    scene bg17c
    with dissolve

    show jor 115 at center
    with dissolve

    voice "audio/voice/op05/op05_0029.ogg"
    jordh "「ちいっ！　その避け方、なんかムカつく！」"

    hide jor
    with dissolve

    "しかし、避けるスピードにだんだんと陰りが出てくる。"
    "疲労だ。"
    "体力の限界に達してきた。"
    "足も目も辛い。"

    kosuke "「（だめだ、このままじゃいつか……）」"

    show fau 110 at center
    with dissolve

    voice "audio/voice/op05/op05_0030.ogg"
    fauna "「〜〜〜っ！」"

    "気がつくと、もう一人の女神が近くにいた。"
    "この子はさっきから動いていない。……なぜ俺を襲ってこない？"

    voice "audio/voice/op05/op05_0031.ogg"
    jordh 115 "「ちょこまかと！」"

    voice "audio/voice/op05/op05_0032.ogg"
    jordh 102 "「もう怒った。これでラストにするわ！　でかいの行くからね！」"

    show fau 109

    "近くにいる女神と目が合った。"
    "瞬間、彼女を盾にすれば攻撃がやむのでは、と閃く。"

    voice "audio/voice/op05/op05_0033.ogg"
    jordh 114 "「この大きなガラス群で、その体、切り刻んでやる！」"

    "しかし、いくら自分が助かる為とはいえ、女の子を盾にするなんて、そんな卑怯な真似は俺にはできない。"
    "例えそれが、俺のことを殺そうとしている子だとして\nも……だ！"

    hide fau
    with dissolve

    show jor 114 at center

    # TODO: ^nature0,"魔法"

    voice "audio/voice/op05/op05_0034.ogg"
    jordh "「そーれ！　逝ってこい黄泉の国！」"

    # TODO: ^nature0

    kosuke "「わっ！　だっだめだ……あんなの避けられない……！」"

    hide jor
    show fau 109 at center
    with dissolve

    "顔をそらした瞬間、再び彼女の姿が目に入った。"
    "だめだ！　あの大きさじゃ、この子にも当たっちまう！"

    kosuke "「あぶない！」"

    stop music

    voice "audio/voice/op05/op05_0035.ogg"
    fauna 107 "「え……？」"

    "咄嗟の行動だった。危ないと思ったときには体が勝手に動いていた。"
    "俺の体は意志に反してその行動を拒んだ。しかし、俺は体を引き剥がす思いでその呪縛から抜け出し、彼女に体当たりをした。"

    play sound "audio/sound/se011.ogg"

    # TODO: ^effect,Quake,200

    hide fau

    "もんどりうちながら、彼女は吹っ飛ぶ。"


    "刹那、降ってきた大量のガラス板がぱんと弾け、そのガラス片が全て俺を襲って来た。"

    "降ってくるガラス片や尻餅をつく彼女が、スローモー\nションの映像のように見えた。"

    play sound "audio/sound/se095.ogg"

    # TODO: ^effect,Flash_$80FF0000,200

    "キラキラ輝くガラスを綺麗だと思った瞬間、体に鈍い衝撃が来た。"

    scene black
    with Dissolve(2)

    "俺は……"
    "ガラスの破片に、体をぐちゃぐちゃに切り刻まれた。"

    stop music

    scene white
    with Dissolve(2)

    "…………。"
    "…………死ぬ……のか……。"
    "痛みはもう感じない。苦しみも悲しみも、何も感じない。"
    "……このまま何もわからないまま死ぬのはイヤだけど……でもまあ、最後は男らしく、カッコ良く女の子を救ったんだ。それで良しとしようか……。"
    "ああでも……。"
    "せめてあのゲーム……プレイしたかったな……。はは\nは……。"
    "…………。"
    "ああ……なにか……手が温かい……。"
    "まるで、女神にでも握られてるみたいな……そんな気\n分……。"

    scene bg17
    with Dissolve(3)

    show fau 109 at right
    show jor 111 at left
    with dissolve

    $ jordh_name = _("ヨルズ")
    $ fauna_name = _("ファウナ")

    play music "audio/bgm/bgm17.ogg"

    voice "audio/voice/op05/op05_0036.ogg"
    jordh "「……もう、虫の息ね。放っておいてもこのまま死ぬでしょう」"

    voice "audio/voice/op05/op05_0037.ogg"
    fauna "「…………」"

    voice "audio/voice/op05/op05_0038.ogg"
    jordh "「帰ろう？　任務は無事終了したわ……」"

    voice "audio/voice/op05/op05_0039.ogg"
    fauna "「う、うん……」"

    play sound "audio/sound/se033.ogg"

    hide jor
    show fau 110 at center
    with dissolve

    voice "audio/voice/op05/op05_0040.ogg"
    fauna "「（どうして……？　どうして飛び出したりした\nの……？）」"

    voice "audio/voice/op05/op05_0041.ogg"
    fauna "「（そんなことをしなければ、まだ避けられたはずなの\nに……）」"

    voice "audio/voice/op05/op05_0042.ogg"
    fauna 105 "「（……死ななくて済んだのに……）」"

    voice "audio/voice/op05/op05_0043.ogg"
    fauna "「（彼はわたしを救おうとしたの……？）」"

    voice "audio/voice/op05/op05_0044.ogg"
    fauna "「（わたしは姉さんのバリアに守られていたから当たっても平気だった。けど、彼はそんなことを知らずに、わたしを救うために飛び出した……）」"

    voice "audio/voice/op05/op05_0045.ogg"
    fauna 109 "「（どうして……？）」"

    voice "audio/voice/op05/op05_0046.ogg"
    fauna "「（どうしてそんなことができるの……？）」"

    voice "audio/voice/op05/op05_0047.ogg"
    fauna "「（限りある命なのに……）」"

    voice "audio/voice/op05/op05_0048.ogg"
    fauna 105 "「（死んだらお終いの命なのに……）」"

    voice "audio/voice/op05/op05_0049.ogg"
    fauna "「（それでも、他人を救おうとしたの……？）」"

    voice "audio/voice/op05/op05_0050.ogg"
    fauna 110 "「（さっきもそうだった……。彼は猫を助けた。今と同じく、自己犠牲によって……）」"

    voice "audio/voice/op05/op05_0051.ogg"
    fauna "「（街中で攻撃したときも、きっと周りに被害を与えたくないから、人のいない所に走って行ったんだわ……）」"

    voice "audio/voice/op05/op05_0052.ogg"
    fauna 109 "「（人間は自分の事しか考えない下等な生き物ではなかったの……？）」"

    voice "audio/voice/op05/op05_0053.ogg"
    fauna "「（他人の命を奪ってまで生きようとするんじゃない\nの……？）」"

    voice "audio/voice/op05/op05_0054.ogg"
    fauna "「（わたしはそう教わってきた……。なのに彼は違っ\nた……）」"

    voice "audio/voice/op05/op05_0055.ogg"
    fauna 110 "「（大神様……彼は……彼は本当に今死すべき人間なのでしょうか……）」"

    voice "audio/voice/op05/op05_0056.ogg"
    fauna "「（ここで終わらせて良い命なのでしょうか……）」"

    show fau 110 at right
    show jor 103 at left
    with dissolve

    voice "audio/voice/op05/op05_0057.ogg"
    jordh "「……もう手を離してあげなよ。そこにいると辛くなるよ」"

    voice "audio/voice/op05/op05_0058.ogg"
    fauna 105 "「…………」"

    voice "audio/voice/op05/op05_0059.ogg"
    jordh 111 "「ねえ、行こうよ。時間も動き始めてるんだ。人が来る」"

    voice "audio/voice/op05/op05_0060.ogg"
    fauna "「……わからないの……」"

    voice "audio/voice/op05/op05_0061.ogg"
    jordh "「え？」"

    voice "audio/voice/op05/op05_0062.ogg"
    fauna "「わたしたちのしたことは、本当に正しいことなの？」"

    voice "audio/voice/op05/op05_0063.ogg"
    jordh 111 "「それは……。だって、こうしなかったら、もっと多くの、何万何億という命が消滅してしまうのよ？」"

    voice "audio/voice/op05/op05_0064.ogg"
    fauna 109 "「そうだけど……」"

    voice "audio/voice/op05/op05_0065.ogg"
    fauna 105 "「それでもわたしは……。わたしの本心は、彼を守りたかったの……」"

    voice "audio/voice/op05/op05_0066.ogg"
    jordh 103 "「ファウナ……」"

    voice "audio/voice/op05/op05_0067.ogg"
    fauna "「命の尊さを知っている彼を……、他人を思いやり、守る勇気を持つ彼を、わたしたちは殺めてしまった……」"

    voice "audio/voice/op05/op05_0068.ogg"
    jordh 110 "「違うよ。彼を殺したのは私。だから、ファウナが気にする必要はない」"

    voice "audio/voice/op05/op05_0069.ogg"
    fauna 110 "「……姉さんはいつもそう。わたしの代わりに、辛い役を引き受ける……」"

    voice "audio/voice/op05/op05_0070.ogg"
    jordh 109 "「いや、それは……その……」"

    voice "audio/voice/op05/op05_0071.ogg"
    fauna 102 "「……。決めた」"

    voice "audio/voice/op05/op05_0072.ogg"
    jordh 107 "「え？」"

    voice "audio/voice/op05/op05_0073.ogg"
    fauna "「わたしの生命を、彼に分け与えます」"

    voice "audio/voice/op05/op05_0074.ogg"
    jordh 109 "「ばっ……！　何を言いだすのよこの子は！　そんなの、人間に対して行ったら重罪になるのよ！？」"

    voice "audio/voice/op05/op05_0075.ogg"
    fauna 111 "「構わないわ。わたしは、彼を死なせたくない。例え、天界に背くことになったとしても！」"

    voice "audio/voice/op05/op05_0076.ogg"
    jordh "「ファウナ落ち着いて！　そんなことをしたって何にもならないわ！？　今助かったとしても、また誰かが彼を殺しに来るのよ？」"

    voice "audio/voice/op05/op05_0077.ogg"
    fauna 102 "「そのときは……わたしが彼を守ります」"

    voice "audio/voice/op05/op05_0078.ogg"
    jordh 108 "「ファウナ……！」"

    voice "audio/voice/op05/op05_0079.ogg"
    jordh 111 "「命令よ。やめなさい！　一時の感情に流されないで。彼が生きてたら後々皆が困るのよ！？」"

    voice "audio/voice/op05/op05_0080.ogg"
    fauna 111 "「大丈夫よ。時が経てばきっと、彼を魔王化させない方法だって見つかるわ」"

    voice "audio/voice/op05/op05_0081.ogg"
    jordh 110 "「ファウナ……」"

    voice "audio/voice/op05/op05_0082.ogg"
    fauna "「姉さん、お願い。我がままなのはわかってる。大神様\nを……天界を裏切ることになるのもわかってる」"

    voice "audio/voice/op05/op05_0083.ogg"
    fauna 111 "「だけど、わたしはわたしの思った通りにしてみたい。わたしは彼を……この人を救いたいの……！」"

    voice "audio/voice/op05/op05_0084.ogg"
    jordh 111 "「…………」"

    voice "audio/voice/op05/op05_0085.ogg"
    fauna "「手伝ってとは言わないから、今だけわたしのすることを見逃して！　お願い！」"

    voice "audio/voice/op05/op05_0086.ogg"
    jordh "「…………」"

    stop music

    voice "audio/voice/op05/op05_0087.ogg"
    jordh 100 "「わかった」"

    voice "audio/voice/op05/op05_0088.ogg"
    fauna 100 "「じゃあ……」"

    play music "audio/bgm/bgm04.ogg"

    voice "audio/voice/op05/op05_0089.ogg"
    jordh 111 "「わたしも協力する」"

    voice "audio/voice/op05/op05_0090.ogg"
    fauna 107 "「え……？」"

    voice "audio/voice/op05/op05_0091.ogg"
    jordh 100 "「確かに、こいつは他の人間とはちょっと違うみたいだ\nもんね」"

    voice "audio/voice/op05/op05_0092.ogg"
    fauna 112 "「ヨルズ……」"

    voice "audio/voice/op05/op05_0093.ogg"
    jordh "「さあ、そうと決まったら、ちゃっちゃとやっちゃいま\nしょ？　まだ息があるうちに！」"

    voice "audio/voice/op05/op05_0094.ogg"
    fauna 105 "「……姉さん、ありがとう」"

    voice "audio/voice/op05/op05_0095.ogg"
    jordh "「まったく、困った妹だよ、アンタは」"

    voice "audio/voice/op05/op05_0096.ogg"
    fauna 105 "「うん……。ぐすっ。ごめんね……」"

    voice "audio/voice/op05/op05_0097.ogg"
    jordh "「ほら、泣いてちゃ術が失敗するよ」"

    voice "audio/voice/op05/op05_0098.ogg"
    fauna 112 "「うん……！」"

    show jor 114 at midleft

    voice "audio/voice/op05/op05_0099.ogg"
    jordh "「いくわよ？　方陣形成。特殊陣形パターン２２６。生命管理センターへのアクセス開始」"

    show fau 115 at midright

    voice "audio/voice/op05/op05_0100.ogg"
    fauna 115 "『生きとし生けるもの全ての命運を司りし生命の樹よ、我が命を彼の者に分け与え、彼を救いたまえ。我が名はファウナ。彼の者は川神幸介……！』"

    play sound "audio/sound/se058.ogg"
    stop music

    scene white
    with Dissolve(1)

    scene black
    with Dissolve(3)

    $ renpy.movie_cutscene("images/op_movie.mpg")

    jump op07
