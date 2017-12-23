import re


TICKS = 4000


def parse_input(filename):
    particles = {}
    index = 0
    with open(filename) as file:
        for line in file:
            vectors = re.split(r'[<>]', line)[1::2]
            numbers = []
            for vector in vectors:
                for value in vector.split(','):
                    numbers.append(int(value))
            position = tuple(numbers[:3])
            velocity = tuple(numbers[3:6])
            acceleration = tuple(numbers[6:9])
            particles[index] = (position, velocity, acceleration)
            index += 1
    return particles


def find_positions(particles, ticks):
    positions = {}

    for i in range(len(particles)):
        position, velocity, acceleration = particles[i]
        positions[i] = calculate_position(
            position, velocity, acceleration, ticks)
    return positions


def calculate_position(position, velocity, acceleration, tick):
    sigma = ((tick + 1) * tick) / 2
    return tuple([position[i] + tick * velocity[i] + acceleration[i] * sigma for i in range(3)])


def calculate_distances(positions):
    return [sum(abs(d) for d in positions[key]) for key in positions]


def run_full_simulation(particles, ticks):
    particles_map = {particles[k][0]: (
        particles[k][1], particles[k][2], particles[k][0]) for k in particles}
    update_buffer = {}
    last_length = len(particles_map)
    print('t=0: {}'.format(last_length))
    for tick in range(1, ticks + 1):
        for position in particles_map:
            vel = particles_map[position][0]
            acc = particles_map[position][1]
            x_0 = particles_map[position][2]
            new_position = calculate_position(x_0, vel, acc, tick)
            if new_position in update_buffer:
                update_buffer[new_position] = None
            else:
                update_buffer[new_position] = (vel, acc, x_0)

        particles_map = {
            k: update_buffer[k] for k in update_buffer if update_buffer[k] is not None}
        update_buffer.clear()
        if len(particles_map) < last_length:
            last_length = len(particles_map)
            print('t={}: {}'.format(tick, last_length))
    return len(particles_map)


def main():
    particles = parse_input('advent20_input.txt')
    distances = calculate_distances(find_positions(particles, TICKS))
    minimum = min(distances)
    index = distances.index(minimum)
    print("After {} ticks, minimum = {} at i = {}".format(TICKS, minimum, index))
    remaining = run_full_simulation(particles, TICKS)
    print('After {} ticks there are {} particles left'.format(TICKS, remaining))


if __name__ == '__main__':
    main()
