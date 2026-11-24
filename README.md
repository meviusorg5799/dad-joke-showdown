[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/meviusorg5799/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/meviusorg5799/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

# Dad Joke Showdown

Entry for the [Dad Joke Showdown bounty](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) on make.fun.

## Approach

One original dad joke, authored for this bounty and kept in `entry.txt`.
The joke is built around a concrete everyday scene a father would actually
talk about at the dinner table, with a single clean pun that lands on first
read and a punchline that arrives at the very end. `main.py` (Python 3.13,
standard library only, fully deterministic) reads the joke from `entry.txt`
and writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
when set), failing loudly if the text is not a single joke of 1–200
characters.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
