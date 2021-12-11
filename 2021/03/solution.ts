import stream from "stream";

class Solver extends stream.Transform {
    #avgBits: number[] = [];
    #numOfSamples: number = 0;

    _transform(
        chunk: Buffer,
        _: BufferEncoding,
        callback: stream.TransformCallback
    ) {
        const numbers = chunk
            .toString()
            .split('\n')
            .filter(s => s);

        // update avg value for each bit with each number
        numbers
            .map(numberString =>
                numberString.split(''))
            .map(digitArray =>
                digitArray.map(digitString =>
                    Number.parseInt(digitString)))
            .forEach(digitArray => {
                digitArray.forEach((digit, idx) => {
                    if (this.#avgBits[idx] === undefined) {
                        this.#avgBits[idx] = digit;
                    } else {
                        this.#avgBits[idx] =
                            (this.#numOfSamples * this.#avgBits[idx] + digit)
                            / (this.#numOfSamples + 1);
                    }
                })
                this.#numOfSamples++;
            })
        const gammaRate = Number.parseInt(this.#avgBits.map(n => Math.round(n)).join(''), 2);
        const epsilonRate = Number.parseInt(this.#avgBits.map(n => 1 - Math.round(n)).join(''), 2);

        let oxygenGeneratorRatingCandidates = [...numbers];
        let co2ScrubberRatingCandidates = [...numbers];
        for (
            let bit = 0;
            (bit < numbers[0].length
             && (oxygenGeneratorRatingCandidates.length > 1
                || co2ScrubberRatingCandidates.length > 1));
            bit++
        ) {
            if (oxygenGeneratorRatingCandidates.length > 1) {
                const mostCommonBit = Math.round(
                    oxygenGeneratorRatingCandidates
                        .reduce((sum, candidate) =>
                            sum + Number.parseInt(candidate[bit]),
                            0)
                    / oxygenGeneratorRatingCandidates.length
                );
                oxygenGeneratorRatingCandidates = oxygenGeneratorRatingCandidates
                    .filter(candidate =>
                        Number.parseInt(candidate[bit]) === mostCommonBit
                    );
            }
            if (co2ScrubberRatingCandidates.length > 1) {
                const leastCommonBit = 1 - Math.round(
                    co2ScrubberRatingCandidates
                        .reduce((sum, candidate) =>
                            sum + Number.parseInt(candidate[bit]),
                            0)
                    / co2ScrubberRatingCandidates.length
                );
                co2ScrubberRatingCandidates = co2ScrubberRatingCandidates
                    .filter(candidate =>
                        Number.parseInt(candidate[bit]) === leastCommonBit
                    );
            }
        }
        const oxygenGeneratorRating = Number.parseInt(oxygenGeneratorRatingCandidates[0], 2);
        const co2ScrubberRating = Number.parseInt(co2ScrubberRatingCandidates[0], 2);

        callback(
            null,
            `part one: ${gammaRate * epsilonRate}\n`
            + `part two: ${oxygenGeneratorRating * co2ScrubberRating}\n`
        );
    }
}

process.stdin
    .pipe(new Solver())
    .pipe(process.stdout);
