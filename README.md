# Where the next dollar goes furthest

We run **Claude Sonnet 5.5 at `high`**, on **$200 / person / month**. This ranks every
model on Bedrock and Vertex by *capability per dollar* - Artificial Analysis
Intelligence Index ÷ measured cost to complete the Index suite - against that baseline.

**Our default buys 179 tasks per $200 and ranks 12th of 32.**

Interactive table: [`index.html`](index.html) ·
Calculator: [`platform-models.py`](platform-models.py) · Prices 2026-10-06.

---

## 1. The best setting Anthropic sells is 8th overall

`medium` is the most efficient configuration Anthropic offers - ahead of our `high`
default, ahead of `max`, ahead of Haiku. It still places only **8th of 32**.

| | Index | $/task | Index per $ | Tasks per $200 |
|---|--:|--:|--:|--:|
| **GPT-6 Luna** | 38 | $0.07 | **543** | 2,857 |
| GPT-5.6 Luna | 37 | $0.18 | 206 | 1,111 |
| GPT-6.1 Sol `high` | 50 | $0.32 | 156 | 625 |
| DeepSeek V4 Flash | 34 | $0.22 | 155 | 909 |
| DeepSeek V4.1 Flash | 39 | $0.27 | 144 | 741 |
| GPT-6 Sol `high` | 42 | $0.37 | 114 | 541 |
| GPT-6.1 Sol `max` | 52 | $0.72 | 72 | 278 |
| **Claude Sonnet 5.5 `medium`** | 41 | $0.59 | **69** | 339 |

**GPT-6 Luna runs 8.4× more tasks per dollar than our best Anthropic setting** - at
index 38 vs 41, so near-identical capability.

---

## 2. `effort` swings the bill 13×, and `max` is the wrong lever

Same model, same rate card. Only the effort setting changes.

| Sonnet 5.5 | Index | $/task | Index per $ | Rank | Tasks per $200 |
|---|--:|--:|--:|--:|--:|
| `medium` | 41 | $0.59 | 69 | 8th | 339 |
| `high` | 47 | $1.12 | 42 | 12th | 179 |
| `max` | 56 | $7.67 | 7 | **last** | 26 |

The same comparison moves with it: GPT-6 Luna is **16× more** value than Sonnet 5.5 at
`high`, and **110× more** at `max`.

**If you need `max`, do not use Sonnet.** Opus 5.5 is both cheaper and smarter there:

| vs Sonnet 5.5 `max` | Index | $/task | Value |
|---|--:|--:|--:|
| Claude Sonnet 5.5 `max` | 56 | $7.67 | baseline |
| **Claude Opus 5.5 `max`** | **58** | $5.98 | **1.3× more** - higher index, lower cost |
| **Claude Opus 5.5 `high`** | 54 | $1.82 | **4.2× more** - for 2 index points |

Sonnet 5.5 at `max` sits at the bottom of the whole table, level with Fable 5.1 - both
at 7 index per $ and 26 tasks per $200. We default to `high`, so this is an **escalation
guardrail**: `max` must never be the answer to "this needs more capability." Opus 5.5 at
`high` gets you index 54 for $1.82 - seven points above our default at a quarter the cost
of Sonnet `max`. Pin effort per route, not just model per route.

---

## 3. The cheap tier is owned by models we cannot buy

Everything under $0.30/task, by capability:

| Model | Index | $/task | Index per $ | Platform |
|---|--:|--:|--:|---|
| **DeepSeek V4.1 Flash** | **39** | $0.27 | 144 | **direct API only** |
| GPT-6 Luna | 38 | $0.07 | 543 | Bedrock |
| GPT-5.6 Luna | 37 | $0.18 | 206 | Bedrock |
| DeepSeek V4 Flash | 34 | $0.22 | 155 | **direct API only** |
| Claude Haiku 4.5 | 17 | $0.28 | 61 | both |

**DeepSeek V4.1 Flash is the most capable model at any price under $0.30** - index 39,
beating GPT-6 Luna, GPT-5.6 Luna and more than doubling Haiku 4.5. The V4 family is on
**neither Bedrock nor Vertex**; both platforms stop at V3.2. Using it means a direct
vendor relationship in another jurisdiction - a compliance review, not a procurement line.

Haiku 4.5 is the only Anthropic entry in this tier and it is not competitive: index 17
against 34–39 for everything else at the same money.

---

## 4. OpenAI wins on value at every tier

GPT takes the top 3 and 4 of the top 6. The cleanest comparison is at an **identical
rate card** - GPT-6.1 Sol and Sonnet 5.5 both list at $2 in / $10 out:

| | Index | $/task | Index per $ | Tasks per $200 |
|---|--:|--:|--:|--:|
| **GPT-6.1 Sol `high`** | **50** | **$0.32** | **156** | **625** |
| Claude Sonnet 5.5 `high` | 47 | $1.12 | 42 | 179 |

