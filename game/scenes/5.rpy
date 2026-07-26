label chapter_three:

    scene bg rooftop

    narrator "He doesn't go to the library after class."
    narrator "He goes to the roof."
    narrator "You know this because you follow him."
    narrator "You tell yourself it's strategic."

    narrator "His notebook is closed."
    narrator "That's the first time you've ever seen that during study hours."
    narrator "It looks wrong."
    narrator "Like a clock with no hands."

    mc "You're not studying."

    orion "Observant."

    mc "Four days distracted. Sign error in Gauss's Law yesterday."
    mc "You never make sign errors."

    narrator "Something shifts in his face."
    narrator "Not the usual careful neutrality."
    narrator "Something underneath it."

    orion "You track my errors."

    mc "I track everything."

    orion "Why."

    narrator "You don't have an answer that isn't embarrassing."
    narrator "So you say the true one."

    mc "Because you're the only person here worth tracking."

    narrator "He looks at the city."

    orion "My father wants me to drop Physics."
    orion "Commerce is more practical."

    mc "That's the stupidest thing I've ever heard."

    orion "He's not wrong about the practicality."

    mc "He's wrong about you."

    narrator "You say it before you can stop yourself."
    narrator "He turns."
    narrator "You don't take it back."
    narrator "You're usually very good at taking things back."

    thought "Because it's true."
    thought "Because the way he looks when something clicks—"
    thought "Stop."

    orion "You don't know me."

    mc "I know you tap your pencil when you're irritated."
    mc "I know you avoid eye contact when someone compliments you."
    mc "I know you ask questions you already know the answer to."
    mc "I know you moved to the table by the window when the library got crowded."
    mc "And left one chair empty."

    narrator "A long silence."

    orion "That's observation."

    mc "Same thing."

    narrator "He almost smiles."
    narrator "Not quite."
    narrator "Close enough."

    orion "Gauss's Law. From the beginning."

    mc "You already know Gauss's Law."

    orion "Teach it anyway."

    thought "Like he just wants to hear me explain things."
    thought "Like that's something someone would want."
    thought "Like I'm worth listening to."

    narrator "You sit beside him."
    narrator "You teach him Gauss's Law."
    narrator "He already knows all of it."
    narrator "The sun goes down while you're talking."
    narrator "Neither of you mentions it."

    menu:
        "Ask him what he decided.":
            $ respect += 1
            jump rooftop_ask
        "Don't ask. Just stay.":
            jump rooftop_stay

label rooftop_ask:

    mc "Commerce or Physics."

    orion "Physics."

    mc "Because?"

    orion "Because someone told me my father was wrong about me."
    orion "And I believed them."

    mc "That's a terrible reason to make a life decision."

    orion "Probably."

    narrator "He's smiling."
    narrator "Actually smiling."
    narrator "You don't have a category for this one."

    thought "I'm going to need a new page."

    jump chapter_four

label rooftop_stay:

    narrator "You don't ask."
    narrator "You stay until a janitor tells you both to leave."
    narrator "At the bottom of the stairs he says:"

    orion "Thank you."

    mc "For what."

    orion "For not asking."

    narrator "You walk in opposite directions."
    narrator "You spend the whole walk home trying to figure out how he knew."
    narrator "You don't figure it out."
    narrator "That's new."

    jump chapter_four
