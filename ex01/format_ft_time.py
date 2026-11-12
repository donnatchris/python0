import time
from datetime import datetime

now = time.time()
date = datetime.fromtimestamp(now).strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {now:,.4f} "
    f"or {now:.2e} in scientific notation")
print(f"{date}")
