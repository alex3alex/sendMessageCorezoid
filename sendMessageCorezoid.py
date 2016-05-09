import subprocess


def sendMessageCorezoid(template, email):
    """
    Send message, using Corezoid backend.
    Arguments is object with keys: day, email, idTemplate, key, user.
    """
    data = '{ "ops" : [{ "type" : "create", "obj" : "task", "conv_id" : \
        136950, "data" : {"day":"1","email":"%s","idTemplate":"%s","key":\
        "AxYXSJ92xN4ZEdLtLh0_4g","user":"Igor"} }] }' % (email, template)
    url = 'https://www.corezoid.com/api/1/json/'
    subprocess.Popen('sh shell.sh %s %s' % (template, email), shell=True).wait()

# example
sendMessageCorezoid('telegram', 'misha.gavela@dataroot.co')
