label prologue:
    scene bg classroom at bg_fit
    with fade

    narrator "Midterm results day."
    narrator "The list goes up at 8:47 AM."
    narrator "You don't run to check it."
    narrator "You already know."

    show mcneutral at center_char
    with dissolve

    narrator "You've always known."
    narrator "That's the thing nobody understands about you."
    narrator "You don't panic before results."

    thought "Riya got 91 last time, she studied harder this time. Probably 93 now."
    thought "Kabir stopped taking notes in week three. Drop of at least four marks now."
    thought "Orion Hale."
    thought "..."
    thought "Don't think about Orion Hale."

    hide mcneutral
    with dissolve

    scene bg classroom at bg_fit
    with dissolve

    show mcneutral at center_char
    with dissolve

    narrator "Rank 2. Again."
    narrator "And above you."
    narrator "Same name."
    narrator "It always has been."
    narrator "The gap this time?"
    narrator "0.1 marks."

    narrator "You stand there for exactly three seconds."
    narrator "Then you smile."
    narrator "Because someone is watching."
    narrator "And you know how to look like someone who doesn't care."

    hide mcneutral
    show mcsmile at center_char

    mc "..."

    narrator "The smile costs nothing."
    narrator "You've been practicing it since you were eleven."

    hide mcsmile
    with dissolve

    scene bg classroom at bg_fit
    with dissolve

    show mcneutral at center_char
    with dissolve

    narrator "You're stuffing your paper into your bag when you hear footsteps beside you."

    hide mcneutral
    with dissolve

    show orioncalmtalk at center_char
    with dissolve

    orion "Hey."

    hide orioncalmtalk
    with dissolve

    show mctalk at center_char
    with dissolve

    mc "What."

    hide mctalk

    narrator "He holds out your paper."
    narrator "Question 3."
    narrator "Red ink."
    narrator "Half mark deducted."

    show mctalk at center_char

    mc "I got the right answer."

    hide mctalk

    show orioncalmtalk at center_char

    orion "You got {i}an{/i} answer."

    hide orioncalmtalk

    show mctalk at center_char

    mc "Same thing."

    hide mctalk

    show orioncalmtalk at center_char

    orion "No. It's not."

    hide orioncalmtalk

    show mctalk at center_char

    narrator "You look at him properly for the first time in years."
    narrator "He's not gloating."
    narrator "And that's the part that bothers you."

    hide mctalk

    menu:
        "What's your problem? You already won.":
            $ respect -= 1
            jump rival_explains_sharp
        "...Show me.":
            $ respect += 1
            jump rival_explains_calm


label rival_explains_sharp:

    show mctalk at center_char
    with dissolve

    mc "What's your problem? You already won."

    hide mctalk

    show orioncalmtalk at center_char

    orion "My problem is that you were {i}right{/i} and still lost marks."
    orion "That should bother you more than it bothers me."

    hide orioncalmtalk

    show mcneutral at center_char

    narrator "It does bother you."
    narrator "More than he will ever know."
    narrator "But you don't say that."
    narrator "You never say that."

    hide mcneutral

    show mctalk at center_char

    mc "I'll live."

    hide mctalk

    show orioncalmtalk at center_char

    orion "You mean you'll lose."
    orion "That's different."

    hide orioncalmtalk

    show mctalk at center_char

    mc "Aww~ You're worried about me?"
    mc "I'm flattered."
    mc "Don't tell me you have feelings for me now?"

    hide mctalk

    show oriondisturbed at center_char

    narrator "He stares at you."
    narrator "You stare back."
    narrator "Neither of you blinks."

    hide oriondisturbed

    jump rival_explains_calm


label rival_explains_calm:

    show orioncalmtalk at center_char
    with dissolve

    orion "Look at your answer."
    orion "You wrote 2.5 times 10 to the power of 3."
    orion "The data had three significant figures."

    hide orioncalmtalk

    show mctalk at center_char

    mc "The value is identical."

    hide mctalk

    show orioncalmtalk at center_char

    orion "The information isn't."

    hide orioncalmtalk

    show mcneutral at center_char

    thought "I hope he trips on his huge ego."

    hide mcneutral

    jump library_scene


label library_scene:

    scene bg library at bg_fit
    with dissolve

    show mcneutral at center_char
    with dissolve

    narrator "It becomes a thing."
    narrator "After school, library."
    narrator "His notes and your questions."

    thought "This is strategic."
    thought "He's the only person in this school whose study methods are worth reverse engineering."
    thought "This is my strategy."

    narrator "You open the notebook to a fresh page."
    narrator "The left side is Physics."
    narrator "The right side..."
    narrator "You close it before he can see."

    hide mcneutral
    with dissolve

    show orionneutral at center_char
    with dissolve

    thought "Orion Hale."
    thought "Taps pencil when emotionally irritated."
    thought "Avoids eye contact when complimented."
    thought "Smiles after correcting someone — but not today."
    thought "Doesn't react to praise. Probably hears it too often."
    thought "Asks questions he already knows the answer to."

    hide orionneutral

    show orioncalmtalk at center_char

    orion "You're not writing."

    hide orioncalmtalk

    show mctalk at center_char

    mc "I'm thinking."

    hide mctalk

    show orioncalmtalk at center_char

    orion "About Physics?"

    hide orioncalmtalk

    show mctalk at center_char

    mc "Obviously."

    hide mctalk

    show orionneutral at center_char

    narrator "He looks at you for one second longer than necessary."
    narrator "Then looks back at his page."

    hide orionneutral

    

    jump chapter_one
