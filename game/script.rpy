# This is the main script that sets up common variables and also handles routes

define g_FauFlg = 0
define g_JorFlg = 0
define g_LeuFlg = 0
define g_KloFlg = 0

define g_Day = 0

# Characters
define kosuke = Character(_("幸介"))
define fauna = DynamicCharacter("fauna_name", image="fau")
define fauna_name = _("ファウナ")
define jordh = DynamicCharacter("jordh_name", image="jor")
define jordh_name = _("ヨルズ")
define ogami = DynamicCharacter("ogami_name", image="oga")
define ogami_name = _("大神様")
define lea = DynamicCharacter("lea_name", image="leu")
define lea_name = _("レア")
define klotho = DynamicCharacter("klotho_name", image="kur")
define klotho_name = _("クロト")

image white = "#ffffff"

transform midleft:
    xanchor 0.5 xpos 0.25

transform midright:
    xanchor 0.5 xpos 0.75

init python:
    config.side_image_only_not_showing = True
    config.say_attribute_transition = Dissolve(0.5)


label splashscreen:
    image logo = "splash/logo.png"
    image caution = "splash/caution.png"

    scene black
    with Pause(1)

    show logo with Dissolve(1)
    play sound "splash/logo.ogg"
    with Pause(3)
    hide logo with Dissolve(1)

    show caution with Dissolve(1)
    with Pause(3)
    hide caution with Dissolve(1)

    return


label start:
    if g_FauFlg == 5:
        jump fau01

    if g_JorFlg == 5:
        jump jor01

    if g_LeuFlg == 5:
        jump lea1

    if g_KloFlg == 5:
        jump kur01

    if g_Day == 1:
        jump in_01

    if g_Day == 2:
        jump mor1

    if g_Day == 3:
        jump in_02

    if g_Day == 4:
        jump com02

    if g_Day == 5:
        jump in_03

    if g_Day == 6:
        jump mor4

    if g_Day == 7:
        jump badend

    jump op01
