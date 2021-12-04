import fs from "fs";

function prepareInput(filename: string) {
    return fs
        .readFileSync(`01/${filename}`)
        .toString('utf-8')
        .split('\n')
        .map(x => Number.parseInt(x));
}

function solve(numbers: readonly number[], windowSize: number) {
    return numbers
        .slice(windowSize - 1)
        .map((_, idx) =>
            numbers
                .slice(idx, idx + windowSize)
                .reduce((acc, x) => acc + x)) 
        .filter((_, idx, array) =>
            idx === 0
                ? false
                : array[idx - 1] < array[idx])
        .length;
}

function main(filename: string) {
    const input = prepareInput(filename);
    const solutions = [
        solve(input, 1),
        solve(input, 3),
    ]
    console.log(solutions);
}

main('test-input');
main('input');