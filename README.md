# sendMessageCorezoid
# Synopsis
Код придназначений для відправки шаблонів повідомлень використовуючи Corezoid. Функція приймає в якості аргумента об’єкт і відправляє повідомлення.
# Include
використовуються такі залежності
```python
import json
import os
import time
```
# Code Example
Приклад надсилання шаблона ```telegram``` на email ```igor.sizon@dataroot.co```

```python
import sendMessageCorezoid
sendMessageCorezoid(
    {"day": "1", "email": "igor.sizon@dataroot.co", "idTemplate":
     "telegram", "key": "AxYXSJ92xN4ZEdLtLh0_4g", "user": "Igor"})
```
---

[back to top](#sendmessagecorezoid)
