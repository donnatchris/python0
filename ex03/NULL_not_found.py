from typing import Any
import math
import numbers

def NULL_not_found(object: Any) -> int:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
	elif isinstance(object, float) and math.isnan(object):
		print(f"Cheese: {object} {type(object)}")
	elif isinstance(object, numbers.Number) and not isinstance(object, bool) and object == 0:
		print(f"Zero: {object} {type(object)}")
	elif isinstance(object, bool) and object == False:
		print(f"Fake: {object} {type(object)}")
	elif isinstance(object, str) and object == "":
		print(f"Empty: {type(object)}")
	else:
		print("Type not Found.")
	return 1


# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False

# Expected output:
# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
