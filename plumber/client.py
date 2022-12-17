import argparse
import discord
import os
import utils

from typing import Any, List


class Plumber(discord.Client):
    def __init__(
        self, *, intents: discord.Intents, changed: List[str], **options: Any
    ) -> None:
        super().__init__(intents=intents, **options)
        self.changed = changed

    async def on_ready(self) -> None:

        for file in self.changed:
            channel_info = utils.map_channels(file)
            channel = client.get_channel(channel_info.get("id"))

            await channel.purge(check=self.is_me)

            content = utils.parse_yaml(file)
            embed = utils.create_embed(content)

            await channel.send(embed=embed)

        await client.close()

    def is_me(self, m) -> bool:
        return m.author == client.user


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    try:
        token = os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise KeyError("DISCORD_TOKEN not set")

    intents = discord.Intents.default()
    intents.message_content = True

    client = Plumber(intents=intents, changed=args.files)
    client.run(token)
