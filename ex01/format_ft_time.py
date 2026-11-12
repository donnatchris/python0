import time
from datetime import datetime

now = time.time()
date = datetime.fromtimestamp(now).strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
print(f"{date}")

# Expected output:
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
