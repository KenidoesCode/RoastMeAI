import random

def inferno_roast(features):
    """
    features = {
        "emotion": ...,
        "skin": ...,
        "eye_state": ...,
        "face_shape": ...,
        "hairline": ...,
        "ethnicity": ...,
        "pose": ...
    }
    """

    emotion = features["emotion"]
    skin = features["skin"]
    eyes = features["eye_state"]
    shape = features["face_shape"]
    hair = features["hairline"]
    eth = features["ethnicity"]
    pose = features["pose"]

    roast = []

    # 0. OPENING — DEMON MODE ACTIVATION
    demon_entry = [
        "I looked at your picture and even my GPU flinched.",
        "Your face loaded and my system asked: 'Bro… are you SURE?'",
        "You walked in like a corrupted PNG file.",
        "Your aura alone reduced my screen brightness for safety."
    ]
    roast.append(random.choice(demon_entry))

    # 1. ETHNICITY VIBES (NOT RACIAL—JUST VIBE HUMOUR)
    if eth == "south_asian":
        roast.append("You have the 'I didn't choose engineering, engineering chose me' starter pack face.")
    elif eth == "east_asian":
        roast.append("You look like you get A+ but still disappoint someone at home.")
    elif eth == "white":
        roast.append("You look like you say ‘brother from another mother’ without irony.")
    elif eth == "black":
        roast.append("You have main-character energy but zero plot development.")
    else:
        roast.append("Even ancestry.com would lag trying to decode your vibe.")

    # 2. EMOTION — PSYCHOLOGICAL DAMAGE
    if emotion == "happy":
        roast.append("That smile screams 'I joke a lot because life hurts fr'.")
    elif emotion == "sad":
        roast.append("You look like you apologize to chairs after bumping into them.")
    elif emotion == "angry":
        roast.append("Chill bro, even dogs won't steal your food.")
    elif emotion == "neutral":
        roast.append("Neutral? Looks more like 'life defeated me years ago'.")
    else:
        roast.append("Your emotional state is as unclear as your career path.")

    # 3. SKIN TYPE — DOOM MODE (3× ROAST)
    if skin == "acne":
        roast += [
            "Your face looks like it's buffering.",
            "Each pimple has more personality than you.",
            "Your skin looking like Google Earth zoomed too close."
        ]
    elif skin == "oily":
        roast += [
            "Your face shining brighter than your future will ever be.",
            "I could fry pooris on that forehead.",
            "Oil companies want your T-zone formula."
        ]
    elif skin == "dry":
        roast += [
            "Your skin so dry even your tears evaporate on arrival.",
            "Moisturizer left you on read.",
            "Your face is begging the air for humidity."
        ]

    # 4. EYES — HOSTEL + PSYCHO MIX
    if eyes == "sleepy":
        roast += [
            "You look like sleep owes you money.",
            "Your eyes say 'I’m okay', your aura says 'no you’re not'.",
            "You overthink at 3AM for sport."
        ]
    elif eyes == "wide":
        roast += [
            "Why staring like you just realized life has no main quest?",
            "Analyzing reality like a failed philosophy major.",
            "Wide eyes, narrow future."
        ]

    # 5. FACE SHAPE — PURE VIOLENCE
    if shape == "round":
        roast += [
            "Your face looks like a rejected emoji draft.",
            "Symmetry tried bro… it really did.",
            "You store emotions in your cheeks like a squirrel."
        ]
    elif shape == "long":
        roast += [
            "Your face long like a Chennai–Dubai flight path.",
            "Your forehead starts in Mumbai and ends in Bangalore.",
            "Even giraffes looked at you and said 'damn'."
        ]
    else:
        roast.append("Your face shape is losing a battle with geometry.")

    # 6. HAIRLINE — DOOM MODE
    if hair == "receding":
        roast += [
            "Your hairline is socially distancing from you.",
            "At this rate your shampoo will last 8 years.",
            "Your hair fleeing like your ex during arguments."
        ]
    else:
        roast.append("Hairline normal… something had to be okay in your life.")

    # 7. POSE — DEMON POV
    if pose == "tilted":
        roast.append("Your head tilted like you're begging life for one more chance.")
    elif pose == "side":
        roast.append("Side pose? Trying to hide the part that needs the most fixing?")
    elif pose == "close":
        roast.append("Zoomed in this much? You chose emotional damage voluntarily.")

    # 8. FINAL KILLSHOT
    killshots = [
        "Your face has ‘main character energy’, but of the guy who dies in scene 1.",
        "You look like your parents still argue whose mistake you are.",
        "Your vibe says 'I reply late but expect instant replies'.",
        "Your aura screams 'I peaked in 8th grade'.",
        "If disappointment had a face, it would request NOT to be yours."
    ]
    roast.append(random.choice(killshots))

    return " ".join(roast)
