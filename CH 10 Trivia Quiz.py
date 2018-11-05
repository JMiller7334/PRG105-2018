class Question:
    def __init__(self):
        self.__text = "None"
        self.__choices = "None"
        self.__answer = "None"

    def setup(self, new_text, new_choices, new_answer):
        self.__text = str(new_text)
        self.__choices = str(new_choices)
        self.__answer = str(new_answer)

    def get_text(self):
        return self.__text

    def get_choices(self):
        return self.__choices

    def get_answer(self):
        return self.__answer


def main():
    score1 = 0
    score2 = 0
    questions_a = []

    q1 = Question()
    q1.setup("In Mauy Thai low kicks are blocked with what part of the body?",
             "A forearms, B: hands, C: instep, D: shins",
             "D")
    questions_a.append(q1)

    q2 = Question()
    q2.setup("The early version of the Taekwondo Tornado kick utilized what type of kick in its execution?",
             "A : roundhouse kick, B: hook kick, C: crescent kick, D: sidekick",
             "C")
    questions_a.append(q2)

    q3 = Question()
    q3.setup("Wushu is a martial arts that originates from where?",
             "A. China, B: Japan, C: Korea, D: United States",
             "A")
    questions_a.append(q3)

    q4 = Question()
    q4.setup("In Judo Ippon Seoi nage is a what?",
             "A: leg sweeps, B: arm drag take-down, C: Shoulder throw, D: Take-down reversal",
             "C")
    questions_a.append(q4)

    q5 = Question()
    q5.setup("In the Martial Arts Kyouki-do a speed brake is what in board breaking?",
             "A: when the practitioner holds their own board, B two breaks done quickly, C: A single break "
             "involving more than one board, D: a double break involving 4 or more boards.",
             "A")
    questions_a.append(q5)
    print("----- Questions below for Player1 -----")
    for questions in questions_a:
        print("\n")
        print(str(questions.get_text()))
        print(str(questions.get_choices()))
        user_input = str(input("Please type the correct answer. choose either A, B, C, or D.")).upper()
        if user_input == str(questions.get_answer()):
            score1 = score1 + 1
            print("Correct! Player1 gets +1 point. | Player1 score:" + str(score1))
        else:
            print("Incorrect! the answer was " + str(questions.get_answer()) + " Player1 does not get a point.")

    questions_a = []
    q1 = Question()
    q1.setup("In Jiu-jitsu what is widely considered to be the best position?",
             "A: side-mount, B: north-south, C guard, D rear-mount",
             "D")
    questions_a.append(q1)

    q2 = Question()
    q2.setup("In Jiu-Jitsu juji gatame is what?",
             "A: pin hold, B: wrist lock, C: arm-bar, D: leg lock",
             "C")
    questions_a.append(q2)

    q3 = Question()
    q3.setup("Shang Gou or Hook swords are martial arts swords of what origin?",
             "A: Chinese, B: Japanese, C Korean, D, Brazilian",
             "A")
    questions_a.append(q3)

    q4 = Question()
    q4.setup("In Muay Thai a Teep is what type of strike?",
             "A: Side kick, B: Front Kick, C: Knee strike, D: Round Kick",
             "B")
    questions_a.append(q4)

    q5 = Question()
    q5.setup("Hap-Kido is a martial arts style that mainly uses what to control opponents in a fight?",
             "A: Kicks, B: Punches, C: Joints locks, D: Take-downs",
             "C")
    questions_a.append(q5)
    print("\n")
    print("\n")
    print("\n")
    print("----- Questions below for Player2 -----")
    for questions in questions_a:
        print("\n")
        print(str(questions.get_text()))
        print(str(questions.get_choices()))
        user_input = str(input("Please type the correct answer. choose either A, B, C, or D.")).upper()
        if user_input == str(questions.get_answer()):
            score2 = score2 + 1
            print("Correct! Player2 gets +1 point. | Player2 score:" + str(score2))
        else:
            print("Incorrect! the answer was " + str(questions.get_answer()) + " Player2 does not get a point.")

    print("\n")
    print("Scores: Player1: " + str(score1) + " | Player2: " + str(score2) + ".")
    if score1 > score2:
        print("Player1 wins!")
    elif score1 < score2:
        print("Player2 wins!")
    else:
        print("It's a draw!")


main()
