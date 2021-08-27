from datetime import date

reps_pd_hours = {
    'ALLANA GILGEOUS' : 7.5,
    'SALLY ROBERTS' : 5.0,
    'MATEO CURCURU' : 3.5,
    'DARIUS L. WOODS' : 3.0,
    'TALI WEG' : 3.0,
    'LAKSHMI BABUREDDY' : 2.5,
    'BRIAN LI' : 2.5,
    'ANINA VOLCY' : 2.5,
    'LIAM FITZGERALD' : 2.0,
    'JONATHAN SPIELMAN' : 2.0,
    'BRIAN PARKER' : 1.0,
    'MELISSA TYSON' : 1.0,
    'THERESE CHERIAN' : 0.0,
    'ABHIT PAL' : 0.0
}

reps_output = {
    'ALLANA GILGEOUS' : 11.0,
    'SALLY ROBERTS' : 4.0,
    'MATEO CURCURU' : 2.0,
    'DARIUS L. WOODS' : 1.0,
    'TALI WEG' : 1.0,
    'LAKSHMI BABUREDDY' : 10.0,
    'BRIAN LI' : 3.0,
    'ANINA VOLCY' : 1.0,
    'LIAM FITZGERALD' : 1.0,
    'JONATHAN SPIELMAN' : 4.0,
    'BRIAN PARKER' : 1.0,
    'MELISSA TYSON' : 2.0,
    'THERESE CHERIAN' : 0.0,
    'ABHIT PAL' : 0.0
}

def show_inefficient(hours, output):

    today = date.today()

    # initialize array to return reps who didn't hit 2.0
    inefficient_reps = []
    efficient_reps = []

    # calculate how many trainings each rep should get per 2.0 hours
    for value in hours:
        hours[value] = hours[value] * 2

    for k, k2 in zip(hours, output):
        if hours[k] > output[k2]:
            efficiency = output[k] / (hours[k] / 2)
            inefficient_reps.append([k, efficiency])
        else:
            if hours[k] != 0:
                efficiency = output[k] / (hours[k] / 2)
                efficient_reps.append([k, efficiency])

    with open(f'{today}.txt', 'w') as f:
        f.write(f'Reps below target: {inefficient_reps}')
        f.write('\n')
        f.write(f'Reps above target: {efficient_reps}')

    # print(f'Reps below target: {inefficient_reps}')
    # print(f'Reps above target: {efficient_reps}')



if __name__ == '__main__':
    show_inefficient(reps_pd_hours, reps_output)

