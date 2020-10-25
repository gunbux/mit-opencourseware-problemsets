# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    dict = {}
    for line in inputFile:
        list = line.strip().split(',')
        ##print list #-Working as intended

        dict[list[0]] = (int(list[1]),int(list[2]))

    return dict

    ##print 'final dictionary value is %s' % (dict) #-Working as intended
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

##loadSubjects('shortened_subjects.txt') #-Working as intended
def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

sub = loadSubjects('shortened_subjects.txt')
#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[VALUE] > subInfo2[VALUE]

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    return subInfo1[WORK] < subInfo2[WORK]

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...
    return (float(subInfo1[VALUE])/float(subInfo1[WORK])) > (float(subInfo2[VALUE])/float(subInfo2[WORK]))

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    currentWork = 0
    courses = {}
    while currentWork < maxWork:
        bestSubject = None
        for subject in subjects:

            if subjects[subject][WORK] > maxWork-currentWork:
                ##print 'limit reached. work is %s while work remaining is %s' % (subjects[subject][WORK],maxWork-currentWork)
                continue
            elif bestSubject == None:
                if subject not in courses:
                    bestSubject = subject
                continue
            else:
                ##print 'comparing %s and %s' % (subjects[bestSubject][WORK],subjects[subject][WORK])
                test = comparator(subjects[bestSubject],subjects[subject])
                ##print 'test results are %s' % (test)
                if test == False and subject not in courses:
                    bestSubject = subject
                    ##print 'best subject is now %s' % (bestSubject)

        if bestSubject == None:
            ##print 'breaking'
            break
        else:
            currentWork += subjects[bestSubject][WORK]
            courses[bestSubject] = subjects[bestSubject]
            ##print 'currentWork is %s while courses is %s' % (currentWork, courses)

    return courses

#
# Problem 3: Subject Selection By Brute Force
#
def countValue(subjects):

    value = 0
    for sub in subjects:
        value += subjects[sub][VALUE]

    return value

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    if len(subjects) == 0 or maxWork <= 0:
        ##print 'base case'
        return {}
    else:
        bestCase = {}

        for sub in subjects:
            case = {}
            if subjects[sub][WORK] > maxWork:
                continue
            else:
                ## recursive case here
                case[sub] = subjects[sub]
                remainingSubjects = subjects.copy()
                remainingSubjects.pop(sub)
                remainingWork = maxWork - subjects[sub][WORK]

                recursion = bruteForceAdvisor(remainingSubjects,remainingWork)
                case.update(recursion)

            ##print 'current case is %s with value of %s. \n current best case s %s with value of %s'
            ##print 'got here'
            if bestCase == {}:
                bestCase = case
            else:
                if countValue(case) > countValue(bestCase):
                    bestCase = case

        ##print 'returning case of %s' % (bestCase)
        return bestCase

printSubjects(bruteForceAdvisor(sub,15))

