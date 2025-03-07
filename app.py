"""
A HTTP API for dannyedel/dspdfviewer.
"""

from flask import Flask
from flask import request
from pyautogui import press

app = Flask(__name__)


@app.route("/<item>", methods=["POST"])
def entrypoint_with_item(item: str):
    """Handles POST requests for a specific item.

    Args:
        item (str): The name of the item being posted.

    Returns:
        None
    """
    data: str = request.get_data(as_text=True)
    print(f"POST {item} to {data}")

    {"slide": lambda: goto_slide(int(data))}.get(item, lambda: print("Unimplemented"))()

    return "OK"


def goto_slide(page: int):
    """Navigates to a specific slide.

    Args:
        page (int): The slide number to navigate to.

    Returns:
        None
    """
    press("g", interval=0.1)
    for char in str(page):
        press(char, interval=0.05)
    press("enter", interval=0.05)
