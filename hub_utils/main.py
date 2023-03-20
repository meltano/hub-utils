import typer
from hub_utils.utilities import Utilities
from typing import Optional
from hub_utils.yaml_lint import find_all_yamls
import os
import json

app = typer.Typer()

@app.callback()
def callback():
    """
    MeltanoHub Utilities
    """

@app.command()
def add(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add(repo_url)

@app.command()
def add_bulk(
    csv_path: str,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add_bulk(csv_path)

@app.command()
def update(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.update(repo_url)

@app.command()
def update_sdk(
    repo_url: str = None,
    plugin_name: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.update_sdk(repo_url, plugin_name)

@app.command()
def add_airbyte(
    repo_url: str = None,
    auto_accept: bool = typer.Option(False)
):
    util = Utilities(auto_accept)
    util.add_airbyte(repo_url)

@app.command()
def refresh_sdk_variants(
    starting_yaml: str = None,
):
    util = Utilities(True)
    start = False
    failures = []
    for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
        data = util._read_yaml(yaml_file)
        if yaml_file == f'{util.hub_root}{starting_yaml}':
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            try:
                util.update_sdk(data.get('repo'), data.get("name"))
            except Exception as e:
                failures.append(yaml_file)
                print(e)

@app.command()
def extract_metadata(
    output_dir: str,
    starting_yaml: str = None,
):
    util = Utilities(True)
    start = False
    failures = []
    for yaml_file in find_all_yamls(f_path=f"{util.hub_root}/_data/meltano/"):
        data = util._read_yaml(yaml_file)
        if not starting_yaml or yaml_file == f'{util.hub_root}{starting_yaml}':
            start = True
        elif not start:
            print(f"Skipping SDK based: {yaml_file}")
            continue
        if "keywords" in data and "meltano_sdk" in data.get("keywords"):
            print(f"Updating: {yaml_file}")
            p_type = util.get_plugin_type(data.get("repo"))
            p_name = data.get("name")
            sdk_def = util._test(
                p_name,
                p_type,
                data.get("pip_url"),
                data.get("namespace"),
                data.get("executable", p_name),
                True
            )
            if not sdk_def:
                failures.append(yaml_file)
                continue
            file_name = os.path.basename(yaml_file).replace('.yml', '.json')
            util._write_dict(
                f"{output_dir}/{p_type}/{p_name}/{file_name}",
                sdk_def
            )
    print(failures)

@app.command()
def get_variant_names(
    hub_root: str,
    # sdk_based: bool = typer.Option(False),
):
    select_subset = [
        "extractors/tap-snowflake/meltanolabs.yml",
        # "extractors/tap-github/meltanolabs.yml",
        # "extractors/tap-cloudwatch/meltanolabs.yml"
    ]
    files = []
    for yaml_file in find_all_yamls(f_path=f"{hub_root}/_data/meltano/"):
        suffix = yaml_file.replace(f"{hub_root}/_data/meltano/", "")
        if suffix in select_subset:
            files.append(yaml_file)
    # print(json.dumps(files))
    print(",".join(files))

@app.command()
def extract_metadata_v2(
    variant_path_list: str,
    output_dir: str,
):
    util = Utilities(True)
    failures = []
    for yaml_file in variant_path_list.split(","):
        data = util._read_yaml(yaml_file)
        p_type = util.get_plugin_type(data.get("repo"))
        p_name = data.get("name")
        sdk_def = util._test(
            p_name,
            p_type,
            data.get("pip_url"),
            data.get("namespace"),
            data.get("executable", p_name),
            True
        )
        if not sdk_def:
            failures.append(yaml_file)
            continue
        file_name = os.path.basename(yaml_file).replace('.yml', '.json')
        util._write_dict(
            f"{output_dir}/{p_type}/{p_name}/{file_name}",
            sdk_def
        )
    print(failures)


@app.command()
def translate(
    variant_path_list: str,
    sdk_output_path: str,
):
    util = Utilities(True)
    from hub_utils.meltano_util import MeltanoUtil

    for yaml_file in variant_path_list.split(","):
        existing_def = util._read_yaml(yaml_file)
        suffix = "/".join(yaml_file.split("/")[-3:])
        json_file = f"{sdk_output_path}/{suffix}".replace(".yml", ".json")
        with open(json_file, "r") as f:
            sdk_about = json.load(f)
        settings, settings_group_validation, capabilities = MeltanoUtil._parse_sdk_about_settings(sdk_about)
        new_def = util._merge_definitions(
            existing_def,
            settings,
            util._string_to_literal(util._scrape_keywords(True, existing_def.get("keywords"))),
            existing_def.get('maintenance_status'),
            capabilities,
            settings_group_validation,
        )
        p_name = existing_def.get("name")
        p_type = util.get_plugin_type(existing_def.get("repo"))
        p_variant = existing_def.get("variant")
        util._write_updated_def(
            p_name,
            p_variant,
            p_type,
            new_def
        )
        util._reformat(p_type, p_name, p_variant)
