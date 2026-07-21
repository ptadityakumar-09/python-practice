# 📝 Python Day 4 Notes

## What are Conditional Statements?

Conditional statements allow a program to make decisions based on conditions.

Example:

```python
age = 18

if age >= 18:
    print("Eligible for voting")
```

---

# Types of Conditional Statements

## 1. if Statement

Executes a block of code only if the condition is True.

Syntax:

```python
if condition:
    # code
```

---

## 2. if-else Statement

Executes one block if the condition is True, otherwise executes another block.

Syntax:

```python
if condition:
    # code
else:
    # code
```

---

## 3. if-elif-else Statement

Used when multiple conditions need to be checked.

Syntax:

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

---

## 4. Nested if

An `if` statement inside another `if` statement.

Example:

```python
if age >= 18:
    if age >= 21:
        print("Eligible")
```

---

## Indentation

Python uses indentation to define blocks of code.

Correct:

```python
if True:
    print("Hello")
```

Incorrect:

```python
if True:
print("Hello")
```

---

## Key Points

- Every condition returns `True` or `False`.
- Indentation is mandatory in Python.
- `elif` is used for multiple conditions.
- `else` executes when no condition is True.

---

## Common Mistakes

- Forgetting indentation.
- Using `=` instead of `==`.
- Incorrect ordering of conditions.
- Missing `:` after `if`, `elif`, or `else`.

---

## Quick Revision

- `if` → One condition
- `if-else` → Two choices
- `if-elif-else` → Multiple choices
- Nested `if` → Condition inside another condition