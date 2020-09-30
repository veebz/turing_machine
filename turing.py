#!/usr/bin/env python

"""In the past years, algorithms have left their origin disciplines of 
mathematics and informatics and moved to the centre of public discourse. 
Fuelled by the Silicon Valley ideology and tech solutionism, “algorithms” 
are usually viewed as rational, efficient and legitimate means to solve a 
given problem. Often without a technical understanding of the term, 
the public attaches high hopes to algorithms: They are often considered to be 
fairer than humans (Araujo et al 2020) and are trusted with
countless important decisions such as scoring (e.g. for crime recidivism 
likeliness, or for credit eligibility) or autonomous driving. From different 
sides, especially from those who profit economically or are in need of easy 
solutions to complex problems, epistemological claims are made about 
algorithms and algorithmic systems.

Media scholars have rightly and forcefully pointed to the discriminatory and 
wide-reaching effects of algorithms. Especially when personal data (e.g. 
clickstream data, transactional data, location data) comes into play – as in 
various data-driven systems, often based on machine learning – various 
examples of algorithms have been shown to reinforce social inequality, 
perpetuate injustice and to disproportionately affect historically 
marginalized communities : many systems are biased and discriminate against 
people of colour and lower-income communities in crucial areas such as 
risk-based sentencing (Angwin, Larson et al. 2016), predictive policing 
(Ferguson 2017) or predatory lending (Fisher 2009; O’Neil 2016). Another 
strand of research points to the fact that data-driven systems can also be 
deeply connected to diversion from social benefits such as monetary aid. 
Marginalized communities are disproportionately exposed to these systems and 
more likely to lack the resources to contest decisions that affect them. 
(Eubanks 2018; Petty, Saba et al 2018)

As these examples show, the notion of “algorithm” does not have anything to 
do with being rational, legitimate, efficient or fair. What then is an 
algorithm?

Euclid’s step-by-step instructions to compute the greatest common divisor of 
two non-negative numbers, published in his Elements, are often considered as 
one of the first algorithms. Since the 15th century, algorithms gained 
prominence in the West, where the decimal system was being introduced, 
and have played a major role in scientific and technical revolutions ever 
since. Despite their proliferation, it was not before the late 19th century that
mathematicians and logicians made attempts to define what an algorithm is 
characterized by. In the beginning of the 20th century, Alonzo Church, 
Alan Turing and others began to mathematically formalize the notion of 
“algorithm”.

Triggered by Kurt Gödel’s infamous incompleteness theorem which holds that 
some things within the formal system of mathematics cannot be 
calculated, Alan Turing set out to discover what it is that can be 
calculated. To do so, he attempted to formalise what humans do when they 
calculate something and came up with a machine imitating the procedure: “We 
may compare a man in the process of computing a real number to a machine” 
(Turing 1936, p.231) Rather than directly asking “What can(not) be 
calculated?”, Turing asked “What does it mean to compute a real number?” or, 
in other words: “What is an algorithm?”.

Turing developed a hypothetical machine, which would later on become known as 
Turing machine, and equipped it with some mechanical features (a tape, 
a moving head) that supposedly imitate the behaviour of a human computing a 
number. Like a human computes using a pen and squared paper, Turing 
envisioned a machine with a reading and writing head and an infinite amount 
of squared tape, each square containing one symbol. No matter which number 
was to be computed, his machine was able to simulate the procedure. He thus 
defined the basic principles of a universal machine for computation and 
until today, no machine exists that is theoretically more powerful than the 
Turing machine.

When Turing published his paper, the idea of computers had only begun to 
emerge. Later, Turing's conceptualization of the Turing machine turned out to be
a great basis for modelling what computers do. In computer science, a function
f(x,y) is considered computable if a Turing machine exists that simulates its
behaviour for all x and y. An algorithm for f(x,y) exists, if there is a 
Turing machine that computes f(x,y). Thus, the concepts of algorithm and 
Turing machine are closely connected.

Below is an example of a Turing machine that adds two numbers (programme_2).
The way the algorithm is implemented, we could say that this Turing machine
imitates a child adding two numbers by counting his*her fingers: no semantic
understanding of the mathematical process exists, adding works by counting 
one number up and the other one down in the same rhythm until one number 
reaches 0. However, I explicitly want to move away from such comparisons of 
humans (or learning children) and machines here because they either suggest that
machines possess capacities that are, until today, specifically human,
or tap into the pitfall of thinking of the human (brain) as working somehow
mechanically (cf. Dupuy 2000) [1].

The exemplary Turing machine below is an attempt to performatively highlight 
the  fact that machines cannot think (nor recognize or see). The solely 
syntactical and quantitative operations required to add two numbers with a 
Turing machine are a reminder that the machine does not need to think in 
order to perform tasks. Like Turing argued in 1950, it is enough to imitate.[2]

Even though much more powerful and complex in hardware and software, neural 
networks for machine learning applications operate in a very similar way:
originally, their attempt was to imitate the functioning of the human brain (
cf. Rosenblatt 1958) in different situations such as image recognition. To do
so, the machine is fed with pre-classified images to recognize patterns,
syntactical features in images which allow for their statistical discrimination
without considering their "semantics" (Cramer 2018). After the learning
process, the neural network is able to discriminate the same patterns in new
images which allow for classification according to the classification scheme
given in the training data set. Although the notion has a different
connotation in informatics, this "data discrimination" is a highly political
process (Apprich 2018, p.x), especially when decisions are made about people.

Machine learning systems have become possible due to the increasing 
computational power available at ever smaller cost, widespread datafication 
and the resulting vast amounts of data and new database technologies to store
them. On a theoretical level, however, these applications of computing 
machines are not more powerful than the good old Turing machine. Both the 
exemplary implementation of a Turing machine below and commonly used systems 
for pattern discrimination (not only used for image recognition but also for 
various other purposes) rely on syntactical operations to automatically 
filter/generate information from data.

The scholarly works about risk-based sentencing, predatory lending or 
predictive policing quoted above are only the most visible cases of how
algorithms can politically discriminate. On a deeper level, their basic  
operating schemes exclude qualitative interpretation and hermeneutics (
Cramer 2018) in favor of automated, purely quantitative and syntactial
operations. The application of an algorithm is thus in itself already a
political decision because it favors some epistemological assumptions over
others (cf. Winner 1980) [3].

By making recourse to the history of the notion of algorithm, it was my attempt
to shed light on this more implicit dimension of algorithmic bias. In times
in which algorithms are successfully promoted as easy and efficient
problem solvers, it is important to come back to the epistemological
assumptions on which they are based, and to critically reflect upon the
epistemological claims that circulate about them in public discourse today.

Only when implemented considerately - that is to say with a clear idea of
their respective epistemological assumptions, affordances and limits -
algorithms can help humans approach complex problems and find solutions. For
example, as Nick Srnicek argues by recourse to Frederic Jameson,
representational technologies such as computer simulations, computer models
or automatic filtering software, which are nowadays used to approach complex
issues such as the climate, global finance, or political crises, have enabled
humans to create new types of cognitive maps of today’s word (Srnicek 2013,
14). In line with Srnicek, I believe that, when implemented considerately and
with the right goal in mind, algorithms can help individuals navigate the world
and point beyond the the actuality of contemporary capitalism.

[1] Alan Turing himself famously evaded/rejected the question "Can machines
think" in order to evade the necessity to define the notions of "machine" and
"intelligence". However, what is striking about his paper are the repeated
comparisons between humans and machines. The question whether Turing thought
whether machines might one day be able to think (like humans) is contested in
the literature (cf. Copeland 2004). However, in his paper from 1936,
he explicitly speaks about the human brain which has specific "states of
mind" which seemingly determine human behaviour, at least in the realm of
computing (Turing 1936, p. 251).

[2] Turing's "Imitation Game" has widely spread and led to the emergence of
"popular understandings of machine thought as simulative of human thought" (
Fazi 2019, p.814) which Beatrice Fazi refers to as "simulative paradigm".
As Fazi lays out, new developments will possibly stear away from this
paradigm in the future.

[3] Thus, in a sense, the Turing machine implemented below is also biased.
"""

