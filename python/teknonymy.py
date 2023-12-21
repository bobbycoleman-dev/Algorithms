"""
Introduction
In some societies, you receive a name around your birth and people use it to refer to you while you don't have any children.

Once you have at least one child, people give you a teknonym. A teknonym is a way to refer to someone according to some of its descendants, like the 'mother of Joe', the 'great-grandfather of Jane', etc.

In this kata, you will receive some kind of family tree and your task will be to give the correct teknonym to the members of the tree, according to the rules specified in the next section.

Rules
- If X doesn't have any direct descendant : they don't have a teknonym.
    - A direct descendant of X is any member, but X, of the subtree rooted at X.
- If X has some direct descendants : the teknonym is built according to the sex of X and the name of the elder among its direct descendants of the most distant generation from X.
    - The 'generation distance' between X and one of its descendant, say Y, is the number of levels between X and Y.
    - So you have to :
        1. Find the most distant generation
        2. Find the elder of that generation
        3. Build the teknonym of X according to the two previous informations.
    - There won't be any ambiguity to determine who is the elder between two direct descendants of someone.
- The possible teknonyms are (all lower case):
    - 'father of Y', 'grandfather of Y', 'great-grandfather of Y', 'great-great-grandfather of Y', and so on ;
    - 'mother of Y', 'grandmother of Y', 'great-grandmother of Y', 'great-great-grandmother of Y', and so on ;

Example

Here we have three generations:
    - first generation : a
    - second generation : b, c, d
    - third generation : h, e, f, g.\
    
The direct descendants of:
    - a are b, c, d, e, f, g, h ;
    - b is h ;
    - d are e, f, g ;
    - c, e, f, g and h haven't any descendant.

Teknonyms :
    - for a : the last generation, and the most distant one from a, is the third generation, the elder of that generation is e and there is two generations between a and e, so the teknonym of a is 'grandfather of e';
    - for b : b has only one direct descendant, h, in the third generation, and there is one generation between b and h, so the teknonym of b is 'mother of h' ;
    - for d : d has three direct descendants in the third generation, namely e, f, g, and e is the elder, so the teknonym of d is 'father of e' ;
    - c, h, e, f and g haven't any descendant, so they don't have a teknonym.

Input

A structure representing a kind of family tree. Each node of the tree is a structure representing a person and containing:
    - the date of birth of the person
    - its sex, either 'm' for male and 'f' for female
    - its teknonym, an empty string you can mutate if it's relevant to do so
    - a sequence of children. Each child is a person, and the sequence can be empty.

In Python, the structure is a dictionary. Each node has the following keys:

date_of_birth : datetime.datetime
name : str
teknonym : str # that's the field you should mutate if it's relevant to do so
sex : str
children : list[dict] # list of children, possibly empty
"""
