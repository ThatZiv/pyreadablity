# pyreadablity
See how readable your text is with python and Flesch–Kincaid readability tests.

## Using it as a module:
```python
import pyreadability
text = "This is a test sentance. The following output will show you how readable this text is classified under the Flesch–Kincaid readability tests"
r = pyreadability.Readable(text)
print(
    "Total Words: %(words)s\n"
    "Sentances: %(sentances)s\n"
    "Syllables: %(syllables)s\n\n"
    "Reading ease score: %(score)i\n"
    "Grade Level: %(grade)i" %
    {
        "words": r.words,
        "sentances": r.sentances,
        "syllables": r.syllables,
        "score": r.fleschReadingEase(),
        "grade": r.fleschKincaidGradeLevel()
    }
)
"""
output>
Total Words: 22
Sentances: 2
Syllables: 38

Reading ease score: 49
Grade Level: 9
"""
```

## Using it in the command line:
```sh
> python pyreadability.py fleschReadingEase This is a test sentance. The following output will show you how readable this text is classified under the Flesch–Kincaid readability tests
> 49.543
> python pyreadability.py fleschKincaidGradeLevel This is a test sentance. The following output will show you how readable this text is classified under the Flesch-Kincaid readability tests
> 9.082
```
