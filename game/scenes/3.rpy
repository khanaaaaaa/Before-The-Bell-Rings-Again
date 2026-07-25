label chapter_one_library:
    
    scene bg chapter_one_library

    orion "My turn."

    mc "Why does your smile look sinister?"

    orion "It doesn't."

    mc "It does."

    orion "You're deflecting."

    narrator "You are."
    narrator "You know you are."
    narrator "You do it anyway."

    mc "Ask your question."

    orion "Why do you study?"

    narrator "A beat."
    narrator "Then another."

    mc "Because I want to be first."

    orion "That's not a reason, it's a mere position."

    mc "Same thing."

    orion "You said that last time."
    orion "It wasn't true then either."

    thought "I hate him."
    thought "I hate that he asks questions like they're traps."
    thought "I hate that they are."

    mc "Why do {i}you{/i} study?"

    orion "Because I want to understand things."

    mc "That's not a reason, rather a personality trait you're proud of."

    narrator "He looks at you."
    narrator "Something shifts in his expression."
    narrator "Not offense."
    narrator "Closer to interest."

    orion "Fair."

    narrator "You didn't expect that."
    narrator "You were ready for an arguement."
    narrator "You had three follow-up lines prepared."
    narrator "You don't get to use any of them."

    thought "He does that."
    thought "Argees when you expect him to fight."
    thought "It's the most irritating thing about him."
    thought "It makes you feel like you're arguing with a wall that keeps moving."

    orion "Columb's Law. Derive it."

    mc "We're back to Physics?"

    orion "We never left."

    narrator "You derive it."
    narrator "Correctly."
    narrator "He doesn't say so."
    narrator "He just moves to the next question."

    thought "He never says 'good job'."
    thought "I don't know if I hate this or need it."

    orion "Electric field lines. Prperties. All of them."

    mc "They originate from positive charges and terminate at negative."
    mc "They never intersect."
    mc "They're continuous curves in free space."
    mc "Density indicates field strength."

    orion "You missed one."

    mc "I didn't."

    orion "They don't form closed loops in electrostatics."

    narrator "A pause."

    mc "That's implied by the first two."

    orion "Implied isn't stated."

    mc "In an exam, it would be."

    orion "You're not studying for an exam right now."

    narrator "You look at him."

    mc "Then what am I studying for?"

    narrator "He doesn't answer immediately."
    narrator "He writes something in his notebook."
    narrator "You wait."
    narrator "You don't know why you wait."

    orion "For the same reason I do."
    orion "You just haven't admitted it yet."
    
    thought "I want to throw this notebook at his head."
    thought "I want to ask him what he means."
    thought "I do neither."

    mc "You're insufferable."

    orion "You keep showing up."

    narrator "You don't have an answer for that."
    narrator "The worst part is he's not even smiling when he says it."
    narrator "He's already looking back at his page."
    
    menu:
        "Leave early.":
            $ respect -= 1
            jump library_exit_cold
        "Stay and say nothing.":
            $ respect += 1
            jump library_exit_quiet

label library_exit_cold:

    narrator "You close your notebook."
    narrator "Loudly."

    mc "I'll finish at home."

    orion "Okay."

    thought "I wanted him to react."
    thought "I wanted him to say something."
    thought "I hate that I wanted that."

    narrator "You leave."
    narrator "The walk home takes twelve minutes."
    narrator "You spend eleven of them thinking about the property you missed."

    jump chapter_two

label library_exit_quiet:

    narrator "You stay."
    narrator "You don't say anything."
    narrator "Neither does he."
    narrator "For forty minutes you just study."
    narrator "Side by side."
    narrator "In the kind of silence that as weight."

    thought "This is the longest I've been near someone without performing."
    thought "Without calculating what they think of me."
    thought "Without managing it."
    thought "I don't know what to do with that."

    narrator "When the library closes, you both pack up at the same time."
    narrator "He holds the door."
    narrator "Not as a gesture."
    narrator "Just because he got there first."

    orion "Same time Thursday?"

    mc "I'll think about it."

    orion "You'll be here."

    thought "I hate that he's right."
    thought "I hate that I already know he's right."
    thought " I hate that I don't hate it as much as I should."

    jump chapter_two