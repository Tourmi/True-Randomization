
# Archipelago LUA Mod
- Connect to AP game
    - Validate game has correct mods loaded (RandoUtils for softlocks, custom PAK file)
    - Command validation
    - Connection validation
- AP status popups
- Location hooks
    - Items
    - Shards
- Give items to player
    - Spawn shards, or respawn them if player left current screen without picking them up
- Detect victory
- Deathlink

# True-Randomization
- Update UI
    - Add Archipelago checkbox
    - Select player name
    - Select progression balancing
    - Enable/disable deathlink
- Generate YAML
    - Contains player name (auto append {number} to it)
    - Contains progression balancing
    - Contains deathlink flag
    - Contains list of available checks
    - Contains list of available items
    - Contains list of rules (which check is available with which items)
- Generate PAK
    - All items and shards replaced by equivalent dummy items
        - ie: N3029 drops -> Shard_N3029, Common_N3029, Rare_N3029, etc
        - ie: 
# APWorld
- DONE: Initial Implementation
- Read and validate player's YAML
- Assume default items, checks and rules when YAML does not contain them