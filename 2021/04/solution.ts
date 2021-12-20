import { fstat, readFileSync } from "fs";
import { promises } from "stream";

class BingoBoard {
    private readonly DIMENSION = 5 as const;

    public constructor(private readonly board: number[]) {
    }

    get rows(): number[][] {
        return this.board.reduce<number[][]>((result, item, idx) =>
            new Boolean((idx % this.DIMENSION
                ? result[result.length - 1].push(item)
                : result.push([item])))
            && result,
            []);
    }

    toString(): string {
        return `\nBingoBoard: \n${this.rows.map(row => `\t[${row}]\n`)}\n`;
    }
}

class Parser {

    constructor(private readonly filename: string) {
    }

    public async parse() {
        const input = readFileSync(this.filename, {encoding: 'utf-8'});
        return this.processInput(input);
    }

    private processInput(input: string) {
        const lines = input.split('\n');
        const drawnNumbers = lines[0].split(',').map(s => Number.parseInt(s));
        const boardInputs: number[][] = [];
        const linesForBoards = lines.splice(1).filter(s => s);
        for (let x = 0; x < linesForBoards.length; x++) {
            if (x % 5 === 0) {
                boardInputs.push([]);
            }
            boardInputs[Math.floor(x / 5)]
                .push(
                    ...linesForBoards[x]
                        .split(' ')
                        .filter(x => x)
                        .map(s => Number.parseInt(s)))
        }
        const boards: BingoBoard[] = [];
        for (let x = 0; x < boardInputs.length; x++) {
            boards.push(new BingoBoard(boardInputs[x]));
        }
        return [drawnNumbers, boards];
    }
}

class Solver {

    public async solve() {
        const [drawnNumbers, boards] = await new Parser(process.argv[2]).parse();
        console.log(drawnNumbers);
        console.log(boards.toString());
    }

}


(async () => {
    console.log(promises);
    await new Solver().solve();
})();