def turing_machine(input_tape, programme, head_id, state_id):
    """Recursive function for the execution of a Turing machine.

    Following Turing's invention of the "stored programme" idea (Turing
    1936), this Turing machine can be reprogrammed by adding other
    programmes. In this implementation of the Turing machine, the programme
    is, however, not stored on the tape itself.
    """

    def move_head(instruction, head_id):
        """Imitates the moving head of a Turing machine.

        Depending on the instructions of the programme defined in
        turing_machine(), the head either moves right or left on the tape,
        or halts the machine.
        """
        if instruction == 'right':
            head_id += 1
            print(f'The head moved right and is now at index {head_id}.')
            return head_id
        elif instruction == 'left':
            head_id -= 1
            print(f'The head moved left and is now at index {head_id}.')
            return head_id
        elif instruction == 'halt':
            print(f'The programme has halted. The sequence computed by the '
                  f'machine is: {tape}.')
            print('The second number shows the result.')
            exit()
        else:
            print('Error: Incorrect instructions for the movement of the head')

    def change_state(instr, state_id):
        """Manages the different states of the Turing machine.

        The machine changes its state according to programme instructions.
        """
        if instr == 0:
            print('The state remains the same.')
            return state_id
        elif instr == 1:
            state_id = state_id + 1
            print('The machine moved to the next state of the programme.')
            return state_id
        elif instr == -1:
            state_id = state_id - 1
            print('The machine moved to the previous state of the programme.')
            return state_id
        else:
            state_id = state_id + int(instr)
            print(f'The machine moved {instr} steps.')
            return int(state_id)

    def get_index():
        """Checks which instructions in the programme matrix to follow.
        """
        for i,e in enumerate(programme[0][state_id]):
            if str(input_tape[head_id]) == str(e[0]):
                break
        return i

    # Chose a programme to run (set variable to programme_1 or programme_2)
    # programme = programme_2

    # Check which instruction of the programme to follow
    i = get_index()

    # Change the tape according to programme instructions
    print(f'The head scanned the symbol {input_tape[head_id]}.')
    input_tape[head_id] = programme[0][state_id][i][1]
    print(f'The number was changed to {programme[0][state_id][i][1]}.')

    # Check if programme requires state change and move the head
    new_state = change_state(programme[0][state_id][i][3], state_id)
    new_head = move_head(programme[0][state_id][i][2], head_id)
    print(f'The tape now reads: {input_tape}.')

    # Tail recursion
    turing_machine(input_tape, programme, new_head, new_state)


