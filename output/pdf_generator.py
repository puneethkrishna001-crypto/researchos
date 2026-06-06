from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os


def create_pdf(report_text, filename):

    os.makedirs(
        "output/reports",
        exist_ok=True
    )

    filepath = os.path.join(
        "output/reports",
        filename
    )

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(
                    1,
                    6
                )
            )

    doc.build(content)

    return filepath