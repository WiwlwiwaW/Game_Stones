stroke = input('Введите строку:\n')
moder_stroke = stroke.expandtabs(tabsize=4)
while True:
    if ' ' == moder_stroke[0]:
        moder_stroke = moder_stroke[1:]
    else:
        break
while True:
    if ' ' == moder_stroke[-1] or '!' == moder_stroke[-1] or '?' == moder_stroke[-1] or '.' == moder_stroke[-1]:
        moder_stroke = moder_stroke[:-1]
    else:
        break
moder_stroke = moder_stroke.upper()[0] + moder_stroke.lower()[1:]
print(moder_stroke + ".")
