#!/usr/bin/env python3
"""Value model for text LLMs on AWS Bedrock and Google Vertex AI.

Data collected 2026-10-06 from:
  - Bedrock: aws.amazon.com/bedrock/pricing (rendered price map
    b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/...) + per-model cards under
    docs.aws.amazon.com/bedrock/latest/userguide/model-card-*.html
  - Vertex:  cloud.google.com/vertex-ai/generative-ai/pricing
  - Capability: artificialanalysis.ai per-model pages (Intelligence Index v4.x
    and AA's measured cost-per-Intelligence-Index-task)

Prices are USD per 1M tokens, cheapest routing tier on each platform
(Bedrock "Global CRIS" / Vertex "Global"). Regional/geo routing is ~+10%.
DeepSeek is listed at peak rates for comparability; --deepseek-offpeak halves them.

Platform tags are per *version*, not per family: GLM 5.3 is Bedrock-only while
Vertex carries GLM 5.2; MiniMax M2.5 is Bedrock-only while Vertex carries M2;
Kimi K3 is Bedrock-only while Vertex carries K2 Thinking.
"""

import argparse

# name, platform, input, output, cache_write_5m, cache_read, aa_index, aa_cost_per_task
# aa_index: Artificial Analysis Intelligence Index at the effort shown. None = not measured.
# aa_cost_per_task: AA's measured $/task on the Intelligence Index (includes reasoning tokens).
MODELS = [
    # ---- Anthropic (both platforms, identical list price) ----
    ("Claude Opus 5.5 (max)",      "both",    4.00, 20.00,  5.00, 0.20, 58,   5.98),
    ("Claude Opus 5.5 (high)",     "both",    4.00, 20.00,  5.00, 0.20, 54,   1.82),
    ("Claude Sonnet 5.5 (max)",    "both",    2.00, 10.00,  2.50, 0.20, 56,   7.67),
    ("Claude Sonnet 5.5 (high)",   "both",    2.00, 10.00,  2.50, 0.20, 47,   1.12),
    ("Claude Sonnet 5.5 (medium)", "both",    2.00, 10.00,  2.50, 0.20, 41,   0.59),
    ("Claude Opus 5 (max)",        "both",    5.00, 25.00,  6.25, 0.50, 51,   5.86),
    ("Claude Opus 5 (high)",       "both",    5.00, 25.00,  6.25, 0.50, 48,   3.61),
    ("Claude Sonnet 5 (max)",      "both",    2.00, 10.00,  2.50, 0.20, 38,   5.09),
    ("Claude Fable 5.1",           "both",   10.00, 50.00, 12.50, 0.25, 53,   7.63),
    ("Claude Opus 4.8",            "both",    5.00, 25.00,  6.25, 0.50, 42,   4.08),
    ("Claude Haiku 4.5",           "both",    1.00,  5.00,  1.25, 0.10, 17,   0.28),

    # ---- OpenAI (Bedrock only; Vertex has gpt-oss only) ----
    ("GPT-6.1 Sol (max)",          "bedrock", 2.00, 10.00,  2.50, 0.10, 52,   0.72),
    ("GPT-6.1 Sol (high)",         "bedrock", 2.00, 10.00,  2.50, 0.10, 50,   0.32),
    ("GPT-6 Astra",                "bedrock",10.00, 50.00, 12.50, 1.00, 53,   3.26),
    ("GPT-6 Sol (max)",            "bedrock", 2.00, 10.00,  2.50, 0.20, 48,   1.04),
    ("GPT-6 Sol (high)",           "bedrock", 2.00, 10.00,  2.50, 0.20, 42,   0.37),
    ("GPT-6 Luna",                 "bedrock", 0.10,  0.50,  0.125,0.01, 38,   0.07),
    ("GPT-5.6 Sol",                "bedrock", 4.00, 20.00,  5.00, 0.40, 47,   1.99),
    ("GPT-5.6 Terra",              "bedrock", 2.00, 12.00,  2.50, 0.20, 42,   1.40),
    ("GPT-5.6 Luna",               "bedrock", 0.20,  1.20,  0.25, 0.02, 37,   0.18),

    # ---- Google Gemini (Vertex only) ----
    ("Gemini 3.8 Flash*",          "vertex",  0.75,  3.75,  None, 0.075, 41,  1.24),
    ("Gemini 3.7 Flash*",          "vertex",  0.75,  3.75,  None, 0.075, 39,  0.93),
    ("Gemini 3.5 Flash",           "vertex",  1.50,  9.00,  None, 0.15,  33,  3.69),
    ("Gemini 3.1 Pro (preview)",   "vertex",  2.00, 12.00,  None, 0.20,  30,  1.30),
    ("Gemini 3.5 Flash-Lite",      "vertex",  0.30,  2.50,  None, 0.03,  None, None),
    ("Gemini 3.1 Flash-Lite",      "vertex",  0.25,  1.50,  None, 0.025, None, None),

    # ---- xAI (both) ----
    ("Grok 4.7",                   "both",    2.00,  6.00,  None, 0.50, 46,   3.74),
    ("Grok 4.6",                   "both",    2.00,  6.00,  None, 0.50, 44,   1.48),
    ("Grok 4.3",                   "both",    1.25,  2.50,  None, 0.20, None, None),
    ("Grok 4.1 Fast Reasoning",    "vertex",  0.20,  0.50,  None, 0.05, None, None),

    # ---- Open-weight / China-lab (both; Vertex list prices shown) ----
    ("GLM 5.3",                    "bedrock", 1.40,  4.40,  None, 0.14, 45,   2.01),
    ("GLM 5.2",                    "vertex",  1.40,  4.40,  None, 0.14, 34,   1.47),
    ("GLM 5",                      "both",    1.00,  3.20,  None, 0.10, None, None),
    ("Kimi K3 (Bedrock)",          "bedrock", 3.00, 15.00,  3.75, 0.30, 44,   2.00),
    ("Kimi K2 Thinking (Vertex)",  "vertex",  0.60,  2.50,  None, 0.06, None, None),
    ("MiniMax M2.5",               "bedrock", 0.30,  1.20,  None, 0.03, 23,   None),
    ("DeepSeek V3.2",              "both",    0.56,  1.68,  None, 0.056, 21,  None),
    ("Qwen3 Coder 480B",           "both",    0.22,  1.80,  None, 0.022, None, None),

    # ---- DeepSeek direct API (NOT on Bedrock or Vertex) ----
    # PEAK rates, to stay comparable with every other row (which is list price).
    # Off-peak is half of these and covers all hours outside 01:00-04:00 and
    # 06:00-10:00 UTC Mon-Fri, plus weekends and Chinese public holidays in full --
    # so most hours bill at half. Apply --deepseek-offpeak to see that case.
    ("DeepSeek V4.1 Flash",        "deepseek", 0.30,  1.20,  None, 0.006, 39,  0.27),
    ("DeepSeek V4 Flash",          "deepseek", 0.44,  1.32,  None, 0.013, 34,  0.22),
    ("DeepSeek V4 Pro",            "deepseek", 1.32,  3.96,  None, 0.044, 36,  0.67),
    ("DeepSeek V4 Pro (non-think)","deepseek", 1.32,  3.96,  None, 0.044, 20,  0.48),

    # ---- Amazon / Meta / Mistral ----
    ("Amazon Nova 2 Lite",         "bedrock", 0.30,  2.50,  None, 0.075, 13,  None),
    ("Llama 4 Maverick",           "both",    0.24,  0.97,  None, None,  10,  None),
    ("Mistral Large 3",            "both",    0.50,  1.50,  None, 0.05,  9,   0.03),
]


