Feature: Contested Dice Resolution

  As an actor in a contested action
  I want to resolve effort and resistance step-by-step
  So that any contest produces a clear, fair outcome

  @from:start
  Scenario: Actor declares an action
    Given :actor_has_declared_intent
    Then :action_declared

  @from:action_declared
  Scenario: Actor builds dice pool
    Given :actor_is_active
    Then :build_actor_dice_pool

  @from:build_actor_dice_pool
  Scenario: Actor rolls dice
    Given :actor_dice_pool_ready
    Then :actor_dice_rolled

  @from:actor_dice_rolled
  Scenario: Opposition builds dice pool
    Given :opposition_is_active
    Then :build_opposition_dice_pool

  @from:build_opposition_dice_pool
  Scenario: Resolve one opposition die against actor
    Given :opposition_has_dice_remaining
    Then :resolve_next_opposition_die Else :dice_resolution_complete

  @from:resolve_next_opposition_die
  Scenario: Cancel actor die with opposition roll
    Given :opposition_rolls_next_die
    Then :evaluate_opposition_roll

  @from:evaluate_opposition_roll
  Scenario: Determine if opposition die cancels actor die
    Given :opposition_roll_successfully_cancels
    Then :cancel_highest_actor_die Else :next_opposition_roll

  @from:next_opposition_roll
  Scenario: Loop to next opposition die
    Given :opposition_has_dice_remaining
    Then :resolve_next_opposition_die Else :dice_resolution_complete

  @from:dice_resolution_complete
  Scenario: Contest is fully resolved
    Given :all_dice_resolved
    Then :action_resolution_ready
