# Tonkotsu Ramen, Steaming Hot

A make.fun food-picture-01 entry by @ridwan-sumantoro.

## About the photograph

This entry is a professional food photograph centred on a bowl of rich tonkotsu ramen, served steaming hot. The creamy broth holds glossy slices of chashu pork, a jammy soft egg cut open, a scatter of fresh spring onions, and a swirl of chili oil on top. Warm, appetising light falls across the bowl, which sits on a dark rustic table that makes the colours of the dish stand out.

It is meant to feel immediate and inviting — the kind of bowl you want to pick up chopsticks for straight away.

## How it runs

The program is a small Python 3 script using only the standard library, with no network access.

When you run `python3 main.py`, it looks for `entry.png` next to the script and copies it into the output directory. That output directory is taken from the `MAKEFUN_OUTPUT_DIR` environment variable when it is set, and defaults to `/output` when it is not. The folder is created automatically if it does not already exist, and the copy is a plain byte-for-byte transfer, so the result is deterministic.

## License

MIT — see the `LICENSE` file in this repository for the full text.
