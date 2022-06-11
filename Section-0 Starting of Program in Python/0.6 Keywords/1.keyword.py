"""

    Python Keywords Related Learning
    ================================
    # In Python, Python has keyword package to know and work with the keywords.
    # To work with keywords need to import the keyword package.
    
"""

# importing necessary module
import keyword

# getting keyword list from the 'keyword' module
print(keyword.kwlist)

# to check whether a word is keyword or not use iskeyword() function
print(keyword.iskeyword("word")) # returns False though not keyword
print(keyword.iskeyword("not")) # return True though keyword
