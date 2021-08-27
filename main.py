from datetime import date

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
    
    inefficient_reps.sort(key=lambda x : x[1])
    efficient_reps.sort(key=lambda x : x[1])

    with open(f'{today}.txt', 'w') as f:
        f.write(f'Reps below target: {inefficient_reps}')
        f.write('\n')
        f.write(f'Reps above target: {efficient_reps}')

    # print(f'Reps below target: {inefficient_reps}')
    # print(f'Reps above target: {efficient_reps}')



if __name__ == '__main__':
    show_inefficient(reps_pd_hours, reps_output)

