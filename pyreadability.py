import re
import sys
class Readable:
    """
    See how readable your text is.
    This takes in the "txt" argument and must be a string
    """
    def __init__(self, txt):
        self.txt = txt
        if not isinstance("", type(self.txt)):
            return TypeError("TypeError: Please provide a \"string\" only for the argument.")
        self.syllablesPattern = "[aiouy]+e*|e(?!d$|ly).|[td]ed|le$"
        self.words = len(self.txt.split(" "))
        self.sentances = len(self.txt.replace(
            "!", ".").replace("?", ".").split("."))
        self.syllables = len(re.findall(self.syllablesPattern, self.txt))
    # https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
    """ 
    This calculates the flesch reading ease with the equations https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
    returns {float}
    """
    def fleschReadingEase(self):
        score = round((206.835 - 1.015*(self.words/self.sentances) -
                       84.6*(self.syllables/self.words)), 3)
        return score
    """ 
    This calculates the flesch kincaid grade level with the equations found above
    returns {float}
    """
    def fleschKincaidGradeLevel(self):
        score = round((0.39*(self.words/self.sentances)+11.8 *
                       (self.syllables/self.words)-15.59), 3)
        return score

if __name__ == "__main__":
    #driver code
    if not sys.argv[1] or not sys.argv[2]:
        print("Please enter a first argument (like \"fleschReadingEase\") and then a sentance in the second argument")
    text = ' '.join(sys.argv[2:])
    func = Readable(text)
    if sys.argv[1] == "fleschReadingEase":
        print(func.fleschReadingEase())
    elif sys.argv[1] == "fleschKincaidGradeLevel":
        print(func.fleschKincaidGradeLevel())
    else: 
        print("Entry does not exist.")