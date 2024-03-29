import shutil
import os
import json
import os.path
import paeiou
from pa_location import pa_location, mods_path

gen = "telemazer-server"
dl_path = "download"
stage_path = "stage"

mod_urls = {}

COMM_MASS_TELEPORTER = {
    "radius": 30,
    "phasing_duration": 5,
    "phasing_health_frac": 0.5,
    "fixup_radius": 30,
    "energy_drain": 10000,
    "energy_cost": 300000,
    "unit_cap": 5,
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

def install_mod(mod_path):
    install_path = os.path.join(mods_path, mod_path)
    if os.path.isdir(install_path):
        shutil.rmtree(install_path)

    shutil.copytree(mod_path, install_path, dirs_exist_ok=True)

    modinfo_path = os.path.join(install_path, "modinfo.json")
    with open(modinfo_path, 'r') as modinfo_file:
        info = json.load(modinfo_file)
        info["identifier"] = info["identifier"] + "-dev"
    
    with open(modinfo_path, 'w') as modinfo_file:
        json.dump(info, modinfo_file)

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

    shutil.make_archive("telemazer-server", "zip", gen)
    install_mod(gen)


if __name__ == '__main__':
    main()
