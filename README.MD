# Telemazer Go BRRR
Adds "Telemazer" snipes to Planetary Annihilation

## Telemazer Mechanics
- The MLA Commander can build the "Microwave Laser Generator" unit for 30,000 metal
- Both MLA and Legion Commanders can spend 30,0000 energy (up to 10,000 energy per second) to activate "Mass Teleport" to any location anywhere in the system.
  - The Commander can bring up to 5 Microwave Laser Generators with it when uses Mass Teleport.
    - Microwave Laser Generators must be within 30 radius (Commander green/fab range circle)
  - Mass Teleport sets the Commander and accompanying Microwave Laser Generators to 50% health
    - They cannot act for 5 seconds as their health is restored to normal values.
- Legion

## Side Effects
- Uber Cannon no longer uses an ammo bar, so it no longer costs energy.
  - This means energy state does not affect the Uber Cannon
  - This also means you can't see recharge progress on Uber Cannon
  - This change is made because of an engine limitation; units with the Mass Teleport command cannot also have an ammo bar.

## Additional Implementation Details
- The Commander's Mass Teleport can take any unit that has unit types that match `CmdBuild & LaserPlatform`

## Future
- The Microwave Laser Generator does not currently have its own model; this may come in the future.
- Legion may possibly get its own Microwave Laser Generator in the future.