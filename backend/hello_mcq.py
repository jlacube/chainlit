import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat with a welcome message and sample MCQ."""

    # Create a multiple choice question about Python with markdown formatting
    mcq_element = cl.MCQElement(
        question="""**What is the output of the following Python code?**

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```

*Note: Pay attention to how Python handles list references.*""",
        options=[
            {
                "id": "option_a",
                "text": "`3`",
                "isCorrect": False,
                "explanation": "This would be correct if `y` was a **copy** of `x`, but `y` references the same list as `x`.",
            },
            {
                "id": "option_b",
                "text": "`4`",
                "isCorrect": True,
                "explanation": "**Correct!** Since `y` references the same list as `x`, appending to `y` also modifies `x`.",
            },
            {
                "id": "option_c",
                "text": "~~Error~~",
                "isCorrect": False,
                "explanation": "No error occurs. This is *valid* Python code.",
            },
            {
                "id": "option_d",
                "text": "`None`",
                "isCorrect": False,
                "explanation": "The `len()` function returns an **integer**, not `None`.",
            },
        ],
        revealed=False,
    )

    await cl.Message(
        content="Welcome to the MCQ Demo! Here's a Python question for you:",
        elements=[mcq_element],
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """Handle user messages and provide more MCQ examples."""

    if "javascript" in message.content.lower():
        # JavaScript MCQ with markdown
        mcq_element = cl.MCQElement(
            question="**Which of the following correctly declares a constant in JavaScript?**\n\n*Choose the ES6+ syntax:*",
            options=[
                {
                    "id": "js_a",
                    "text": "`var PI = 3.14;`",
                    "isCorrect": False,
                    "explanation": "`var` declares a **variable**, not a constant.",
                },
                {
                    "id": "js_b",
                    "text": "`let PI = 3.14;`",
                    "isCorrect": False,
                    "explanation": "`let` declares a *block-scoped variable*, not a constant.",
                },
                {
                    "id": "js_c",
                    "text": "`const PI = 3.14;`",
                    "isCorrect": True,
                    "explanation": "**Correct!** `const` declares a block-scoped constant.",
                },
                {
                    "id": "js_d",
                    "text": "`constant PI = 3.14;`",
                    "isCorrect": False,
                    "explanation": "This is **not** valid JavaScript syntax.",
                },
            ],
            revealed=False,
        )

        await cl.Message(
            content="Here's a JavaScript question:", elements=[mcq_element]
        ).send()

    elif "multiple" in message.content.lower():
        # Multiple correct answers MCQ
        mcq_element = cl.MCQElement(
            question="Which of the following are valid Python data types? (Select all that apply)",
            options=[
                {
                    "id": "multi_a",
                    "text": "int",
                    "isCorrect": True,
                    "explanation": "Correct! int is a built-in numeric type.",
                },
                {
                    "id": "multi_b",
                    "text": "string",
                    "isCorrect": False,
                    "explanation": "In Python, it's called 'str', not 'string'.",
                },
                {
                    "id": "multi_c",
                    "text": "list",
                    "isCorrect": True,
                    "explanation": "Correct! list is a built-in sequence type.",
                },
                {
                    "id": "multi_d",
                    "text": "dict",
                    "isCorrect": True,
                    "explanation": "Correct! dict is a built-in mapping type.",
                },
            ],
            revealed=False,
            allow_multiple=True,
        )

        await cl.Message(
            content="Here's a multiple-choice question with multiple correct answers:",
            elements=[mcq_element],
        ).send()

    elif "easy" in message.content.lower():
        # Easy MCQ with LaTeX math
        mcq_element = cl.MCQElement(
            question="**What does 'AI' stand for?**\n\nAI is becoming increasingly important in modern technology, with applications in machine learning where we often use functions like $f(x) = \\sigma(wx + b)$.",
            options=[
                {
                    "id": "easy_a",
                    "text": "**Artificial Intelligence**",
                    "isCorrect": True,
                    "explanation": "**Correct!** AI stands for Artificial Intelligence. The mathematical notation $\\sigma$ often represents the *sigmoid activation function* in neural networks.",
                },
                {
                    "id": "easy_b",
                    "text": "~~Automated Information~~",
                    "isCorrect": False,
                    "explanation": "This is **not** what AI stands for.",
                },
                {
                    "id": "easy_c",
                    "text": "*Advanced Integration*",
                    "isCorrect": False,
                    "explanation": "This is **not** what AI stands for.",
                },
                {
                    "id": "easy_d",
                    "text": "`Algorithmic Implementation`",
                    "isCorrect": False,
                    "explanation": "This is **not** what AI stands for.",
                },
            ],
            revealed=False,
        )

        await cl.Message(
            content="Here's an easy question:", elements=[mcq_element]
        ).send()

    else:
        await cl.Message(
            content=f"You said: {message.content}\n\nTry asking for:\n- 'javascript' - for a JavaScript question\n- 'multiple' - for a multiple-answer question\n- 'easy' - for an easy question"
        ).send()
