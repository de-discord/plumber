import discord
import yaml

import constants


def parse_yaml(filepath: str) -> dict:
    """Reads a yaml file and returns a dictionary"""
    # Remove 'plumber/' prefix
    filepath = filepath.split("/", maxsplit=1)[1]
    with open(filepath, "r") as file:
        content = yaml.safe_load(file)

    return content


def map_channels(filename: str) -> dict:
    print(f"Input file: {filename}")
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]

    try:
        channel_info = constants.CHANNELS[filename]
        print(channel_info)
    except KeyError:
        pass

    return channel_info


def create_embed(content: dict, title: str = None) -> discord.Embed:
    embed = discord.Embed(title=title)
    for k, v in content.items():
        embed.add_field(name=k, value="\n".join(v), inline=False)

    embed.set_footer(
        text="---\nFind this bot's source code at https://github.com/de-discord/plumber"
    )

    return embed
