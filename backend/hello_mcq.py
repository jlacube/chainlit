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

    elif (
        "algorithm" in message.content.lower()
        or "complexity" in message.content.lower()
    ):
        # Algorithm complexity MCQ with LaTeX and 5 options
        mcq_element = cl.MCQElement(
            question="""**What is the time complexity of binary search?**

Consider this implementation:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

*Assume the input array is **sorted** and has $n$ elements.*""",
            options=[
                {
                    "id": "algo_a",
                    "text": "$O(1)$ - *Constant time*",
                    "isCorrect": False,
                    "explanation": "**Incorrect.** $O(1)$ would mean the algorithm takes the same time regardless of input size. Binary search needs to examine multiple elements in the worst case.",
                },
                {
                    "id": "algo_b",
                    "text": "$O(\\log n)$ - *Logarithmic time*",
                    "isCorrect": True,
                    "explanation": "**Correct!** Binary search eliminates **half** of the remaining elements in each iteration. This gives us $\\log_2 n$ iterations in the worst case, hence $O(\\log n)$ time complexity.",
                },
                {
                    "id": "algo_c",
                    "text": "$O(n)$ - *Linear time*",
                    "isCorrect": False,
                    "explanation": "**Incorrect.** $O(n)$ would be the complexity of *linear search*. Binary search is much more efficient than examining every element.",
                },
                {
                    "id": "algo_d",
                    "text": "$O(n \\log n)$ - *Linearithmic time*",
                    "isCorrect": False,
                    "explanation": "**Incorrect.** $O(n \\log n)$ is typically the complexity of efficient sorting algorithms like **merge sort** or **heap sort**, not binary search.",
                },
                {
                    "id": "algo_e",
                    "text": "$O(n^2)$ - *Quadratic time*",
                    "isCorrect": False,
                    "explanation": "**Incorrect.** $O(n^2)$ is much worse than binary search's actual complexity. This is typical for algorithms with nested loops, like ~~bubble sort~~.",
                },
            ],
            revealed=False,
        )

        await cl.Message(
            content="Here's an algorithm complexity question:", elements=[mcq_element]
        ).send()

    elif (
        "variation" in message.content.lower()
        or "alternative" in message.content.lower()
    ):
        # MCQ with multiple valid solutions/approaches
        mcq_element = cl.MCQElement(
            question="""**Which approach would be most appropriate for sorting a small array of 10 integers?**

Consider these factors:
- **Performance**: Actual runtime for small datasets
- **Implementation**: Code simplicity and readability
- **Practical use**: Real-world considerations

```python
# Array to sort
arr = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
```

*Note: For small arrays, theoretical complexity may not match practical performance.*""",
            options=[
                {
                    "id": "var_a",
                    "text": "**Bubble Sort** - $O(n^2)$ but simple",
                    "isCorrect": True,
                    "explanation": "**Valid choice!** For just 10 elements, bubble sort's simplicity often outweighs its poor theoretical complexity. Easy to implement and understand.",
                },
                {
                    "id": "var_b",
                    "text": "**Insertion Sort** - $O(n^2)$ but efficient for small arrays",
                    "isCorrect": True,
                    "explanation": "**Excellent choice!** Insertion sort is actually *faster* than quicksort for small arrays (typically < 20 elements) and is often used as the base case in hybrid algorithms.",
                },
                {
                    "id": "var_c",
                    "text": "**Built-in `sorted()`** - Timsort implementation",
                    "isCorrect": True,
                    "explanation": "**Practical choice!** Python's `sorted()` uses Timsort, which is optimized for real-world data and handles small arrays efficiently. Most **production-ready** approach.",
                },
                {
                    "id": "var_d",
                    "text": "**Merge Sort** - $O(n \\log n)$ guaranteed",
                    "isCorrect": False,
                    "explanation": "**Overkill** for 10 elements. The overhead of recursive calls and auxiliary space makes it *slower* than simpler algorithms for this size.",
                },
                {
                    "id": "var_e",
                    "text": "**Radix Sort** - $O(d \\times n)$ for integers",
                    "isCorrect": False,
                    "explanation": "**Unnecessarily complex** for this scenario. The setup overhead makes it impractical for such a small dataset, despite good theoretical complexity.",
                },
            ],
            revealed=False,
        )

        await cl.Message(
            content="Here's a question with multiple valid approaches:",
            elements=[mcq_element],
        ).send()

    else:
        await cl.Message(
            content=f"You said: {message.content}\n\nTry asking for:\n- 'javascript' - for a JavaScript question\n- 'multiple' - for a multiple-answer question\n- 'easy' - for an easy question\n- 'algorithm' - for an algorithm complexity question\n- 'variation' - for a question with multiple valid solutions"
        ).send()