# Programmes
# Programme 1: Adds 1 to a given number.
    # The tape should look like this:
    # ('start', 1, 0, 1, None, None, None)

programme_1 = [[
    # m-configurations
    # state_0:
    [
        # state_0: Move right until the first blank.

        # How the programmes in this implementation work:
        # If the head reads 'start', nothing is changed and it moves right.
        ['start', 'start', 'right', 0],
        # If the head reads 0, nothing is changed and it moves right.
        [0, 0, 'right', 0],
        # If the head reads 1, nothing is changed and it moves right.
        [1, 1, 'right', 0],
        # If the head reads None, it moves left and moves on to state +1.
        [None, None, 'left', 1]
    ],

    # state_1: Add 1.
    [
        [0,1,'halt',0],
        [1,0,'left',0]
    ]
]]

# Programme 2: Adds two numbers. Numbers have to be separated on the tape
# (list) by None, e.g.:
# ('start', 1, 0, 1, None, 1, 0, 0, None, None, None, None)
# In order to be able to add large numbers and to simulate Turing's
# infinite tape, make sure to add a few empty slots at the end of the tape.

programme_2 = [[
    # m-configurations

    # state_0: move to right until a 1 is seen, then continue with the
    # next instruction
    # if no 1 is seen before the first blank, there is nothing left to add.
    # In this case, we move 9 states further down in the programme and halt.
    [
        ['start', 'start', 'right', 0],
        [0, 0, 'right', 0],
        [1, 1, 'right', 1],
        [None, None, 'halt', 0]
    ],

    # state_1:
    # move to the right until the first blank.
    # Once the blank is reached, the head is moved left and the machine
    # changes its state (+1) to state X.
    [
        ['start', 'start', 'right', 0],
        [0, 0,'right', 0],
        [1, 1, 'right', 0],
        [None, None, 'left', 1]
    ],

    # state_2: SUBSTRACTION
    # We are now at the end of the first number.
    # We substract 1 and move to the next state (+1) to state X.
    [
        [1, 0, 'right', 1],
        [0, 1, 'left', 0],
        [None, None, 'right', 1],
        ['start', 'start', 'right', 1]
    ],

    # state_3:
    # We are now somewhere within the first number from which we have
    # substracted 1. We move to the start of the second number.
    [
        [0, 0, 'right', 0],
        [1, 1, 'right', 0],
        [None, None, 'right', 1]
    ],

    # state_4:
    # We move right until the first blank at the end of the second number.
    [
        [0, 0, 'right', 0],
        [1, 1, 'right', 0],
        [None, None, 'left', 1]
    ],

    # state_5: ADDITION
    # We add 1 to the second number:
    # We move to left switching 1 to 0 and 0 to 1.
    # If we move to the start of the number without seeing any 0,
    # the number will become longer.
    [
        [0, 1, 'left', 3],
        [1, 0, 'left', 0],
        [None, None, 'right', 1]
    ],

    # state_6:
    # We are at the start of the second number now again.
    # We now it is a 0 ( we have changed it to 0) and switch it to 1.
    [
        [0, 1, 'right', 1]
    ],

    # state_7:
    # We change all other zeros to 1 until we reach the first blank.
    # We change the blank to 0 - thereby adding a new digit to our number.
    [
        [0, 0, 'right', 0],
        [None, 0, 'left', 1]
    ],

    # state_8:
    # Move back to start of the tape, then to programme's start.
    [
        [0, 0, 'left', 0],
        [1, 1, 'left', 0],
        [None, None, 'left', 0],
        ['start', 'start', 'right', -8]
    ],
]]

