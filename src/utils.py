import torch
import matplotlib.pyplot as plt

def plot(values, moving_avg_period, every, curr_episode):
    plt.figure(2)
    plt.clf()
    plt.title("Training...")
    plt.xlabel('Episode')
    plt.ylabel('Duration')
    plt.plot(values)
    moving_avg = get_moving_average(moving_avg_period, values)
    plt.plot(moving_avg)
    if curr_episode % every == 0:
        print(f'Episode {len(values)}\n{moving_avg_period} episode average: {moving_avg[-1]}')
    plt.pause(0.001)

def get_moving_average(period, values):
    values = torch.tensor(values, dtype=torch.float)
    if len(values) >= period:
        moving_avg = values.unfold(dimension=0, size=period, step=1).mean(dim=1).flatten(start_dim=0)
        moving_avg = torch.cat((torch.zeros(period-1), moving_avg))
    else:
        moving_avg = torch.zeros(len(values))

    return moving_avg.numpy()
