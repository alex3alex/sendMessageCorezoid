# sendMessageCorezoid
# Synopsis
Код придназначений для відправки шаблонів повідомлень використовуючи Corezoid. Функція приймає два параметра: назву темплейта, електронну адресу одержувача.
# Include
використовуються такі залежності
```python
import subprocess
```
# Code Example
Приклад надсилання шаблона ```telegram``` на email ```misha.gavela@dataroot.co```

```python
import sendMessageCorezoid
sendMessageCorezoid('telegram', 'misha.gavela@dataroot.co')
```
# Quickly start [install]
```console
git clone https://github.com/Arfey/sendMessageCorezoid.git
cd sendMessageCorezoid

python
import sendMessageCorezoid

sendMessageCorezoid('telegram', 'misha.gavela@dataroot.co')

```
---

[back to top](#sendmessagecorezoid)
