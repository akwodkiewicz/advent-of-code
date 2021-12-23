import { readFileSync } from "fs";

const filename = process.argv[2];
const input = readFileSync(filename, 'utf-8');

const world: Map<`${number},${number}`, number> = new Map();

for (const line of input.split('\n')) {
    const [start, end] =
        line
        .split(' -> ')
        .map(pointStr =>
            pointStr
            .split(',')
            .map(x =>
                Number.parseInt(x)));
    const vector = [
        Math.sign(end[0] - start[0]),
        Math.sign(end[1] - start[1])
    ] as const;
    
    // Uncomment for part 1
    // if (startX !== endX && startY !== endY) continue;

    let x = start[0] - vector[0];
    let y = start[1] - vector[1];
    while (x !== end[0] || y !== end[1]) {
        x = x + vector[0];
        y = y + vector[1];
        world.set(
            `${x},${y}`,
            (world.get(`${x},${y}`) ?? 0) + 1);
    }
}

let counter = 0;
for (const value of world.values()) {
    if (value > 1) counter++;
}

console.log(counter);