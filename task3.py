def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    indicesMinPupil = [i for i,v in enumerate(pupil) if v < lesson[0]]
    indicesMinTutor = [i for i,v in enumerate(tutor) if v < lesson[0]]
    indicesMaxPupil = [i for i,v in enumerate(pupil) if v > lesson[-1]]
    indicesMaxTutor = [i for i,v in enumerate(tutor) if v > lesson[-1]]

    for i in indicesMaxPupil:
        pupil[i] = lesson[-1]
    for i in indicesMaxTutor:
        tutor[i] = lesson[-1]

    for i in indicesMinPupil:
        pupil[i] = lesson[0]
    for i in indicesMinTutor:
        tutor[i] = lesson[0]

    tutorTuples = []
    for i in range(int(len(tutor)/2)):
        tutorTuples.append([tutor[i*2],tutor[i*2 + 1]])

    pupilTuples = []
    for i in range(int(len(pupil)/2)):
        pupilTuples.append([pupil[i*2],pupil[i*2 + 1]])

    tutorTuples = sorted(tutorTuples)
    pupilTuples = sorted(pupilTuples)

    newTutorTuples = []
    for tupl in tutorTuples:
        if tupl[1]-tupl[0] > 0:
            if not bool(newTutorTuples):
                newTutorTuples.append(tupl)
            else:
                if newTutorTuples[-1][1] >= tupl[0]:
                    if tupl[1] >= newTutorTuples[-1][1]:
                        newTutorTuples[-1][1] = tupl[1]
                else:
                    newTutorTuples.append(tupl)

    newPupilTuples = []
    for tupl in pupilTuples:
        if tupl[1]-tupl[0] > 0:
            if not bool(newPupilTuples):
                newPupilTuples.append(tupl)
            else:
                if newPupilTuples[-1][1] >= tupl[0]:
                    if tupl[1] >= newPupilTuples[-1][1]:
                        newPupilTuples[-1][1] = tupl[1]
                else:
                    newPupilTuples.append(tupl)

    pupilTuples = newPupilTuples
    tutorTuples = newTutorTuples

    total = 0
    currentTuple = 'tutor'
    while bool(pupilTuples) & bool(tutorTuples):
        if currentTuple == 'pupil':
            if tutorTuples[0][0] > pupilTuples[0][1]:
                pupilTuples = pupilTuples[1:]
                currentTuple = 'tutor'
            elif tutorTuples[0][1] > pupilTuples[0][1]:
                total += pupilTuples[0][1] - tutorTuples[0][0]
                pupilTuples = pupilTuples[1:]
                currentTuple = 'tutor'
            else:
                total += tutorTuples[0][1] - tutorTuples[0][0]
                tutorTuples = tutorTuples[1:]

        else:
            if pupilTuples[0][0] > tutorTuples[0][1]:
                tutorTuples = tutorTuples[1:]
                currentTuple = 'pupil'
            elif tutorTuples[0][1] < pupilTuples[0][1]:
                total += tutorTuples[0][1] - pupilTuples[0][0]
                tutorTuples = tutorTuples[1:]
                currentTuple = 'pupil'
            else:
                total += pupilTuples[0][1] - pupilTuples[0][0]
                pupilTuples = pupilTuples[1:]

    return total


tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
