label start:
    jump name_entry


label name_entry:

    scene bg classroom
    with fade

    narrator "Before we begin."
    narrator "What's your name?"

    $ raw_name = renpy.input("Enter your name", length=20).strip()
    $ player_name = raw_name if raw_name else "You"

    narrator "[player_name]."
    narrator "Right."
    narrator "Let's go."

    jump prologue
