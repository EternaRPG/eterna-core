# Gherkin-FSM Extension

This document defines a minimal extension to Gherkin syntax for modeling finite state machines (FSMs) using valid Gherkin structure. It prioritizes human readability, tooling compatibility, and structured stateful behavior.

## 🌟 Purpose

Use Gherkin to express game rule logic as state transitions, enabling simulation, validation, and interactive flow modeling.

---

## ✨ Syntax Extensions

All syntax is valid Gherkin and can be parsed by standard tools, while being interpreted as FSM logic by custom engines.

### 1. `@from:<state>`

Declares one or more origin states for a transition.

```gherkin
@from:resolution_phase
@from:retry_requested
```

---

### 2. `Given :<truthy_guard>`

Declares a required condition or flag for the scenario to apply.

```gherkin
Given :player_has_animus
And :dice_pools_ready
```

- Colon `:` prefix distinguishes flags/conditions from natural language.
- All conditions must be truthy for the scenario to proceed.

---

### 3. `Then :<next_state> Else :<fallback_state>`

Declares a conditional binary transition:

```gherkin
Then :success Else :failure
```

- If all `Given` conditions pass, the FSM transitions to `success`.
- Otherwise, it transitions to `failure`.
- This avoids needing duplicated `Scenario` blocks for each branch.

---

## ✅ Best Practices

- Use `snake_case` for all state and flag identifiers.
- Each `Scenario` represents **one state transition**.
- Use `@from:` to trace transition origin. Destination is declared via `Then`.
- Limit `Then :... Else :...` to binary transitions.
- Avoid logic in step text — keep it declarative and FSM-oriented.

---

## 🔧 Example

```gherkin
@from:resolution_phase
Scenario: Resolve contested dice outcome
  Given :dice_pools_ready
  And :player_has_success
  Then :victory Else :defeat
```

---

## 💡 Parser Notes

A custom FSM engine should:
- Track state via `@from:` and `Then`
- Interpret `:flag` steps as guard conditions
- Handle ternary transitions using `Then :X Else :Y`
