import argparse
import discord
import os
import utils

from typing import Any, List

from constants import PR_CHANNEL


class Plumber(discord.Client):
    def __init__(
        self,
        *,
        intents: discord.Intents,
        changed: List[str],
        purge: bool,
        **options: Any
    ) -> None:
        super().__init__(intents=intents, **options)
        self.changed = changed
        self.purge = purge

    async def on_ready(self) -> None:
        for file in self.changed:
            channel_info = utils.map_channels(file)

            if self.purge:
                channel = client.get_channel(channel_info.get("id"))
            else:
                channel = client.get_channel(PR_CHANNEL)

            content = utils.parse_yaml(file)
            embed = utils.create_embed(content, channel_info.get("title"))

            if self.purge:
                await channel.purge(check=self.is_me)

            await channel.send(embed=embed)

        await client.close()

    def is_me(self, m) -> bool:
        return m.author == client.user


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("--purge", action="store_true")
    args = parser.parse_args()

    try:
        token = os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise KeyError("DISCORD_TOKEN not set")

    intents = discord.Intents.default()
    intents.message_content = True

    client = Plumber(intents=intents, changed=args.files, purge=args.purge)
    client.run(token)
