from auth import load_config


def test_load_config(tmp_path):

    config_file = tmp_path / "config.yaml"

    config_file.write_text(
        "name: Poorvi"
    )

    data = load_config(config_file)

    assert data["name"] == "Poorvi"