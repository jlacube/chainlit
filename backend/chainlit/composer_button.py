"""
Composer Button implementation for Chainlit.

Allows adding custom buttons to the MessageComposer area from Python backend.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ComposerButton:
    """A custom button that appears in the MessageComposer area."""

    id: str
    label: str
    style: str = "secondary"  # primary, secondary, outline
    data: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for frontend transmission."""
        return {
            "id": self.id,
            "label": self.label,
            "style": self.style,
            "data": self.data or {},
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ComposerButton":
        """Create ComposerButton from dictionary."""
        return cls(
            id=data["id"],
            label=data["label"],
            callback=data["callback"],
            icon=data.get("icon"),
            style=data.get("style", "secondary"),
            disabled=data.get("disabled", False),
            tooltip=data.get("tooltip"),
        )


# Global registry for composer button callbacks
_composer_button_callbacks: Dict[str, Any] = {}


def composer_button_callback(button_id: str):
    """
    Decorator to register a composer button callback function.

    Args:
        button_id: The ID of the button that this callback handles

    Example:
        @cl.composer_button_callback("deep-search-button")
        async def handle_deep_search(data: Dict[str, Any]):
            # Handle button click
            pass
    """

    def decorator(func):
        _composer_button_callbacks[button_id] = func
        return func

    return decorator


async def set_composer_buttons(buttons: List[ComposerButton]) -> None:
    """
    Set the custom buttons that appear in the MessageComposer area.

    Args:
        buttons: List of ComposerButton instances to display

    Example:
        await cl.set_composer_buttons([
            cl.ComposerButton(
                id="deep-search",
                label="🔍 Deep Search",
                callback="toggle_deep_search"
            )
        ])
    """
    from chainlit.context import context

    # Convert buttons to dict format
    buttons_data = [button.to_dict() for button in buttons]

    # Send to frontend via socket
    await context.emitter.emit("set_composer_buttons", {"buttons": buttons_data})

    # Store in session for persistence (gracefully handle missing user_session)
    try:
        if (
            hasattr(context.session, "user_session")
            and context.session.user_session is not None
        ):
            context.session.user_session["composer_buttons"] = buttons_data
    except (AttributeError, TypeError):
        # If user_session is not available, just continue without storing
        # The buttons will still work for the current session via the socket emit above
        pass


async def update_composer_button(button_id: str, updates: Dict[str, Any]) -> None:
    """
    Update properties of a specific composer button.

    Args:
        button_id: The ID of the button to update
        updates: Dictionary of properties to update (label, disabled, etc.)

    Example:
        await cl.update_composer_button("deep-search", {
            "label": "🔍 Deep Search: ON",
            "disabled": False
        })
    """
    from chainlit.context import context

    # Send update to frontend
    await context.emitter.emit(
        "update_composer_button", {"buttonId": button_id, "updates": updates}
    )

    # Update session storage (gracefully handle missing user_session)
    try:
        if (
            hasattr(context.session, "user_session")
            and context.session.user_session is not None
        ):
            buttons = context.session.user_session.get("composer_buttons", [])
            for button in buttons:
                if button["id"] == button_id:
                    button.update(updates)
                    break
    except (AttributeError, TypeError):
        # If user_session is not available, skip session storage update
        pass


async def remove_composer_buttons() -> None:
    """Remove all custom composer buttons."""
    from chainlit.context import context

    # Send to frontend
    await context.emitter.emit("remove_composer_buttons", {})

    # Clear session storage (gracefully handle missing user_session)
    try:
        if (
            hasattr(context.session, "user_session")
            and context.session.user_session is not None
        ):
            context.session.user_session["composer_buttons"] = []
    except (AttributeError, TypeError):
        # If user_session is not available, skip session storage update
        pass


async def handle_composer_button_click(button_id: str, data: Dict[str, Any]) -> None:
    """
    Handle a composer button click event from the frontend.

    Args:
        button_id: The ID of the clicked button
        data: Additional data passed with the button click
    """
    if button_id in _composer_button_callbacks:
        callback_func = _composer_button_callbacks[button_id]

        # Call the registered callback function
        try:
            await callback_func(data)
        except Exception as e:
            print(f"Error in composer button callback for '{button_id}': {e}")
            # Optionally send error to frontend
            from chainlit.context import context

            await context.emitter.emit(
                "composer_button_error", {"button_id": button_id, "error": str(e)}
            )
    else:
        print(f"No callback registered for composer button: {button_id}")
