import fs from "fs";

type Direction = 'forward' | 'up' | 'down';
const DIRECTIONS: readonly Direction[] = ['forward', 'down', 'up'] as const;
function isDirection(x: unknown): x is Direction {
    return typeof x === 'string' && (DIRECTIONS as string[]).includes(x);
}
type Unit = number;
type Command = [Direction, Unit];
type IncorrectPosition = [Unit, Unit];
type Position = [Unit, Unit, Unit];

function prepareInput(filename: string): Command[] {
    return fs
        .readFileSync(`02/${filename}`)
        .toString('utf-8')
        .split('\n')
        .map(x => {
            const [unknownDirection, unknownUnits] = x.split(' ');
            if (!isDirection(unknownDirection)) {
                throw new Error(`wrong direction: ${unknownDirection}`);
            } else if (Number.isNaN(Number.parseInt(unknownUnits))) {
                throw new Error(`wrong units: ${unknownUnits}`);
            } else {
                return [unknownDirection, Number.parseInt(unknownUnits) as Unit]
            }
        });
}

function applyIncorrectCommand(
    [x, depth]: IncorrectPosition,
    [direction, units]: Command
): IncorrectPosition {
    switch(direction) {
        case 'down':
            return [x, depth + units];
        case 'up':
            return [x, depth - units];
        case 'forward':
            return [x + units, depth];
    }
}

function applyCommand(
    [x, depth, aim]: Position,
    [direction, units]: Command
): Position {
    switch(direction) {
        case 'down':
            return [x, depth, aim + units];
        case 'up':
            return [x, depth, aim - units];
        case 'forward':
            return [x + units, depth + (units * aim), aim];
    }
}

function solveOne(commands: Command[]) {
    return commands
        .reduce((pos, command) =>
            applyIncorrectCommand(pos, command),
            [0, 0] as IncorrectPosition)
        .reduce((acc, x) =>
            acc * x,
            1);
}

function solveTwo(commands: Command[]) {
    return commands
        .reduce((pos, command) =>
            applyCommand(pos, command),
            [0, 0, 0] as Position)
        .slice(0, -1)
        .reduce((acc, x) =>
            acc * x,
            1);
}

function main(filename: string) {
    const input = prepareInput(filename);
    const solutionOne = solveOne(input);
    const solutionTwo = solveTwo(input);
    console.log(solutionOne);
    console.log(solutionTwo);

}

main('test-input');
main('input');