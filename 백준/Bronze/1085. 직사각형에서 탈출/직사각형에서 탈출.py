x, y, w, h = map(int, input().split())
sub = []

sub.append(x)
sub.append(y)
sub.append(w-x)
sub.append(h-y)

print(min(sub))