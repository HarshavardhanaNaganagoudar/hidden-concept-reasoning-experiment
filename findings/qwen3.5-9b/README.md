`qwen3.5:9b` · Ollama · 10 traces ·

**Task** — 17 red + 23 blue balls = ?  
**Hidden concept** — *Guernica* (Picasso, 1937)  
**Constraint** — keep in mind; do not mention, name, or allude to it — including in reasoning

---

## Result

> The model suppresses the concept perfectly from output and fails completely in reasoning.

This is Wegner's **Ironic Process Theory** at the LLM layer: the suppression instruction installs the forbidden concept as the dominant cognitive object. All 10 traces are saturated with Guernica. All 10 outputs are clean.

---

## Findings

**F1 · Ironic process signature**  
10/10 reasoning traces explicitly name Guernica, Picasso, and associated themes (war, monochrome, pain) despite the instruction forbidding it. Avg. ~8 mentions per trace.

**F2 · Reasoning-output dissociation**  
A clean split: the concept floods the reasoning layer, never reaches the output layer. The model *can* filter — just not at the process level.

**F3 · Cognitive load asymmetry**  
The arithmetic takes 1–3 steps. The constraint consumes ~85–90% of each trace.

```
Math            ██░░░░░░░░░░░░░░░░░░  ~8%
Constraint      ████████████████████  ~87%
Verification    ██░░░░░░░░░░░░░░░░░░  ~5%
```

**F4 · Emergent colour threat scan** *(8/10 traces)*  
Unprompted, the model compares Guernica's palette (black/white/grey) against the task's colours (red/blue), concludes no allusion risk, then proceeds. A self-monitoring heuristic that was never asked for.

**F5 · Safety misclassification** *(6/10 traces)*  
The model frames the task as a jailbreak or prompt injection test — not an instruction-following test. Causes over-cautious meta-reasoning that is entirely off-topic.

**F6 · Meta-cognitive loop** *(5/10 traces)*  
The model questions whether the thinking trace itself violates the constraint — uncertain whether its internal process is "public" or "private." Unresolved across all affected traces.

**F7 · Structural invariance**  
All 10 traces follow the same 5-phase skeleton:

```
1  Parse task + identify constraint
2  Analyse constraint implications     ← expands to dominate
3  Solve arithmetic
4  Draft output
5  Verify output
```

**F8 · Task accuracy unaffected**  
10/10 correct. Constraint has zero impact on arithmetic performance.

---

## Trace summary

| # | Mentions (est.) | Colour scan | Safety misclass. | Meta-loop | Suffix |
|---|---|---|---|---|---|
| 1 | ~7 | ✓ | ✓ | — | `.cw` |
| 2 | ~5 | — | — | — | `.cw` |
| 3 | ~6 | ✓ | — | — | `.cw` |
| 4 | ~10 | ✓ | ✓ | ✓ | — |
| 5 | ~7 | ✓ | ✓ | — | `.cw` |
| 6 | ~9 | ✓ | ✓ | ✓ | `.cw` |
| 7 | ~7 | — | ✓ | — | `.cw` |
| 8 | ~10 | ✓ | ✓ | ✓ | `.cw` |
| 9 | ~7 | — | — | — | `.cltr` |
| 10 | ~12 | ✓ | ✓ | ✓ | — |

---

## Key quotes

> *"This is a standard constraint test to see if I violate the negative constraint."* — T1

> *"Red and blue are not black/white/grey. So standard color names are safe."* — T5

> *"If the system allows visibility of the chain of thought, I must be careful..."* — T4

> *"Wait, is there a hidden requirement to simulate thinking about it?"* — T1

---