# Initial cache trial

Run cache-01 used config `ttl=60`, code commit
`3333333333333333333333333333333333333333`, clean source, seed 3,
dataset requests-v1, protocol load-v1, 1,000 requests, concurrency 4.
P95 latency was 42 ms. Evidence: [run export](../../evidence/cache-01.json).

Run cache-02 used the same settings except concurrency 32.
It failed after 170/1,000 requests with database locked; no final latency.
Its only surviving reproduction command is:
`python bench.py --ttl 60 --concurrency 32 --seed 3`.
Tracker was not synced before the worker stopped.