# Initialization (initial m-configuration of the machine)
head_init = 0
state_init = 0

# Preparation of the tape
# Note: the tape needs to be prepared according to the workings of the chosen
# programme (see comments on the two exemplary programmes above)
tape = ['start',1,1,1,0,1,None,1,1, None, None, None, None, None]
print(f'Input: {tape}')

# Main
turing_machine(tape, programme_2, head_init, state_init)

"""The code above is an attempt to imitate the functioning of a Turing 
machine very closely. The Turing machine implemented here includes two 
exemplary programmes with respective m-configurations (see Turing 1936, 
p. 231) and a "scanner" (ibid.) moving across a tape. The two 
additional functions get_index() and change_state() manage the execution of the 
programme. In Turing's conceptualisation, these functions would correspond to 
the mechanical setup of the machine. Crucially, the programmes in this 
exemplary implementation work without "working memory" - the head only 
reads/changes one symbol on the tape at a time: "The 'scanned symbol' is the 
only one of which the machine is, so to speak, 'directly aware'. However, 
by altering its m-configuration the machine can effectively remember some of the
symbols which it has 'seen' (scanned) previously." (ibid) This Turing 
machine has a one-directional tape. For simplicity, the Turing machine always 
starts from a defined starting position which is called 'start'. The None 
object represents the "x" letters on intermediate squares of the tape as 
envisioned by Turing: "On the intermediate squares we never print anything 
but  "x". These letters serve to 'keep the place' for us and are erased 
when we have finished with them." (p. 234) As the erasure would have made the 
above programmes much more complex, I decided to not include the necessary 
states to do so in this exercise."""



# Bibliography

# Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016, May 23). Machine
# Bias: There’s software used across the country to predict future criminals.
# And it’s biased against blacks.
# https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

# Apprich, C. (2018). Introduction. In C. Apprich, W. H. K. Chun, F. Cramer,
# & H. Steyerl (Eds.), Pattern Discrimination (pp. ix–xii). meson press.

# Araujo, T., Helberger, N., Kruikemeier, S., & de Vreese, C. (2020). In AI we
# trust? Perceptions about automated decision-making by artificial intelligence.
# AI & SOCIETY, 35, 611–623.

# Copeland, B. J. (Ed.). (2004). The essential Turing: Seminal writings in
# computing, logic, philosophy, artificial intelligence, and artificial life,
# plus the secrets of Enigma. Clarendon Press; Oxford University Press.

# Cramer, F. (2018). Crapularity Hermeneutics: Interpretation as the Blind
# Spot of Analytics, Artificial Intelligence, and Other Algorithmic Producers
# of the Postapocalyptic Present. In C. Apprich, W. H. K. Chun, F. Cramer,
# & H. Steyerl (Eds.), Pattern Discrimination (pp. 23–58). meson press.

# Dupuy, J.-P. (2000). The Mechanization of the Mind: On the Origins of
# Cognitive Science. Princeton University Press.

# Eubanks, V. (2018). Automating Inequality: How High-Tech Tools Profile, Police
# and Punish the Poor. St. Martin’s Press.

# Fazi, M. B. (2019). Can a machine think (anything new)?  Automation beyond
# simulation. AI & SOCIETY, 34(4), 813–824.

# Ferguson, A. G. (2017). The Rise of Big Data Policing: Surveillance, Race, and
# the Future of Law Enforcement. New York University Press.

# Fisher, L. (2009). Target Marketing of Subprime Loans. Journal of Law and
# Policy, 18(1), 121–155.

# O’Neil, C. (2016). Weapons of Math Destruction: How Big Data Increases
# Inequality and Threatens Democracy. Crown.

# Petty, T., Saba, M., Lewis, T., Gangadharan, S. P., & Eubanks, V. (2018).
# Reclaiming our data: Interim report, Detroit. Our Data Bodies.

# Rosenblatt, F. (1958). The perceptron: A probabilistic model for information
# storage and organization in the brain. Psychological Review, 65(6), 386–408.

# Srnicek, N. (2013). Representing Complexity [PhD Dissertation, London School
# of Economics].
# http://etheses.lse.ac.uk/803/1/Srnicek_Representing_Complexity.pdf

# Turing, A. (1936). On Computable Numbers. With an Application to the
# Entscheidungsproblem.

#  	     --- (1937). Computability and λ-definability. Journal of Symbolic
# Logic, 2(4), 153–163.

# 	     --- (1950). Computing Machinery and Intelligence.


# Winner, L. (1980). Do Artifacts Have Politics? Daedalus, 109(1), 121–136.




