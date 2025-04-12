from pysine import sine

print("hello world")

# define methods
def flip_song(song):
    reversed = []
    for i in range(len(song)):
        reversed.append(song[len(song)-i-1])
    return reversed

# define notes
c=260
csharp=275
d=292
dsharp=309
e=328
f=347
fsharp=368
g=390
gsharp=413
a=437
asharp=463
b=491
secondc=520

# define songs
ascending_scale = [c, csharp, d, dsharp, e, f, fsharp, g, gsharp, a, asharp, b, secondc]
descending_scale = [secondc, b, asharp, a, gsharp, g, fsharp, f, e, dsharp, d, csharp, c]
reversed_function_test = flip_song(ascending_scale)

# play songs
for i in range(len(ascending_scale)):
    sine(frequency=ascending_scale[i], duration=0.5)
    sine(frequency=reversed_function_test[i], duration=0.5)
