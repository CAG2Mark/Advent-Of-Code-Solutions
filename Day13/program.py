tg = int(input());
bus = input().split(",");
times = list();
for b in bus:
    if b == 'x': continue;
    times.append(int(b));

times_ = [x * (tg // x + 1) for x in times];

print((min(times_) - tg) * times[times_.index(min(times_))])