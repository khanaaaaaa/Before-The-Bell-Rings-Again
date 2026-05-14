label prologue:
    scene bg classroom

    narrator "Midterm results day."
    narrator "The list goes up at 8: 47 AM."
    narrator "You don't run to check it."
    narrator "You already know"

    narrator "You've always known."
    narrator "That's the thing nobody understands about you."
    narrator "You don't panic before results."

    thought "Riya got 91 last time, she studied harder this time. Probably 93 now."
    thought "Kabir stopped taking notes in week three. Drp of atleast four marks now."
    thought "Orion Hale."
    thought "..."
    thought "Don't think about Orion Hale."

    scene bg results_board

    narrator "Rank 2. Again."
    narrator "And above you."
    narrator "Same name."
    narrator "It always has been."
    narrator "The gap this time?"
    narrator "0.1 marks."

    narrator "You stand there for exactly three seconds."
    narrator "Then you smile."
    narrator "Because someone in watching."
    narrator "And you know how to look like someone who doesn't care."

    mc "..."

    narator "The smile costs nothing."
    narrator "You've been practicing it since you were eleven."

    scene bg classroom with dissolve

    narrator "You're stuffing your paper into your bag when you hear footsteps beside you."

    orion "Hey!"

    mc "What."

    narrator "He holds out your paper."
    narrator "Question 3."
    narrator "Red ink."
    narrator "Half mark deducted."

    mc "I got the right answer."

    orion "You got {i}an{/i} answer."

    mc "Same thing."

    orion "No. It's not."

    narrator "You look at him properly for the first time in years."
    narrator "He's not gloating."
    narrator "And that's the part that bothers you."

    menu:
        "What's your problem? You already won.":
            $ respect -= 1
            jump rival_explains_sharp
        "...Show me.":
            $ respect += 1
            jump rival_explains_calm

label rival_explains_sharp:

    orion "My problem is that you were {i}right{/i} and still lost marks."
    orion "That should bother you more than it bothers me."

    narrator "It does bother you."
    narrator "More than he will ever know."
    narrator "But you don't say that."
    narrator "You never say that."

    mc "I'll live."

    orion "You mean you lost?"
    orion "That's different."

    mc "Aww~ You're worried about me?"
    mc "I'm flattered."
    mc "Don't tell me you have feelings for me now?"

label rival_explains_calm:

    orion "Look at your answer."
    orion "You wrote 2.5 times 10 to the power of 3."
    orion "The data had three significant figures."

    mc "The value is identical."

    orion "The information isn't."

    thought "I hope he trips on his huge ego."

    jump library_scene

label library_scene:
    scene bg library

    narrator "It becomes a thing."
    narrator "After school, library."
    narrator "His notes and your questions."

    thought "This is strategic."
    thought "He's the only person in this school whose study methods are worth reverse engineering."
    thought "This is my strategy."

    narrator "You open the notebook to a fresh page."
    narrator "The left side is Physics."
    narrator "The right side..."
    narrator "You close before he can see it."

    thought "Orion Hale."
    thought "Taps pencil when emotionally irritated."
    thought "Avoids eye contact when complimented."
    thought "Smiles after correcting someone.. but not today."
    thought "Doesn't react to praise as he hears it often."
    thought "Asks questions he already knows the answer to."

    orion "You're not writing."

    mc "I'm thinking."

    orion "About Physics?"

    narrator "A beat."

    mc "Obviously."

    narrator "He looks at you for one second longer than necessary."
    narrator "Then looks back at his page."
    
    jump chapter_one