Higher index, **3.5× the budget life, same price per token.** The entire gap is
reasoning-token burn - how much each model generates to reach an answer.

**GPT-6.1 Sol is Bedrock-only.** Gemini is Vertex-only. Claude and Grok are on both at
identical prices; GLM, Kimi and MiniMax are on both but *not version-matched* (Bedrock
has GLM 5.3 / Kimi K3 / MiniMax M2.5, Vertex has GLM 5.2 / K2 Thinking / M2).

---

## What we should do

We default to Sonnet 5.5 at `high` - 179 tasks per $200, 12th of 32. Four moves from there:

1. **Pilot GPT-6.1 Sol at `high` on Bedrock.** Strictly better on both axes: index 50 vs
   47, and 625 tasks per $200 vs 179 - **3.5× the budget life at a higher score**, on an
   identical rate card. This is the only change that costs us nothing in capability.
2. **Drop routine work to Sonnet 5.5 `medium`.** 339 tasks per $200 - **1.9× our current
   budget life** for 6 index points. Free to pull, same model, same platform.
3. **Escalate to Opus 5.5 `high`, never Sonnet 5.5 `max`.** Index 54 at $1.82 beats index
   56 at $7.67 for any realistic purpose, and costs a quarter as much.
4. **Route bulk classification and extraction to GPT-6 Luna.** 2,857 tasks per $200.

Before committing: **measure our cache hit rate and output tokens per turn.** Those two
numbers move the per-seat answer more than the choice between any two models here.

---

## What this does not tell you

- **$/task is Artificial Analysis's benchmark suite, not our workload.** It is a
  relative-value index. Our actual per-seat cost depends on cache hit rate and output
  volume, neither of which we have measured. A 40-turn agent task on Sonnet 5.5 costs
  $2.26 at a 90% cache hit and $6.00 with caching off - a bigger swing than most model
  switches.
- **One composite score.** The Index says nothing about tool-use reliability over long
  runs, long-context behaviour, or latency - often what decides whether an agent is
  usable. Run our own evals before committing.
- **AA's harness, prompts and repeat policy were not independently verified**, and
  reasoning burn is prompt-dependent. Our $/task will land somewhere else.
- **Catalog availability ≠ entitlement.** Both platforms gate models per account and
  region. Prices move; re-pull before committing budget.

---

## Every model, ranked by capability per dollar

All 32 measured models, best value first. **Budget** compares each against our
default, **Claude Sonnet 5.5 at `high`** ($1.12/task, 179 tasks per $200) - how much
further or shorter the same $200 goes. Sortable version:
[`index.html`](index.html).

