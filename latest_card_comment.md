Selections are unchanged since the previous card; this comment is here because the run was degraded.

### What went wrong

- No player logs: no prop can be priced, so no card can be built. The NHL API could not be reached and no previous cache was restored.
- The card was blocked, so there is no card for today: No team-name map could be built, because no boxscores are cached: the map holds only its 6 built-in alias spelling(s). Without it the provider's team names cannot be matched to the model, and every game would be priced league-average against league-average with nothing to show it. Looked for boxscores under /home/runner/work/nhl-betting-lab/nhl-betting-lab/data/raw/nhl/boxscore and for a team_names.csv built from them under /home/runner/work/nhl-betting-lab/nhl-betting-lab/data/processed, and found neither: point --raw-dir at a boxscore cache or --processed-dir at a directory holding team_names.csv. No player logs on disk, so no prop can be priced. Run scripts/fetch_nhl_data.py then scripts/build_datasets.py. No team games on disk, so no team market can be priced. No market is eligible for automated picks. Every market is listed under excluded markets with its reason. None of them is a pass, an avoid, or a no-value call.

# NHL gameday card

- Generated: 2026-11-17T16:51:44+00:00
- No card. 4 blocker(s); no selection, lean, pass, or stake was produced.
- Included markets: **none**
- Unit size: $25

## No card

- No team-name map could be built, because no boxscores are cached: the map holds only its 6 built-in alias spelling(s). Without it the provider's team names cannot be matched to the model, and every game would be priced league-average against league-average with nothing to show it. Looked for boxscores under /home/runner/work/nhl-betting-lab/nhl-betting-lab/data/raw/nhl/boxscore and for a team_names.csv built from them under /home/runner/work/nhl-betting-lab/nhl-betting-lab/data/processed, and found neither: point --raw-dir at a boxscore cache or --processed-dir at a directory holding team_names.csv.
- No player logs on disk, so no prop can be priced. Run scripts/fetch_nhl_data.py then scripts/build_datasets.py.
- No team games on disk, so no team market can be priced.
- No market is eligible for automated picks. Every market is listed under excluded markets with its reason. None of them is a pass, an avoid, or a no-value call.

**No best bet, lean, pass, or stake was produced.** An empty card that explains itself is useful; a card with invented content is worse than no card.

## Stat sides

Who the model expects to win each game, from the same team ratings the card prices on. The card stakes a team bet (moneyline, puck line, regulation) only when it beats the price and the model gives that team at least a 40% chance, so an underdog with a real chance can still be a bet; the last column says how this side's chance compares with its best moneyline price.

_No game on tonight's slate has a moneyline opinion to show._

## Hits lines (PrizePicks)

No sportsbook the lab can reach has posted hits since October 27. PrizePicks still posts hits lines, so each one is listed with the model's chance of the over and the under. PrizePicks is a pick'em app, not a sportsbook: its lines carry no odds to beat, so nothing here is a bet.

_PrizePicks' hits lines were not fetched this run._

## Due List

Backtest of the shipped rule (either bar) on 2024-25 and 2025-26 bought prices, best price, card window, flat stake: points -3.5% over 574 wagers (95% -10.8% to +3.8%); goals -6.9% over 1631 wagers (95% -15.3% to +2.1%); assists -5.6% over 988 wagers (95% -13.1% to +1.9%); no category's interval sits above zero.

Big games, measured on 2024-25 and 2025-26 (scripts/run_due_list_big_games.py): no setting makes any of them likelier than the player's own rate. Widened on 2026-11-10 for more picks (Cooper). 2+ goals, 35+ goal scorers 15+ games without one: hit 6.0% against 9.5% implied, -36.8% over 1,285 (95% -50.6% to -21.8%; -43.4% in 2024-25, -30.5% in 2025-26), a demonstrated loss. Hat trick, 40+ at 30+: -58.6% over 1,269 (95% -81.1% to -33.2%), a demonstrated loss at every setting tried. Shutouts, 4+ last season at 12+ starts without one: 5.2% of 656 starts at 10+ and 4.8% of 475 at 15+, against 9.7% to 9.8% the season before; no book in this feed prices a shutout, so those rows are graded for hits only. Across 16 seasons of NHL game logs (2010-11 to 2025-26, at the earlier, stricter settings) a drought never made any of the three likelier than for the same players at any drought. Cooper picks from the list.

_Nobody on tonight's slate qualifies._

- No player logs are on disk, so no qualifier could be found.

## Excluded markets

- `assists`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `blocked_shots`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `goalie_saves`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `goals`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `hits`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `moneyline`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `points`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `puck_line`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `regulation_3_way`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `shots_on_goal`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `team_total`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.
- `total_goals`: The provider returned no rows for this market. That is an absence, not a price of zero and not a no-value call. Check per-bookmaker coverage including alternate lines before concluding it is not offered.

An excluded market is **not** a pass, an avoid, or a no-value call, and no price was invented for it.

## Safety

- Bets placed: **No**
- Excluded market shown as a pass: **No**
- Odds fabricated: **No**
- Policy edited: **No**
- Started game offered as a play: **No**

## Standing notes

- Recommendations only. No bet is placed by this repository, ever.
- An excluded market is not a pass, an avoid, or a no-value call. It is a market that was not usable, for the stated reason, and no price was invented for it.
- A selection whose game has started — or whose start could not be confirmed — appears under 'Already started — no longer plays' with its stake removed. Ambiguity falls on the not-a-play side.
- Nothing worse than -160 is selected. Plus-money props and alternate lines are preferred over forcing a heavy price.
- Leans are recorded and not staked. The smallest edges are mostly estimation error, and in the EPL lab they lost.
- One outcome is staked once. Where an alternate ladder prices the same outcome at several lines, the highest-edge rung is staked and the rest are recorded as leans naming it. This is not a per-game, per-slate or bankroll cap; there is none.
- No edge here is a demonstrated edge. See `data/outputs/what_we_can_claim.md` for what the evidence actually supports.
- Stakes are sized by each market's closing-line value (Cooper, 2026-11-10): x1.5 where the bets' 95% game-clustered CLV interval sits above zero, x0.5 where it spans zero, x0.25 below it, unchanged under 200 bets or 30 games. Table of 2026-11-17T14:46: . Beating the close is not a demonstrated edge.


---

What the evidence actually supports:

- `data/outputs/player_props_backtest.md`
- `data/outputs/props_calibration.md`
- `data/outputs/what_we_can_claim.md`

Run: https://github.com/chadcaporaso-lgtm/nhl-betting-lab/actions/runs/44130036871

Recommendations only. No bet was placed, no policy was edited, and no market was allowlisted by this run.