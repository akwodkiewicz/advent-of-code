/**
 * @returns array of `array` elements grouped into of `groupSize`-long arrays 
 */
export function group<T extends unknown[]>(array: T, groupSize: number): T[] {
    return array.reduce<T[]>((result, item, idx) =>
        new Boolean((idx % groupSize
            ? result[result.length - 1].push(item)
            : result.push([item] as typeof result[number])))
        && result,
        []);
}

export function* range(exclusiveEnd: number) {
    for (let i = 0; i < exclusiveEnd; i++)
        yield i;
}