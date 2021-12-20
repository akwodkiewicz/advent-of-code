import { readFileSync } from "fs";
import { group, range } from "../utils";
import { EventEmitter } from "events";

class BingoBoard {
    private readonly DIMENSION = 5 as const;
    private readonly marked: Map<number, boolean> = new Map();
    private alreadyBingoed: boolean = false;

    public constructor(
        private readonly eventEmitter: EventEmitter,
        private readonly board: number[]
    ) {
        board.forEach(n => this.marked.set(n, false));
        eventEmitter.on('drawn', (n: number) =>
            this.onDrawn(n));
    }

    get rows(): number[][] {
        return group(this.board, this.DIMENSION);
    }

    get isBingo(): boolean {
        return (
            this.rows.some(r => r.every(n => this.marked.get(n)))
            || Array.from(range(this.DIMENSION))
                .some(columnIdx =>
                    this.rows.every(r =>
                        this.marked.get(r[columnIdx]))))
    }

    get unmarkedSum(): number {
        return this.board.reduce((result, current) =>
            this.marked.get(current) ? result : result + current,
            0);
    }

    public toString(): string {
        return `BingoBoard: \n\t${this.rows
            .map(row =>
                `|${row.map(n =>
                    `${this.marked.get(n)
                        ? ' X'
                        : n < 10
                            ? ` ${n}`
                            : n}`)
                    .join(' ')}|`)
            .join('\n\t')}`;
    }

    private onDrawn(drawn: number) {
        if (this.alreadyBingoed) {
            return;
        }
        this.marked.set(drawn, true);
        if (this.isBingo) {
            this.alreadyBingoed = true;
            this.eventEmitter.emit('bingo', drawn * this.unmarkedSum);
        }
    }
}

class Drawer {
    private readonly DELAY = 100 as const;

    private numOfDrawnNumbers = 0;
    private ongoingGame?: NodeJS.Timer;

    public constructor(
        private readonly eventEmitter: EventEmitter,
        private readonly numbersToDraw: number[]
    ) { }

    public start() {
        this.ongoingGame = setInterval(() =>
            this.draw(this.numbersToDraw[this.numOfDrawnNumbers++]),
            this.DELAY);
    }

    public stop() {
        if (this.ongoingGame) {
            clearInterval(this.ongoingGame);
        }
    }

    public draw(n: number) {
        console.log(`next number: ${n}`);
        this.eventEmitter.emit('drawn', n);
    }
}

class Parser {
    constructor(private readonly filename: string) { }

    public async parse() {
        const input = readFileSync(this.filename, { encoding: 'utf-8' });
        return this.processInput(input);
    }

    private processInput(input: string): [number[], number[][]] {
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
        return [drawnNumbers, boardInputs];
    }
}

class Solver {
    private readonly eventEmitter;
    private boards: BingoBoard[] = [];
    private drawer!: Drawer;
    private bingos: number[] = [];

    constructor() {
        this.eventEmitter = new EventEmitter();
        this.eventEmitter.setMaxListeners(Infinity);
        this.eventEmitter.on('bingo', this.onBingo.bind(this));
    }

    public async solve() {
        const [drawnNumbers, boardInputs] = await new Parser(process.argv[2]).parse();
        this.createBoards(boardInputs);
        this.createDrawer(drawnNumbers);
        this.drawer.start();
    }

    private onBingo(bingo: number) {
        this.bingos.push(bingo);
        if (this.bingos.length === 1) {
            console.log(`----- FIRST WINNER: ${bingo}`);
            return;
        }
        if (this.bingos.length === this.boards.length) {
            console.log(`----- LAST WINNER: ${bingo}`);
            this.drawer.stop();
            return;
        }
    }

    private createBoards(boardInputs: number[][]) {
        for (let x = 0; x < boardInputs.length; x++) {
            this.boards.push(
                new BingoBoard(this.eventEmitter, boardInputs[x]));
        }
    }

    private createDrawer(numbersToDraw: number[]) {
        this.drawer = new Drawer(this.eventEmitter, numbersToDraw);
    }
}


(async () => {
    await new Solver().solve();
})();