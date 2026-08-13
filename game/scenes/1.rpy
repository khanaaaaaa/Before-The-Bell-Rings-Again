label prologue:
    scene bg classroom

    narrator "Midterm results day."
    narrator "The list goes up at 8:47 AM."
    narrator "You don't run to check it."
    narrator "You already know."

    narrator "You've always known."
    narrator "That's the thing nobody understands about you."
    narrator "You don't panic before results."

    thought "Riya got 91 last time. She studied harder this term. Probably 93."
    thought "Kabir stopped taking notes in week three. Drop of at least four marks."
    show orionquiet at center_char
    thought "Orion Hale."
    thought "..."
    thought "Don't think about Orion Hale."
    hide orionquiet

    scene bg results_board

    narrator "Rank 2. Again."
    narrator "And above you, same name."
    narrator "It always has been."
    narrator "The gap this time: 0.1 marks."

    narrator "You stand there for exactly three seconds."
    narrator "Then you smile."
    narrator "Because someone is watching."
    narrator "And you know how to look like someone who doesn't care."

    narrator "The smile costs nothing."
    narrator "You've been practicing it since you were eleven."

    narrator "Somewhere behind you, you hear him."
    narrator "Already walking away."

    thought "He doesn't need to look."
    thought "He already knew too."

    scene bg classroom with dissolve

    narrator "You're stuffing your paper into your bag when footsteps stop beside you."
    narrator "You don't look up."
    narrator "You know the sound of his footsteps."
    narrator "You hate that you know the sound of his footsteps."

    show orionhappytalk at center_char

    orion "Hey."
    hide orionhappytalk
    show orionsmilequiet at center_char

    mc "What."

    narrator "He holds out your paper."
    narrator "Question 3, half mark deducted."
    narrator "He's not holding out his own paper."
    narrator "Just yours."

    mc "I got the right answer."

    hide orionsmilequiet
    show orionsmiletalk at center_char

    orion "You got {i}an{/i} answer."

    hide orionsmiletalk
    show orionsmilequiet at center_char

    mc "Same thing."

    hide orionsmilequiet
    show orionsmiletalk at center_char

    orion "No, it's not."

    hide orionsmiletalk
    show orionsmilequiet at center_char

    narrator "You look at him properly for the first time in years."
    narrator "He's not gloating."
    narrator "He's not even looking at you like you're competition."
    narrator "He's looking at you like you're a problem he wants you to solve yourself."
    narrator "That's the part that bothers you."

    menu:
        "What's your problem? You already won.":
            $ respect -= 1
            jump rival_explains_sharp
        "...Show me.":
            $ respect += 1
            jump rival_explains_calm

label rival_explains_sharp:

    hide orionsmilequiet 
    show orionsmiletalk at center_char

    orion "My problem is that you were {i}right{/i} and still lost marks."
    orion "That should bother you more than it bothers me."

    hide orionsmiletalk
    show orionsmilequiet at center_char

    narrator "It does bother you."
    narrator "More than he will ever know."
    narrator "But you don't say that."
    narrator "You never say that."

    mc "I'll live."

    hide orionsmilequiet
    show orionsmiletalk at center_char

    orion "Losing and living aren't the same thing."

    hide orionsmiletalk
    show orionsmilequiet at center_char

    narrator "You stare at him."

    hide orionsmilequiet
    show orionsmiletalk at center_char

    mc "Aww. You're worried about me?"

    hide orionsmiletalk
    show orionsmilequiet at center_char

    narrator "He doesn't react to that."
    narrator "Not even a flicker."
    narrator "He just looks at you like he's waiting for you to stop performing."
    narrator "Then he puts your paper down on the desk and walks away."

    hide orionsmilequiet

    thought "I hate that he didn't take the bait."
    thought "I had three more lines ready."
    thought "He didn't even give me the argument."

    jump library_scene

label rival_explains_calm:

    show orionangrytalk at right

    orion "Look at your answer."
    orion "You wrote 2.5 times 10 to the power of 3."
    orion "The data had three significant figures."

    hide orionangrytalk
    show orionquiet at center_char

    mc "The value is identical."

    hide orionquiet
    show orionhappytalk at center_char

    orion "The information isn't."

    hide orionhappytalk

    narrator "He says it quietly."
    narrator "Like a fact he's sorry about."

    thought "I hope he trips on his huge ego."
    thought "I hope he trips and his notebook falls open and everyone sees whatever he writes in the margins."
    thought "I hope it's embarrassing."
    thought "It won't be."
    thought "Nothing about him is embarrassing."
    thought "That's the most irritating thing about him."

    jump library_scene

label library_scene:
    scene bg library

    show orionquiet at center_char

    narrator "It becomes a thing."
    narrator "After school. Library."
    narrator "His notes and your questions."

    thought "This is strategic."
    thought "He's the only person in this school whose methods are worth reverse engineering."
    thought "This is my strategy."
    thought "I'm allowed to have a strategy."

    narrator "You open your notebook to a fresh page."
    narrator "The left side is Physics."
    narrator "The right side..."
    narrator "You close it before he can see."

    thought "Orion Hale."
    thought "Taps pencil when emotionally irritated."
    thought "Avoids eye contact when complimented."
    thought "Smiles after correcting someone — but not today."
    thought "Doesn't react to praise. Hears it too often."
    thought "Asks questions he already knows the answer to."
    thought "Sat down without asking if the seat was taken."
    thought "Hasn't looked at me once since we got here."
    thought "Is absolutely aware I'm watching him."

    narrator "He turns a page."
    narrator "Doesn't look up."

    hide orionquiet
    show orionhappytalk at center_char

    orion "You're not writing."

    hide orionhappytalk
    show orionquiet at center_char

    mc "I'm thinking."

    hide orionquiet
    show orionhappytalk at center_char

    orion "About Physics?"

    hide orionhappytalk
    show orionsmilequiet at center_char

    narrator "A beat."

    mc "Obviously."

    narrator "He looks at you for one second longer than necessary."
    narrator "Then he looks back at his page."
    narrator "He already knew the answer."
    hide orionsmilequiet

    jump chapter_one

