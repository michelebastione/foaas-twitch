import random

class FOAAP:

    general_expressions = [
        "Fuck you, asshole. ",
        "Eat a bag of fucking dicks. ",
        "Please choke on a bucket of cocks. ",
        "How about a nice cup of shut the fuck up? ",
        "You disingenuous dense motherfucker! ",
        "I'd love to stop and chat to you but I'd rather have type 2 diabetes. ",
        "Happiness can be found, even in the darkest of times, if one only remembers to fuck off. ",
        "I can't fuckin' even. ",
        "Everyone can go and fuck off. ",
        "Fuck everything. ",
        "Fuck you, your whole family, your pets, and your feces. ",
        "Fascinating story, in what chapter do you shut the fuck up? ",
        "Fuck That, Fuck You ",
        "Fuck you, you fucking fuck ",
        "I don't want to talk to you, no more, you empty-headed animal, food trough wiper. I fart in your general direction. Your mother was a hamster and your father smelt of elderberries. Now go away or I shall taunt you a second time. ",
        "Fuck you and the horse you rode in on. ",
        "Fuck you, fuck me, fuck your family. Fuck your father, fuck your mother, fuck you and me. ",
        "Fuck my life. ",
        "You low polygon motherfucker! ",
        "Maybe. Maybe not. Maybe fuck yourself. ",
        "Fuck me. ",
        "To fuck off, or to fuck off (that is not a question) ",
        "You Fucktard! ",
        "That's fucking ridiculous ",
        "For Fuck's sake! ",
        "Fuck this shit! ",
        "Fuck you very much. ",
        "Fuck that. ",
        "Fuck this. "
        "Thanks, fuck you too. "
    ]

    particular_expressions = [
        "f\"Fuck off, you must, {name}. \"",
        "f\"Who the fuck are you anyway, {name}, why are you stirring up so much trouble, and, who pays you? \"",
        "f\"Absolutely fucking Not, {name}, No Fucking Way! \"",
        "f\"Fucking {name} is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill {name}. \"",
        "f\"{name}, your head is as empty as a eunuch's underpants. Fuck off! \"",
        "f\"Fuck me gently with a chainsaw, {name}. Do I look like Mother Teresa? \"",
        "f\"Fuck off {name}, you worthless cocksplat \"",
        "f\"{name} you are being the usual slimy hypocritical asshole... You may have had value ten years ago, but people will see that you don't anymore. \"",
        "f\"{name}, go and take a flying fuck at a rolling donut. \"",
        "f\"Go fuck yourself {name}, you'll disappoint fewer people. \"",
        "f\"And {name} said unto {from_name}, 'Verily, cast thine eyes upon the field in which I grow my fucks', and {from_name} gave witness unto the field, and saw that it was barren. - Shakespeare, probably\"",
        "f\"Fuck that shit, {name}. \"",
        "f\"Golf foxtrot yankee, {name}. \"",
        "f\"Fucking fuck off, {name}. \"",
        "f\"{name}: Fuck off. And when you get there, fuck off from there too. Then fuck off some more. Keep fucking off until you get back here. Then fuck off again. \"",
        "f\"Oh fuck off, just really fuck off you total dickface. Christ, {name}, you are fucking thick. \"",
        "f\"{name}, there aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap. \"",
        "f\"What you've just said is one of the most insanely idiotic things I have ever heard, {name}. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points {name}, and may God have mercy on your soul. \"",
        "f\"Well {name}, aren't you a shining example of a rancid fuck\"",
        "f\"Fuck off, {name}. \"",
        "f\"{name}, why don't you go outside and play hide-and-go-fuck-yourself? \"",
        "f\"What the fuck is your problem {name}? \"",
        "f\"{name}, Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch! \"",
        "f\"{name}, shut the fuck up. \"",
        "f\"{name}, what the fuck were you actually thinking? \"",
        "f\"Listen here {name}! What part of 'Fuck Off' don't you understand? \"",
        "f\"I don't waste my fucking time with your bullshit {name}! \"",
        "f\"Fuck you, {name}. \""
    ]

    fucks_not_given = [
        "I don't give a flying fuck. ",
        "I give zero fucks. ",
        "You can not imagine the immensity of the FUCK I do not give. ",
        "Do I look like I give a fuck? ",
        "Looking for a fuck to give. ",
        "No fucks given. ",
        "I don't give a rat's arse. ",
        "Not a single fuck was given. ",
        "Do you think I give a fuck? ",
        "Who has two thumbs and doesn't give a fuck? You guessed it, me!. ",
        "Ask me if I give a motherfuck?! ",
        "Zero, that's the number of fucks I give. "
    ]

    def fuck_off(self, from_name: str) -> str:
        return f"{random.choice(self.general_expressions)}"

    def fuck_off_more(self, name: str) -> str:
        choice = eval(random.choice(self.particular_expressions))
        return f"{choice}"

    def idgaf(self, from_name):
        return f"{random.choice(self.fucks_not_given)}- {from_name}"
