import os

os.chdir('/Users/rahma/OneDrive/Documents')

print(os.getcwd())

for f in os.listdir('.'):
    print(f)

print('#######################################')
for f in os.listdir('.'):
    print(f)
print('#######################################')
for f in os.listdir('.'):
    print(os.path.getsize(f))
print('#######################################')
for f in os.listdir('.'):
    print(os.path.getmtime(f))
print('#######################################')
for f in os.listdir('.'):
    print(os.path.splitext(f))
print('########################################')


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    if '-' not in f_name:
        continue

    f_title, f_course, f_num = f_name.split('-')
#to strip the unwanted spaces in sentences we use below method and zfill makes numbers two digit
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
###
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))

new_name='{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext)
os.rename(f,new_name)
