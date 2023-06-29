# `hub-utils`

MeltanoHub Utilities - A utility CLI intended to streamline the steps needed to add Singer taps/targets to [MeltanoHub](https://hub.meltano.com/).

**Installation**

```
export HUB_ROOT_PATH='/Users/meltano/hub'

poetry install
poetry run hub-utils --help
```

**Tests**

```bash
poetry run pytest -v

poetry run pytest -v tests/test_core.py::test_sdk_about_parsing_1
```

**Refreshing This README**

The CLI is auto documenting so put all content in the CLI modules
and this will use [typer-cli](https://typer.tiangolo.com/typer-cli/) utilities
to render them as markdown.

Run the following command:

```bash
poetry run typer hub_utils/main.py utils docs --name hub-utils --output README.md
```

**Usage**:

```console
$ hub-utils [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`
* `add-airbyte`
* `add-hotglue`
* `download-metadata`
* `extract-metadata`
* `extract-sdk-metadata-to-s3`
* `get-variant-names`
* `merge-metadata`
* `refresh-sdk-variants`
* `sdk-variants-as-csv`: This command will generate a `sdk.csv` CSV...
* `translate-sdk`
* `update-definition`
* `update-quality`
* `upload-airbyte`

## `hub-utils add`

**Usage**:

```console
$ hub-utils add [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils add-airbyte`

**Usage**:

```console
$ hub-utils add-airbyte [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils add-hotglue`

**Usage**:

```console
$ hub-utils add-hotglue [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils download-metadata`

**Usage**:

```console
$ hub-utils download-metadata [OPTIONS] LOCAL_PATH
```

**Arguments**:

* `LOCAL_PATH`: [required]

**Options**:

* `--variant-path-list TEXT`
* `--help`: Show this message and exit.

## `hub-utils extract-metadata`

**Usage**:

```console
$ hub-utils extract-metadata [OPTIONS] OUTPUT_DIR
```

**Arguments**:

* `OUTPUT_DIR`: [required]

**Options**:

* `--starting-yaml TEXT`
* `--help`: Show this message and exit.

## `hub-utils extract-sdk-metadata-to-s3`

**Usage**:

```console
$ hub-utils extract-sdk-metadata-to-s3 [OPTIONS] VARIANT_PATH_LIST OUTPUT_DIR
```

**Arguments**:

* `VARIANT_PATH_LIST`: [required]
* `OUTPUT_DIR`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils get-variant-names`

**Usage**:

```console
$ hub-utils get-variant-names [OPTIONS] HUB_ROOT
```

**Arguments**:

* `HUB_ROOT`: [required]

**Options**:

* `--metadata-type TEXT`: [default: sdk]
* `--plugin-type TEXT`
* `--help`: Show this message and exit.

## `hub-utils merge-metadata`

**Usage**:

```console
$ hub-utils merge-metadata [OPTIONS] HUB_ROOT LOCAL_PATH
```

**Arguments**:

* `HUB_ROOT`: [required]
* `LOCAL_PATH`: [required]

**Options**:

* `--variant-path-list TEXT`
* `--help`: Show this message and exit.

## `hub-utils refresh-sdk-variants`

**Usage**:

```console
$ hub-utils refresh-sdk-variants [OPTIONS]
```

**Options**:

* `--starting-yaml TEXT`
* `--help`: Show this message and exit.

## `hub-utils sdk-variants-as-csv`

This command will generate a `sdk.csv` CSV file in the current directory containing the following columns:
plugin_type, name, variant, sdk

**Usage**:

```console
$ hub-utils sdk-variants-as-csv [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `hub-utils translate-sdk`

**Usage**:

```console
$ hub-utils translate-sdk [OPTIONS] VARIANT_PATH_LIST SDK_OUTPUT_PATH
```

**Arguments**:

* `VARIANT_PATH_LIST`: [required]
* `SDK_OUTPUT_PATH`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils update-definition`

**Usage**:

```console
$ hub-utils update-definition [OPTIONS]
```

**Options**:

* `--repo-url TEXT`
* `--plugin-name TEXT`
* `--auto-accept / --no-auto-accept`: [default: no-auto-accept]
* `--help`: Show this message and exit.

## `hub-utils update-quality`

**Usage**:

```console
$ hub-utils update-quality [OPTIONS] METRICS_FILE_PATH
```

**Arguments**:

* `METRICS_FILE_PATH`: [required]

**Options**:

* `--help`: Show this message and exit.

## `hub-utils upload-airbyte`

**Usage**:

```console
$ hub-utils upload-airbyte [OPTIONS] VARIANT_PATH_LIST ARTIFACT_NAME
```

**Arguments**:

* `VARIANT_PATH_LIST`: [required]
* `ARTIFACT_NAME`: [required]

**Options**:

* `--help`: Show this message and exit.
