from pydantic import ValidationError
from models import QuoteLine, ExtractedQuote

tests = [
    {"description": "Pose faïence", "quantity": 6, "unit": "m2"},
    {"description": "Pose faïence", "quantity": "6", "unit": "m2"},
    {"description": "Pose faïence", "quantity": "six", "unit": "m2"},
    {"description": "Pose faïence", "quantity": 6},
    {"description": "Plinthes", "quantity": 10, "unit": "metres"},
    {"description": "Peinture", "quantity": 0, "unit": "m2"}
]

for test in tests:
    try:
        line = QuoteLine.model_validate(test)
        print("OK : ", line)
    except ValidationError as error:
        print("REFUSÉ : ", error)

try:
    quote = ExtractedQuote.model_validate({"lines": []})
    print("OK : ", quote)
except ValidationError as error:
    print("REFUSÉ : ", error)
