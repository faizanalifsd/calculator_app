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
