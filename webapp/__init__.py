#!/usr/bin/env python3


from flask import Flask, render_template, request

from ingredient_parser import inspect_parser
from ingredient_parser.dataclasses import IngredientText

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Return homepage.

    Returns
    -------
    str
        Rendered HTML template
    """
    sentence = request.args.get("sentence", None)
    if sentence is None:
        return render_template(
            "index.html.jinja",
            display=False,
            sentence="",
        )

    parser_info = inspect_parser(sentence)
    parsed = parser_info.PostProcessor.parsed

    return render_template(
        "index.html.jinja",
        display=True,
        sentence=sentence,
        tokens=zip(
            parser_info.PostProcessor.tokens,
            parser_info.PostProcessor.labels,
            parser_info.PostProcessor.scores,
        ),
        name=parsed.name if parsed.name is not None else IngredientText("", 0),
        size=parsed.size if parsed.size is not None else IngredientText("", 0),
        amounts=parsed.amount,
        preparation=parsed.preparation
        if parsed.preparation is not None
        else IngredientText("", 0),
        comment=parsed.comment if parsed.comment is not None else IngredientText("", 0),
        purpose=parsed.purpose if parsed.purpose is not None else IngredientText("", 0),
    )
