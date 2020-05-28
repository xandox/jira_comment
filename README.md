
Helps to manage tables and images for JIRA

Example:

```python

from jira_comment import *

with image_directory("./JIRA-184/comments/0"):
    left_image = Image("~/my_reports/left.png")
    right_image = Image("~/my_reports/right.png")

p = Paragraph(
    H2("Some new results"),
    Table(
        HeadRow("Left image", "Right Image"),
        Row(left_image, right_image),
    ),
    Paragraph("Some conclusion")
)

print(p)

```

Will:
1. Create directory `./JIRA-184/comments/0` with images content. New names for images will be sha256 hesh sum. It needed if your report generate different images but with same name time to time. So you can upload this directory content to JIRA by one drop.
2. Print to stdout formated comment which you can copy past to JIRA comment directly.

Output example:
```
h2. Some new results

||Left image||Right Image||
|!27fe3d2814911f70d5beee531560d39b1e48a119ee1ef533b5f87e41c4122d29.png|thumbnail!|!5df38c22c81eaa2e2b735b82c04d9cf7866d63f86fba85c7e4dcba6a6002b7a4.png|thumbnail!|

Some conclusion 1


Some conclusion 2


```