| Model (effort) | Where | Index | $/task | Index per $ | Tasks per $200 | Budget vs Sonnet 5.5 `high` | Input | Output | Cache read | Cache saving | Context |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| GPT-6 Luna | Bedrock | 38 | $0.07 | 543 | 2,857 | **16× more** | $0.10 | $0.50 | $0.01 | 90% | 1.05M |
| GPT-5.6 Luna | Bedrock | 37 | $0.18 | 206 | 1,111 | **6.2× more** | $0.20 | $1.20 | $0.02 | 90% | 1.05M |
| GPT-6.1 Sol (high) | Bedrock | 50 | $0.32 | 156 | 625 | **3.5× more** | $2.00 | $10.00 | $0.10 | 95% | 1M |
| DeepSeek V4 Flash | Direct | 34 | $0.22 | 155 | 909 | **5.1× more** | $0.44 | $1.32 | $0.013 | 97% | 1M |
| DeepSeek V4.1 Flash | Direct | 39 | $0.27 | 144 | 741 | **4.1× more** | $0.30 | $1.20 | $0.006 | 98% | 1M |
| GPT-6 Sol (high) | Bedrock | 42 | $0.37 | 114 | 541 | **3.0× more** | $2.00 | $10.00 | $0.20 | 90% | 1.05M |
| GPT-6.1 Sol (max) | Bedrock | 52 | $0.72 | 72 | 278 | **1.6× more** | $2.00 | $10.00 | $0.10 | 95% | 1M |
| Claude Sonnet 5.5 (medium) | Both | 41 | $0.59 | 69 | 339 | **1.9× more** | $2.00 | $10.00 | $0.20 | 90% | 1M |
| Claude Haiku 4.5 | Both | 17 | $0.28 | 61 | 714 | **4.0× more** | $1.00 | $5.00 | $0.10 | 90% | 200K |
| DeepSeek V4 Pro | Direct | 36 | $0.67 | 54 | 299 | **1.7× more** | $1.32 | $3.96 | $0.044 | 97% | 1M |
| GPT-6 Sol (max) | Bedrock | 48 | $1.04 | 46 | 192 | **1.1× more** | $2.00 | $10.00 | $0.20 | 90% | 1.05M |
| Claude Sonnet 5.5 (high) | Both | 47 | $1.12 | 42 | 179 | **baseline** | $2.00 | $10.00 | $0.20 | 90% | 1M |
| Gemini 3.7 Flash | Vertex | 39 | $0.93 | 42 | 215 | **1.2× more** | $0.75 | $3.75 | $0.075 | 90% | 1M |
| Gemini 3.8 Flash | Vertex | 41 | $1.24 | 33 | 161 | 1.1× less | $0.75 | $3.75 | $0.075 | 90% | 1M |
| GPT-5.6 Terra | Bedrock | 42 | $1.40 | 30 | 143 | 1.2× less | $2.00 | $12.00 | $0.20 | 90% | 1.05M |
| Grok 4.6 | Both | 44 | $1.48 | 30 | 135 | 1.3× less | $2.00 | $6.00 | $0.50 | 75% | 500K |
| Claude Opus 5.5 (high) | Both | 54 | $1.82 | 30 | 110 | 1.6× less | $4.00 | $20.00 | $0.20 | 95% | 1M |
| GPT-5.6 Sol | Bedrock | 47 | $1.99 | 24 | 101 | 1.8× less | $4.00 | $20.00 | $0.40 | 90% | 1.05M |
| GLM 5.2 † | Vertex | 34 | $1.47 | 23 | 136 | 1.3× less | $1.40 | $4.40 | $0.14 | 90% | 1M |
| Gemini 3.1 Pro (preview) | Vertex | 30 | $1.30 | 23 | 154 | 1.2× less | $2.00 | $12.00 | $0.20 | 90% | 1M |
| GLM 5.3 † | Bedrock | 45 | $2.01 | 22 | 100 | 1.8× less | $1.40 | $4.40 | $0.14 | 90% | 1M |
| Kimi K3 † | Bedrock | 44 | $2.00 | 22 | 100 | 1.8× less | $3.00 | $15.00 | $0.30 | 90% | 1M |
| GPT-6 Astra | Bedrock | 53 | $3.26 | 16 | 61 | 2.9× less | $10.00 | $50.00 | $1.00 | 90% | 1.05M |
| Claude Opus 5 (high) | Both | 48 | $3.61 | 13 | 55 | 3.2× less | $5.00 | $25.00 | $0.50 | 90% | 1M |
| Grok 4.7 | Both | 46 | $3.74 | 12 | 53 | 3.3× less | $2.00 | $6.00 | $0.50 | 75% | 500K |
| Claude Opus 4.8 | Both | 42 | $4.08 | 10 | 49 | 3.6× less | $5.00 | $25.00 | $0.50 | 90% | 1M |
| Claude Opus 5.5 (max) | Both | 58 | $5.98 | 10 | 33 | 5.3× less | $4.00 | $20.00 | $0.20 | 95% | 1M |
| Gemini 3.5 Flash | Vertex | 33 | $3.69 | 9 | 54 | 3.3× less | $1.50 | $9.00 | $0.15 | 90% | 1M |
| Claude Opus 5 (max) | Both | 51 | $5.86 | 9 | 34 | 5.2× less | $5.00 | $25.00 | $0.50 | 90% | 1M |
| Claude Sonnet 5 (max) | Both | 38 | $5.09 | 7 | 39 | 4.5× less | $2.00 | $10.00 | $0.20 | 90% | 1M |
| Claude Sonnet 5.5 (max) | Both | 56 | $7.67 | 7 | 26 | 6.8× less | $2.00 | $10.00 | $0.20 | 90% | 1M |
| Claude Fable 5.1 | Both | 53 | $7.63 | 7 | 26 | 6.8× less | $10.00 | $50.00 | $0.25 | 98% | 1M |

**Index per $** is a blunt ratio - it rewards cheapness regardless of whether the
score clears our bar, which is why an index-38 model tops it. Set a capability floor
first, then optimise cost beneath it.

**$/task** is the measured cost of completing the whole Artificial Analysis
Intelligence Index suite, reasoning tokens included. **Rates** are the cheapest
routing tier (Bedrock *Global CRIS*, Vertex *Global*); regional and geo routing is
+10% on both. DeepSeek is shown at peak rates - off-peak is half.

† Marketplace-billed on Bedrock; rates not published on the main pricing page, so
Artificial Analysis's listed rate is shown.

Measured but below the index-17 floor, so excluded: Mistral Large 3 (index 9, $0.03)
and Qwen3 Coder Next (index 9, $0.55). AA-*estimated* rather than measured, so also
excluded: MiniMax M2.5 ≈23, DeepSeek V3.2 ≈21, Amazon Nova 2 Pro ≈14, Nova 2 Lite ≈13,
Llama 4 Maverick ≈10.
