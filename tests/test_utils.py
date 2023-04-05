from hub_utils.utilities import Utilities


def test_get_plugin_type_from_suffix():
    utils = Utilities()
    plugin_type = utils.get_plugin_type_from_suffix(
        "extractors/tap-csv/meltanolabs"
    )
    assert plugin_type == "extractors"

def test_get_plugin_variant_from_suffix():
    utils = Utilities()
    variant = utils.get_plugin_variant_from_suffix(
        "extractors/tap-csv/meltanolabs"
    )
    assert variant == "meltanolabs"
