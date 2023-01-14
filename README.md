A basic Discord bot to manage content such as rules, resources, and FAQs for the Data Engineering Discord server.

## Overview
Each file in the `plumber/yaml/` directory maps to a channel in the Data Engineering Discord server. The channel mapping can be found in `/plumber/constants.py`. 

On a push to the `main` branch (e.g. when merging  a pull request) if any files in the `yaml` directory have been modified then the corresponding channel will be updated. A channel being *updated* means that any previous posts in that channel by the bot user will be purged and the content of the modified yaml file will be posted as an embed in the channel. This same process can be run on-demand via the Actions page. See `.github/workflows/` for the Github Actions workflow files.

The bot runs entirely in Github Actions. It does not require a server and does not listen for events. For this reason, it is not possible at the moment to create interactive functionality in which user actions/commands in Discord trigger bot actions. Barring exceptional circumstances, this bot should function entirely within the generous Github Actions free-tier (2,000 min/month).

### Contributing
Contributions from the community are welcome, both in terms of the code and bot functionality, and especially in the content included in the `yaml` files. Please open a pull request against the `main` branch. Your changes will have to be reviewed by a code owner (i.e. one of the organization maintainers). If approved and merged, your changes will soon be reflected in the server.

#### Local Development
Once you clone the repository you can build the image from the directory root: `docker build -t plumber . `

The application can then be run with: `docker run -e DISCORD_TOKEN=$DISCORD_TOKEN plumber client.py <files>`.
`<files>` here is a series of files corresponding to the yaml files in the `plumber/yaml/` directory. They should be in the format of `plumber/yaml/<filename>.yaml`. So in order to execute an update on the `faq.yaml` file and the `rules.yaml` file, run: `docker run -e DISCORD_TOKEN=$DISCORD_TOKEN plumber client.py plumber/yaml/faq.yaml plumber/yaml/rules.yaml`

Note: You will need to create your own Discord application to be used for development. Once that is done you can generate a bot token to be passed in to the above command as `$DISCORD_TOKEN`. Your bot user will also need to be added to a server. At this time there is no centralized development server so you should create your own and add your bot user there. You will also need to update the channel mapping in `plumber/constants.py` to point to channels in your development server.

#### Desired Features
- [ ] Show formatted embed as comment on PR if yaml file changed
- [ ] Add a check of embed length and split into multiple embeds if maximum length exceeded