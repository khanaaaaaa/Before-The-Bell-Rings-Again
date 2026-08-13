label chapter_five:

    scene bg library

    narrator "Three days before Physics."
    narrator "Last session."
    narrator "You both know it without saying it."

    narrator "You go through everything."
    narrator "Two hours."
    narrator "No gaps."

    narrator "At the end he closes his notebook."
    narrator "You close yours."
    narrator "Neither of you moves."

    orion "You're ready."

    mc "I know."

    orion "You were ready two weeks ago."

    narrator "Silence."

    mc "Why did you keep coming then."

    narrator "He looks at the table."
    narrator "Then at you."

    orion "Same reason you did."

    thought "I came because I wanted to beat you."
    thought "I came because your methods were worth studying."
    thought "I came because the table by the window had one empty chair."
    thought "And it was always for me."
    thought "And I knew that."
    thought "And I kept coming anyway."

    mc "That's not an answer."

    orion "It's the only one I have."

    narrator "The library is empty."
    narrator "Just the two of you and the fluorescent lights and three years of keeping score."

    orion "Can I tell you something."

    mc "..."

    orion "The first time you asked why force follows an inverse square law—"
    orion "No one had ever asked me that."
    orion "Not a teacher. Not anyone."
    orion "You asked it like the answer mattered."
    orion "Not for the exam."
    orion "Just because you wanted to know."

    narrator "You look at him."

    orion "That's when I moved to the table by the window."

    thought "Oh."
    thought "Oh."
    thought "I wasn't ready for that."
    thought "I'm still not ready for that."

    mc "You could have just said that."

    orion "You weren't ready to hear it."

    mc "And now?"

    narrator "He looks at you."
    narrator "Waiting."
    narrator "Not pushing."
    narrator "Just waiting."
    narrator "Like he has all the time in the world."
    narrator "Like the answer matters."
    narrator "Not for the exam."
    narrator "Just because he wants to know."

    menu:
        "\"I'm still not.\"":
            $ respect -= 1
            jump ending_bittersweet
        "\"Maybe.\"":
            $ respect += 1
            jump ending_good


label ending_good:

    narrator "He almost smiles."
    narrator "The one without a category."

    orion "That's enough."

    narrator "You pack up."
    narrator "He holds the door."
    narrator "Not as a gesture."
    narrator "Just because he got there first."

    scene bg results_board

    narrator "Physics finals."
    narrator "8:47 AM."
    narrator "You don't run."

    narrator "Rank 1."
    narrator "Your name."
    narrator "For the first time."
    narrator "Below it, his."
    narrator "The gap: 0.1 marks."

    narrator "You stand there for three seconds."
    narrator "You don't smile."
    narrator "There's no one watching."
    narrator "There's no performance to give."
    narrator "You just feel it."
    narrator "Clean and quiet."
    narrator "Like a proof that resolves."

    narrator "He appears beside you."

    orion "Congratulations."

    mc "You're not upset."

    orion "No."

    mc "Why not."

    orion "Because I know why you won."
    orion "It's not the same reason as before."

    narrator "He's right."
    narrator "It's not."
    narrator "You don't know exactly when it changed."
    narrator "Somewhere between significant figures and a rooftop at sunset."
    narrator "Somewhere between 'teach it anyway' and 'you don't have to do that here.'"

    mc "Same time next term?"

    orion "You'll be there."

    mc "Obviously."

    scene black

    narrator "You walk home."
    narrator "Twelve minutes."
    narrator "You spend none of them thinking about rank."
    narrator "That's new."

    return


label ending_bittersweet:

    narrator "He nods."
    narrator "Like he expected that."
    narrator "Like he's not surprised."
    narrator "Maybe he isn't."

    orion "Okay."

    narrator "You pack up."
    narrator "He packs up."
    narrator "You leave separately."
    narrator "The way you always have."

    scene bg results_board

    narrator "Physics finals."
    narrator "8:47 AM."
    narrator "You don't run."

    narrator "Rank 2."
    narrator "Your name."
    narrator "Above it, his."
    narrator "The gap: 0.1 marks."

    narrator "You stand there for three seconds."
    narrator "Then you smile."
    narrator "Because someone is watching."
    narrator "And you know how to look like someone who doesn't care."

    narrator "It's the same smile."
    narrator "The one you've been practicing since you were eleven."
    narrator "It costs nothing."

    narrator "He appears beside you."
    narrator "Looks at the board."
    narrator "Doesn't say anything."
    narrator "You wait for the gloat."
    narrator "It doesn't come."
    narrator "It never comes."
    narrator "That's still the part that bothers you."

    mc "Next term."

    orion "Next term."

    narrator "He walks away."
    narrator "You watch him go."
    narrator "You think about the table by the window."
    narrator "The empty chair."
    narrator "The way he said {i}you don't have to do that here.{/i}"
    narrator "The way you said {i}I'm still not ready.{/i}"
    narrator "And meant it."
    narrator "And chose it anyway."

    thought "I could have said something different."
    thought "I know that."
    thought "I chose not to."
    thought "I always choose not to."
    thought "That's the thing nobody understands about me."
    thought "I don't panic."
    thought "I just lose."
    thought "Quietly."
    thought "And I already know."

    scene black

    narrator "You walk home."
    narrator "Twelve minutes."
    narrator "You spend all twelve of them thinking about 0.1 marks."
    narrator "Some things don't change."
    narrator "Not yet."

    return
