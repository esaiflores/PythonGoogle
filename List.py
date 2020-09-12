filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for file in filenames:
    if '.hpp' in file:
        newfilenames.append((file, file[:-2]))
    else:
        newfilenames.append((file, file))

print(
    newfilenames)  # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
