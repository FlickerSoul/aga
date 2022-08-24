"""The command-line UI."""

from rich import print as rprint
from rich.box import ROUNDED
from rich.panel import Panel

from ..runner import AgaProblemOutput

RICH_PANEL_OPTS = {
    "box": ROUNDED,
    "title_align": "left",
    "subtitle_align": "right",
}


def print_fancy_summary(output: AgaProblemOutput) -> None:
    """Print a fancy summary of the problem."""
    rprint(
        Panel(
            output.output,
            title="Overall",
            subtitle=f"Total score: {output.score}",
            **RICH_PANEL_OPTS,  # type: ignore
        )
    )

    for test in output.tests:
        # TODO: should we print smth even if there's no output?
        if test.output and not test.hidden:
            rprint(
                Panel(
                    test.output,
                    title="" if test.correct() else "[bright_red]" + test.name,
                    subtitle=f"{test.score}/{test.max_score}",
                    **RICH_PANEL_OPTS,  # type: ignore
                )
            )
