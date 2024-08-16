import time
with open('main.py', 'r') as file:
    main_content = file.read()

for i in range(10):
    exec(main_content)
    time.sleep(10)


