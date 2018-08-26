# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Allura")
define l = Character("Lance")
define k = Character("Keith")
define p = Character("Pidge")
define d = Character("Daniel")
define b = Character("Larmina")
define h = Character("Hunk")
define v = Character("Vince")
define c = Character("Coran")
define w = Character("Wade")
define vol = Character("Voltron")
define incel = Character("Lotor")
define waifu = Character("Merla")
define i = Character("[name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg logo
    with fade
    play music "vftheme.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show daniel fullbod_gonnakillu at right with zoomin

    # These display lines of dialogue.

    d "So you've decided to play Voltron Force Romance Sim. Awesome!"

    d "Make sure you play with integrity and stuff, or I'll eat your skin."

    $ name = renpy.input("Now, what's your name, Cadet?")
    $ name = name.strip()


    scene bg space
    with fade
    play music "voltaic.mp3"

    i "The universe is safe again, thanks to the heroic efforts of Voltron and its crew. But for
    how long?"
    "Haggar has been discovered to be alive, and still scheming with Lotor.
    And for whatever reason, I'm the only one who seems to be able to resist her powerful new
    sorcery, a consequence of her formation of the neo-haggarium radioactive isotope..."
    "Could it be that my biological parents, who I never met, were descended from her people?"
    "I don't know, but one thing is for certain- I need to work alongside the Voltron Force to
    protect this fragile new peace. Not that I mind... they're pretty cool."
    "And who knows? I might even get a date..."

    #affection begin
    $ a_aff = 0
    $ l_aff = 0
    $ k_aff = 0
    $ h_aff = 0
    $ p_aff = 0
    $ b_aff = 0
    $ v_aff = 0
    $ d_aff = 0
    $ c_aff = 0

    scene bg hallofkings
    with fade
    show allura fullbod_happy at right

    a "I'm so glad that destiny led to you being present at that battle in Neoaustin, [name]! If you hadn't
    been there to throw off Haggar, we'd be in deep trouble. And I am sorry that you have to leave
    college to work with us in this time of crisis- I'm sure you'd rather be in class than dealing
    with a witch."
    i "It's fine, your highness. This is more important than some lecture, anyways."
    a "True, this is essential to the future of all Alliance planets. Still, I appreciate how
    accomodating you're being. Come, let's go talk to the others."

    scene bg lionchutes
    with fade
    show allura fullbod_happy at right
    show keith fullbod_unhappy at left

    a "Oh, Keith! Do you know where everyone is? I realized that we've never formally introduced [name]
    as a member of the team."

    k "Are you sure about this, Allura? No offense, [name], I appreciate your help at Neoaustin, but...
    becoming a member of the Voltron Force isn't something to be taken lightly. You might not be ready for it."

    a "We took on the cadets on the whim of destiny, and destiny has brought [name] here as well.
    Don't be so hesitant, Keith."

    k "Well... we'll see how things turn out."

    hide keith with dissolve

    a "Sorry about him, [name]. He's the paranoid sort."

    menu:

        "It's okay. ":
            jump ok
        "Maybe... maybe he's right.":
            jump sad
        "He seems rude.":
            jump angry

    label ok:

        a "He'll warm up to you in time. For now, let's go check the hangar for the others."
        jump after



    label sad:
        $ a_aff +=5
        a "Don't worry, [name]! I have the utmost faith in you. Come, now. Let's go see the rest of the team."
        jump after


    label angry:

        show lance fullbod_unhappy at left

        $ l_aff +=5

        l "Tell me about it. He's a self absorbed piece of-"
        a "Lance... did you two have a fight again?"
        l "Not my fault! He's been like this ever since that last battle with Haggar. It's like he can't handle
        knowing all our old tricks aren't gonna work against her, so he takes it out on us."
        a "Well, with [name] on our side, things will turn around!"
        l "I sure hope so."
        a "Lance, do you know where the rest of the team is? I want to formally introduce [name]."
        l "They're in the hangar washing the lions. I just came out to punch some doors after Keith came and whined about how we
        weren't working hard enough or whatever. I need a drink."

        hide lance fullbod_unhappy

        a "Well... anyways, let's go see the crew!"
        jump after

    label after:
    "Allura takes you to the hangar."


    scene bg hangar with fade

    show team happy at left

    l "Well, we're all here. It's good to have you on board, [name]."
    i "Likewise."
    h "Well, we want you to feel at home here. We're all pretty different, but we're still friends!"
    l "I just wish the cadets hadn't run off before you came in."
    h "Why do you still call them cadets? They're, like, twenty by now. They must be officers, at least."
    l "I never promoted them. I like calling them cadets."
    h "Uh, okay, Lance. Whatever makes you happy."
    p "I'm looking forward to studying your unique ability to deflect neo-haggarium's radioactivity, [name].
    Maybe we can figure out how to channel that ability into Voltron."
    a "Now, let's not overwhelm our newest team member! [name], since you've just arrived, what would you like to do?"
    menu:
        "Can you show me around the castle?":
            jump allura_tour
        "I'd like to explore the castle on my own.":
            jump alone
        "I'm going to go outside for a bit.":
            jump outside


    label allura_tour:
        $ a_aff +=5
        a "I'd love to show you around! There's so much history in the castle of lions. Perhaps we'll even see the space mice!"
        jump tour

    label alone:
        a "Of course. If you get lost, just follow the mice."
        i "Ah... of course."
        jump solo

    label outside:
        k "There's a courtyard just next to here. It's a good thinking spot."
        i "Cool, I'll go check it out."
        jump court

    label tour:
    scene bg hallofkings with fade
    show allura fullbod_happy at right
    a "You've seen this room on your way in, but I never explained its significance."
    a "This is the Hall of Kings, where the Arusian leaders of the past are commemorated."
    a "These are my forefathers... I only hope to do their legacy justice."

    show coran thinking at left

    c "Princess, I just- Oh, hello. Who is this?"
    a "This is [name]. I was just giving the official tour!"
    c "In that case, I won't interrupt. Pleasure to make your acquaintance, [name]."
    a "The same to you!"

    hide coran thinking with dissolve

    a "Next, let me show you the classroom. You might not be going to college any time soon, but the junior pilots
    are taking time off from the lions to do some studying to better have the knowledge to defeat Haggar, so perhaps you can join them!"

label classroomscene:

    scene bg classroom with fade
    show allura pleased at right

    a "Here we are! It's small, but suits our purposes quite well. We also keep some books in here that you might find interesting."

    scene bg lionchutes with fade
    show allura unhappy at right

    a "This is where we jump down chutes to enter our lions. To be honest, it wasn't the best design choice,
    since any malfunction means near-certain death."



    label solo:
    scene bg hallofkings

    i "Huh. This is full of paintings I didn't have time to look closely at before..."
    " These must be Allura's relatives. These look expensive, and bougie. Not sure I like this whole monarchy system they've got here."

    show coran thinking at right

    c "Oh, hello- I don't believe we've met."
    i "I'm [name]. I'm new here. Who are you?"
    c "I am Coran, ambassador of Arus. It's very nice to meet you."

    menu:
        "What's this room?":
            jump coranfacts

        "I like your moustache.":
            jump coranflattered

        "I need to go now.":
            jump coranok



label coranfacts:
    c "This is the Hall of Kings, where we keep portraits of the former leaders of Arus."
    c "I'd love to tell you more, but I really must inform the Princess of some diplomatic messages. I hope to see you again soon."

    hide coran with fade

    i "He seems nice. I'll go check out the next room."

    jump court

label coranflattered:
    $ c_aff += 10

    c "Oh, why, thank you! And I was worried that it was too old-fashioned..."
    c "I need to go speak to the Princess, but... let me know if you'd ever like to know more about the castle. I'd be happy to show you around."

    hide coran with fade

    i "He seems nice. I'll go check out the next room."

    jump court

label coranok:

    c "Very well, I must go speak to the Princess anyhow. I hope to see you around."

    jump court

label court:
    scene bg courtyard
    show larmina ok at left

    b "Hey, you're the new team member! What are you doing here in the courtyard?"

    menu:

        "I'm getting some fresh air.":

            b "Oh, cool."
            b "Well, I'm gonna go hit the gym. Catch ya later."

        hide larmina ok with dissolve


        "I wanted to find some fun.":

            b "Well... I can show you some parts of the castle Allura won't, if you promise not to tell."

            menu:

                "Sounds cool, I'm in!":

                    $b_aff +=10

                    b "Okay, well, me and Vince and Daniel have this hideout called the Den. We still use it sometimes.
                    The only other person who knows about it is Hunk. Come on, I'll show you."

                    jump theden

                "No thanks.":

                    b "Pfft, square."

                    hide larmina ok with dissolve

                    i "I guess she's the rebellious niece Allura told me about."

                    jump dinner

        label theden:

            scene bg den with fade

            show cadets

            i "Hey, Vince, Daniel! This is [name]."
            d "'Sup."
            v "Hi!"



        label dinner:
            show bg lionchutes with fade

            h "I'm making quesadillas for dinner."

            menu:
                "Offer to help":
                    i "I can help out in the kitchen, Hunk."
                    $ h_aff +=10
                    h "Oh, thanks, [name]! That'd be great."
                    scene bg kitchen
                    show hunk face_happy with fade
                    h "Okay, let's see what we'll need... some cheese, tortillas, pintos refritos, and salsa."
                    i "I can grate the cheese."
                    h "Awesome. I'll make the salsa in the meantime."

                "Go to the table":
                    "you sit down and wait for dinner to be served."

                    show keith confused at right

                    k "Mind if I sit next to you?"
                    i "It's fine."
                    k "Sorry about what I said earlier. Allura is right- you're here for a reason, probably.
                    Let me know if you want to do any combat training, that's mostly my department."
                    i "Thanks, but... I would have guessed that was more Lance's thing."
                    k "Pfft, if you want to fight like a gangster, maybe. He doesn't exactly abide by the code of honour that I do..."

                    show lance danger at left

                    "Lance sits on the other side of you without asking."

                    l "Oh, so you're saying my guerilla tactics, that have saved all our asses countless times, are a BAD thing,
                    just because they don't follow some make-believe chivalry crap you made up?"
                    l "'Cause last time I checked, Haggar and Lotor don't follow those stupid rules."
                    k "Calm down, Lance, I'm just telling [name]-"
                    l "You're just spreading dirt about me is what you're doing! [name], why don't YOU choose whose
                    fighting tactics you want to study?"
                    menu:
                        "Choose Lance":
                            i"I think Lance is right about not playing by the rules, Keith... Haggar doesn't have a code of honour."
                            k "Suit yourself. Just... maybe don't pick up on Lance's [i]other[/i] habits while you're learning to fight."
                            i "Hey, what's that supposed to-"
                            a "[b]BOYS![/b]"
                            "With that interference, Keith and Lance move on to more relaxed banter... you notice Lance sneaking a grin
                            at you while dinner is being eaten."

                        "Choose Keith":
                            i "I think Keith is right. Just because Haggar isn't honourable doesn't mean the Voltron Force should stoop to her level."
                            l "Ugh, it's like I'm seeing double. Well, don't expect me to bail you guys out when the Drule don't go along with your moral convictions."
                            k "At least we [i]have[/i] some moral convi-"
                            a "[b]BOYS![/b]"
                            "With that interference, Keith and Lance move on to more relaxed banter... you notice Keith looking appraisingly
                            at you while dinner is being eaten. Was that... a smile you saw?"




        label evening:

            i "What a busy day! I can't wait for tomorrow."
