define l = Character("Louli", color="#6AA0F2")
define m = Character("Worgaros", color="#ffc9c9")
define i = Character("Meylo", color="#E5FB46")
define s = Character("Saphia", color="#6AA0F2")
define heros = Character("[nomduheros]", color="#6AA0F2")

screen logocarte:
    imagebutton:
        xpos 1150
        ypos 20
        idle "gui/objetcarte.png"
        hover "gui/objetcarte1.png"
        at carte_zoom
        action Jump("carte")

screen localisation:
    imagebutton:
        xpos 120
        ypos 400
        idle "gui/rondchambre.png"
        hover "gui/rondchambre1.png"
        at bouton_zoom

        action Jump("chambre")

    imagebutton:
        xpos 0.5
        ypos 500
        idle "gui/rondmagasin.png"
        hover "gui/rondmagasin1.png"
        at bouton_zoom
        action Jump("magasin")




transform carte_zoom:
    zoom 0.3

transform bouton_zoom:
    zoom 0.3

label start:

    play music "audio/musiqueintro.ogg"
    scene decorintroduction
    with fade
    show femme_intro at center
    with zoomin

    s "( Tien voici peut être enfin le héros enfin attendu )"
    with dissolve


    show femme_intro2 at center
    s "Laisse moi te raconter le début d'une histoire."
    hide femme_intro2 at center
    with dissolve


    show femme_intro3 at center
    s "Mais avant de commencer, tu as un choix à faire. Veut tu te lancer dans l'aventure ?"
    with dissolve








    menu:

        "Non merci !":
            jump non
        "Oui allons y.":
            jump oui



label non:

        show femme_intro_fin_non at center
        s "Trés bien je prend note ! Aurevoir !"
        return


label oui:

        show femme_intro_fin_oui at center
        s "Super alors allons y pour une toute nouvelle aventure !"
        with dissolve

label suite:

        scene decorintroduction
        with slideleft
        s "Sois le bienvenue dans la ville de licorne City. Un endroit remplis de suprise."




        show herodebut at center
        with moveinleft


        s "Mais avant tout quel est ton nom ?"

        $ nomduheros = renpy.input("Entre un nom.")
        $ nomduheros = nomduheros.strip()

        if not nomduheros:
            $ nomduheros = "Adrien"

        s "Votre nom est [nomduheros] ?"



        heros "Oui."


        s "Parfait maintenant clique sur la map et commence a visiter Licorne City"

        m "C'est partie !"


        m "Je dois cliquer sur la carte"
        call screen logocarte






label carte:

        play music "sons/ambiancerue.ogg"
        scene carte
        call screen localisation
        pause

label chambre :
        stop music
        scene chambre
        show herodebut at right
        m "Whouaaaa."
        m "Je me demande si il ya de quoi me changer dans le placard."


        call screen logocarte

label magasin :
        scene magasin
        show herodebut at left
        m "Mais didonc c'est magnifque."
        call screen logocarte



        pause
