# Gherkin-FSM Extension

This document defines a minimal extension to Gherkin syntax for modeling finite state machines (FSMs) using valid Gherkin structure. It prioritizes human readability, tooling compatibility, and structured stateful behavior.

## 🎯 Purpose

Use Gherkin to express game rule logic as state transitions, enabling simulation, validation, and interactive flow modeling.

---

## ✨ Syntax Extensions

All syntax is valid Gherkin and can be parsed by standard tools, while being interpreted as FSM logic by custom engines.

### 1. `@start`

Declares the **single** FSM entrypoint.

```gherkin
@start
Scenario: Begin gameplay
  Then :initialize_game
```

There must be exactly one `@start` scenario per FSM.

---

### 2. `@from:<state>`

Declares one or more origin states for a transition.

```gherkin
@from:resolution_phase
@from:retry_requested
```

---

### 3. `Given :<truthy_guard>`

Declares a required condition or flag for the scenario to apply.

```gherkin
Given :player_has_animus
And :dice_pools_ready
```

- Colon `:` prefix distinguishes flags/conditions from natural language.
- All conditions must be truthy for the scenario to proceed.

---

### 4. `Then :<next_state> Else :<fallback_state>`

Declares a conditional binary transition:

```gherkin
Then :success Else :failure
```

- If all `Given` conditions pass, the FSM transitions to `success`.
- Otherwise, it transitions to `failure`.
- This avoids needing duplicated `Scenario` blocks for each branch.

---

### 5. `Then :END`

Marks a terminal state.

```gherkin
Then :END
```

This halts execution or exits the FSM cleanly.

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
@start
Scenario: Begin play
  Given :scene_is_active
  Then :player_turn

@from:player_turn
Scenario: Player acts
  Given :player_has_animus
  Then :success Else :failure

@from:success
Scenario: End of flow
  Then :END
```

---

## 💡 Parser Notes

A custom FSM engine should:
- Track state via `@start`, `@from:` and `Then`
- Interpret `:flag` steps as guard conditions
- Handle ternary transitions using `Then :X Else :Y`
- Recognize `Then :END` as a terminal state
