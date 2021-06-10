import shutil
import os
import json
import os.path
import paeiou
from pa_location import pa_location

gen = "gen"
dl_path = "download"
stage_path = "stage"

mod_urls = {
    "legion": "https://cdn.palobby.com/community-mods/downloads/com.pa.legion-expansion-server.zip"
}

COMM_MASS_TELEPORTER = {
    "radius": 50,
    "phasing_duration": 5,
    "phasing_health_frac": 0.5,
    "fixup_radius": 50,
    "energy_drain": 10000,
    "energy_cost": 300000,
    "unit_cap": 1,
    "target_types": "CmdBuild & LaserPlatform"
}

def gen_unit_shadows():
    def write_new_spec(spec, filename):
        out_filename = os.path.join(gen, filename)
        os.makedirs(os.path.dirname(out_filename), exist_ok = True)
        with open(out_filename, "w") as out:
            json.dump(spec, out)

    paeiou.simulate_mod_mount(pa_location, mod_urls, dl_path, stage_path)

    filename = "pa/units/commanders/base_commander/base_commander.json"
    with open(os.path.join(stage_path, filename)) as file:
        spec = json.load(file)
    spec["command_caps"].append("ORDER_MassTeleport")
    spec["mass_teleporter"] = COMM_MASS_TELEPORTER
    write_new_spec(spec, filename)

    filename = "pa/tools/uber_cannon/uber_cannon.json"
    with open(os.path.join(stage_path, filename)) as file:
        spec = json.load(file)
    spec["rate_of_fire"] = spec.pop("ammo_demand") / spec.pop("ammo_per_shot")
    spec.pop("ammo_capacity")
    spec.pop("ammo_source")
    write_new_spec(spec, filename)

def main():
    if os.path.isdir(gen):
        shutil.rmtree(gen)

    shutil.copytree("export", gen, dirs_exist_ok=True)
    paeiou.paeiou( 
        mod_id = "com.pa.daedalus.telemazer", 
        paeiou_unit_path = "paeiou_units/", 
        unit_add_list = "unit_add_list", 
        output_path = f"{gen}/",
        mod_prefix = "telemazer",
        server = True,
        client = False,
        pa_path = pa_location
    )
    gen_unit_shadows()

if __name__ == '__main__':
    main()
