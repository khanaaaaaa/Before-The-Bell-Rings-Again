label prologue:
    scene bg classroom
    with with fade

    narrator "Midterm results day."
    narrator "The list goes up at 8: 47 AM."
    narrator "You don't run to check it."
    narrator "You already know"

    scene bg results_board
    with with dissolve

    narrator "Rank 2. Again."
    narrator "And above you."
    narrator "Same name."
    narrator "It always has been."
    narrator "The gap this time?"
    narrator "0.1 marks."

    mc "..."

    scene bg classroom
    with dissolve

    narrator "You're stuffing your paper into your bag when you hear footsteps beside you."

    orion "Hey!"

    mc "What."

    narrator "He holds your paper."
    narrator "Question 3."
    narrator "Red ink."
    narrator "Half mark deducted."

    mc "I got the right answer."

    orion "You got {i}an{/i} answer."

    mc "Same thing."

    orion "No. It's not."

    menu:
        "What's your problem? You already won.":
            jump rival_explains_sharp
        "...Show me.":
            jump rival_explains_calm

    return