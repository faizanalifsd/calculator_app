# Tasks: Basic Command-Line Calculator

**Input**: Design documents from `/specs/001-basic-calculator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

---

## Phase 1: Foundational (Blocking Prerequisites) - Core Logic (Already Completed)

**Purpose**: Core calculation logic that MUST be complete before any user story can be implemented.

- [x] T001 Implement `evaluate_expression` function in `src/calculator/core.py` to handle:
    - Addition, Subtraction, Multiplication, Division, Exponentiation
    - Order of operations (parentheses, precedence)
    - Division by zero error handling
    - Malformed expression error handling
- [x] T002 Write comprehensive unit tests for `src/calculator/core.py` in `tests/unit/test_core.py`
- [x] T003 Ensure all unit tests for core logic pass.

---

## Phase 2: User Story 1 - Perform a Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement an interactive command-line interface where users can input expressions and receive correct numerical results.

**Independent Test**: The feature can be tested by running the application, providing a valid mathematical expression (e.g., "5 * (2 + 3)"), and verifying that the output is the correct result (e.g., "25.0").

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T004 [P1] [US1] Integration test for valid expressions in `tests/integration/test_cli.py`
    - Test case: `(10 + 20) * 3` should output `90.0`
- [ ] T005 [P1] [US1] Integration test for division by zero in `tests/integration/test_cli.py`
    - Test case: `10 / 0` should output a specific error message.
- [ ] T006 [P1] [US1] Integration test for malformed expressions in `tests/integration/test_cli.py`
    - Test case: `5 * + 2` should output a specific error message.
    - Test case: `(10 + 5` should output a specific error message.
- [ ] T007 [P1] [US1] Integration test for empty input in `tests/integration/test_cli.py`
    - Test case: Empty input should re-prompt without error.
- [ ] T008 [P1] [US1] Integration test for quit command in `tests/integration/test_cli.py`
    - Test case: "quit" command should terminate the application gracefully.

### Implementation for User Story 1

- [ ] T009 [US1] Create CLI module `src/calculator/cli.py` to handle user interaction.
- [ ] T010 [US1] Implement main entry point `main.py` to run the CLI.
- [ ] T011 [US1] Implement input reading and prompting in `src/calculator/cli.py`.
- [ ] T012 [US1] Integrate `evaluate_expression` from `src/calculator/core.py` into `src/calculator/cli.py`.
- [ ] T013 [US1] Implement output display for results and error messages in `src/calculator/cli.py`.
- [ ] T014 [US1] Implement the "quit" command handling in `src/calculator/cli.py`.
- [ ] T015 [US1] Implement handling for empty or whitespace-only input in `src/calculator/cli.py`.
- [ ] T016 [US1] Add `__init__.py` to `src/calculator/` and `tests/integration/` to ensure proper package structure.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Foundational (Phase 1)**: Core Logic is already completed.
- **User Story 1 (Phase 2)**: Depends on Foundational (Phase 1) completion.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.
- Core implementation (done) before CLI integration.

### Parallel Opportunities

- All tests for User Story 1 can be written in parallel.
- Once tests are failing, CLI implementation tasks can be tackled.
