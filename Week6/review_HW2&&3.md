## cache

- number of seconds in a day: 86400

20191021_1
20191021_2
...
20191021_86400
20191022_1
20191022_2
...
20191022_86400

- minute level stats
- number of minutes of day: 24 * 60 = 1440
m_20191021_1
m_20191021_2
...
m_20191021_1440
(TTL = 10mins)

h_20191021_1
h_20191021_1
...

- `incr()` vs `get() + set()`
- difference
  - who's doing the work
  - concurrency
