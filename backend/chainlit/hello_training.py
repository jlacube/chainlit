# This is a simple example of a chainlit app using TrainingActivityElement.

from chainlit import Message, on_chat_start
from chainlit.element import TrainingActivityElement


@on_chat_start
async def main():
    # Example: send a training activity element
    elem = TrainingActivityElement(
        question="What is the capital of France?",
        hidden_answer="Paris",
        user_answer=None,
        revealed=False,
        name="Geography Quiz",
    )
    print(f"Created TrainingActivityElement: {elem}")
    print(f"Element type: {elem.type}")
    print(f"Element props: {elem.props}")
    print(f"Element to_dict: {elem.to_dict()}")

    # Create the message
    message = Message(content="Try this training activity:", elements=[elem])
    print(f"Message ID before send: {message.id}")
    print(f"Element for_id before send: {elem.for_id}")

    # Send the message
    await message.send()

    print(f"Message ID after send: {message.id}")
    print(f"Element for_id after send: {elem.for_id}")
    print(f"Element to_dict after send: {elem.to_dict()}")
