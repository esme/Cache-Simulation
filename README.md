# Computer Architecture Project 2 - Cache Simulation
Details:
- Software simulation of a cache memory subsystem
- Main memory of 2k array
- Direct-mapped, write-back cache
- Supports three types of requests from the terminal: (R)ead, (W)rite, or (D)isplay Cache
- If a Read is requested: Ff the address is in the cache, display the value found for it in cache AND indicate that a cache hit took place. If not, go to your main memory instead, bring the entire block into the cache, display the value found AND indicate a cache miss
- If a write is to be performed on a block that is not already in the cache, bring the entire block into the cache, perform the write and consider it a cache miss
- Display Cache will display the contents of each slot in the cache