def workload_cost(m, prefix, hit, out_tok, turns):
    """Cost of one task: `turns` turns, each resending `prefix` tokens
    (`hit` fraction served from cache) and producing `out_tok` output tokens."""
    _, _, pin, pout, pcw, pcr = m[:6]
    if pcr is None:                     # no caching available
        hit = 0.0
        pcr = pin
    cached = prefix * hit
    fresh = prefix - cached
    per_turn = (cached * pcr + fresh * pin + out_tok * pout) / 1e6
    # pcw None means the provider charges no separate cache-write fee (Gemini's
    # implicit cache, Grok, GLM, Kimi K2, MiniMax, DeepSeek, Qwen, Mistral, Llama).
    # Only Claude, OpenAI and Kimi K3 bill a write, and those carry an explicit rate.
    write_once = (prefix * pcw) / 1e6 if (hit and pcw) else 0.0
    return per_turn * turns + write_once


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--platform", choices=["bedrock", "vertex", "deepseek", "all"], default="all")
    p.add_argument("--prefix", type=int, default=60000, help="tokens resent per turn")
    p.add_argument("--hit", type=float, default=0.90, help="cache hit rate on the prefix")
    p.add_argument("--output", type=int, default=3000, help="output tokens per turn")
    p.add_argument("--turns", type=int, default=40, help="turns per task")
    p.add_argument("--floor", type=float, default=0.0, help="min AA Intelligence Index")
    p.add_argument("--sort", choices=["index", "cost", "value"], default="index")
    p.add_argument("--deepseek-offpeak", action="store_true",
                   help="halve DeepSeek rates (its off-peak window covers most hours)")
    a = p.parse_args()

    if not 0.0 <= a.hit <= 1.0:
        p.error("--hit must be between 0 and 1")
    if a.prefix < 0 or a.output < 0 or a.turns < 1:
        p.error("--prefix and --output must be >= 0, --turns >= 1")

    rows = []
    for m in MODELS:
        name, plat = m[0], m[1]
        if a.deepseek_offpeak and plat == "deepseek":
            m = (m[0], m[1], m[2] / 2, m[3] / 2, m[4], m[5] / 2 if m[5] else None,
                 m[6], m[7] / 2 if m[7] else None)
        # "both" means Bedrock and Vertex -- it does not include the DeepSeek
        # direct API, which carries only the models tagged "deepseek".
        if a.platform != "all":
            shared = plat == "both" and a.platform in ("bedrock", "vertex")
            if plat != a.platform and not shared:
                continue
        idx = m[6]
        if a.floor and (idx is None or idx < a.floor):
            continue
        cost = workload_cost(m, a.prefix, a.hit, a.output, a.turns)
        rows.append({
            "name": name, "plat": plat, "idx": idx, "cost": cost,
            "aa": m[7], "ppd": (idx / cost) if idx else None,
        })

    key = {"index": lambda r: -(r["idx"] or 0),
           "cost": lambda r: r["cost"],
           "value": lambda r: -(r["ppd"] or 0)}[a.sort]
    rows.sort(key=key)

    print(f"workload: {a.turns} turns x ({a.prefix:,}-token prefix @ {a.hit:.0%} cached "
          f"+ {a.output:,} out)   platform={a.platform}")
    print(f"{'model':<30}{'plat':<9}{'AAidx':>6}{'$/task':>9}{'idx/$':>8}{'AA $/task':>11}")
    print("-" * 73)
    for r in rows:
        idx = str(r["idx"]) if r["idx"] is not None else "-"
        ppd = f"{r['ppd']:.1f}" if r["ppd"] else "-"
        aa = f"{r['aa']:.2f}" if r["aa"] else "-"
        print(f"{r['name']:<30}{r['plat']:<9}{idx:>6}{r['cost']:>9.3f}{ppd:>8}{aa:>11}")


if __name__ == "__main__":
    main()
