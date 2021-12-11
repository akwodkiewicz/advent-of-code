import stream from "stream";

class PartOneSolver extends stream.Transform {
    #avgBits: number[] = [];
    #numOfSamples: number = 0;

    _transform(
        chunk: Buffer,
        _: BufferEncoding,
        callback: stream.TransformCallback
    ) {
        chunk
            .toString()
            .split('\n')
            .filter(s => s)
            .map(numberString =>
                numberString
                    .split(''))
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
        callback(null, `${gammaRate * epsilonRate}\n`);
    }
}

process.stdin
    .pipe(new PartOneSolver())
    .pipe(process.stdout);
