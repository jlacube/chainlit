import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat with a welcome message and sample training activity."""

    # Create a training activity with markdown-formatted question and answer
    training_element = cl.TrainingActivityElement(
        question="""**What is the output of the following Python code?**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
```

*Think step by step about how recursion works here.*""",
        hidden_answer="""**Answer: 5**

The recursive function calculates the 5th Fibonacci number:
- `fibonacci(5)` = `fibonacci(4)` + `fibonacci(3)`
- `fibonacci(4)` = 3, `fibonacci(3)` = 2
- So `fibonacci(5)` = 3 + 2 = **5**

The Fibonacci sequence is: 0, 1, 1, 2, 3, **5**, 8, 13...""",
        user_answer=None,
        revealed=False,
        name="Python Recursion Challenge",
    )

    await cl.Message(
        content="Welcome to the Training Activity Demo! Here's a Python recursion challenge:",
        elements=[training_element],
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Handle user messages and provide more training examples."""

    if "math" in message.content.lower():
        # Math training activity with LaTeX
        training_element = cl.TrainingActivityElement(
            question="""**Solve for x in the quadratic equation:**

$$ax^2 + bx + c = 0$$

Given: $2x^2 - 5x + 2 = 0$

*Use the quadratic formula: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$*""",
            hidden_answer="""**Solution:**

Using the quadratic formula with $a = 2$, $b = -5$, $c = 2$:

$$x = \\frac{-(-5) \\pm \\sqrt{(-5)^2 - 4(2)(2)}}{2(2)}$$

$$x = \\frac{5 \\pm \\sqrt{25 - 16}}{4}$$

$$x = \\frac{5 \\pm \\sqrt{9}}{4} = \\frac{5 \\pm 3}{4}$$

Therefore: $x = 2$ or $x = \\frac{1}{2}$""",
            user_answer=None,
            revealed=False,
            name="Quadratic Equations",
        )

        await cl.Message(
            content="Here's a math challenge with LaTeX formatting:",
            elements=[training_element],
        ).send()

    elif "algorithm" in message.content.lower():
        # Algorithm training activity
        training_element = cl.TrainingActivityElement(
            question="""**What is the time complexity of this algorithm?**

```python
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates
```

Choose from: *O(1)*, *O(n)*, *O(n log n)*, **O(n²)**, *O(2^n)*""",
            hidden_answer="""**Answer: O(n²)**

**Explanation:**
- The outer loop runs `n` times
- The inner loop runs `n-1`, `n-2`, ..., `1` times
- Total iterations: $(n-1) + (n-2) + ... + 1 = \\frac{n(n-1)}{2}$
- This simplifies to **O(n²)** in Big O notation

*Note: This could be optimized to O(n) using a hash set!*""",
            user_answer=None,
            revealed=False,
            name="Algorithm Complexity",
        )

        await cl.Message(
            content="Here's an algorithm analysis challenge:",
            elements=[training_element],
        ).send()

    elif "easy" in message.content.lower():
        # Simple training activity
        training_element = cl.TrainingActivityElement(
            question="**What does 'HTML' stand for?**\n\n*This is a fundamental web technology.*",
            hidden_answer="**HyperText Markup Language**\n\nHTML is the standard markup language for creating web pages and web applications.",
            user_answer=None,
            revealed=False,
            name="Web Basics",
        )

        await cl.Message(
            content="Here's an easy web technology question:",
            elements=[training_element],
        ).send()

    else:
        await cl.Message(
            content=f"You said: {message.content}\n\nTry asking for:\n- 'math' - for a mathematical challenge\n- 'algorithm' - for an algorithm question\n- 'easy' - for a simple question"
        ).send()
