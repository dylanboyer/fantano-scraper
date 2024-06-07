import re
from datetime import datetime

data = """
Listen: �����Highly�Suspect�-�16�[Official�Audio]��

The only stirring thing about listening to MCID is hearing who Highly Suspect will poorly mimic next.

More rock reviews: �����Rock�Reviews��

===================================
Subscribe: http://bit.ly/1pBqGCN

Patreon: ��/�theneedledrop��

Official site: http://theneedledrop.com

TND Twitter: ��/�theneedledrop��

TND Facebook: ��/�theneedledrop��

Support TND: http://theneedledrop.com/support
===================================

HIGHLY SUSPECT - MCID / 2019 / 300 ENTERTAINMENT / ALT ROCK, ELECTROPOP, POP RAP

NOT GOOD/10

Y'all know this is just my opinion, right?
Listen: �����Highly�Suspect�-�16�[Official�Audio]��

The only stirring thing about listening to MCID is hearing who Highly Suspect will poorly mimic next.

---------------------------
248,831 views Nov 6, 2019
"""

# Define regex patterns
rating_pattern = r'(\b\d{1,2}/10\b)'
views_pattern = r'([\d,]+ views)'
date_pattern = r'(\w+ \d{1,2}, \d{4})'
description_pattern = r'Listen: .*\n\n(.*?)\n\n'

# Find matches
rating_match = re.search(rating_pattern, data)
views_match = re.search(views_pattern, data)
date_match = re.search(date_pattern, data)
description_match = re.search(description_pattern, data)

# Extract and process matches
rating = rating_match.group(1) if rating_match else None
views = views_match.group(1).replace(',', '') if views_match else None
date_str = date_match.group(1) if date_match else None
description = description_match.group(1).strip() if description_match else None

# Convert date to a consistent format (e.g., YYYY-MM-DD)
date = datetime.strptime(date_str, '%b %d, %Y').strftime('%Y-%m-%d') if date_str else None

print(f"Rating: {rating}")
print(f"Views: {views}")
print(f"Date: {date}")
print(f"Description: {description}")
