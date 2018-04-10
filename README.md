# Botnet

This is a little botnet project I've been brainstorming on for quite a while. The whole principal is to deploy little scripts across infrastructure to humanize my servers further by making them talk to me in IRC. As lonely as this sounds, there's a valid sysadminy reason for this.

Warning; this does not work yet.

## Intended Usage

The intent here is to create a simple server which sits on a remote machine, accepting input and delegating commands for bots scattered across the interwebs.

These bots can do whatever they like, however the primary purpose is for the bot to accept data to transmit back to the server and then to relay the servers response back to the client. For instance, an IRC bot would communicate the IRC log back to the server and if an action get's triggered, the server would process the action then return the output back to the IRC bot to send to the channel.

Some use cases I've thought of include
- IRC bot for a chat channel
- A Hipchat bot that responds relays your alerts to your team (remember pagers?)
- An interactive Facebook Messenger bot that auto-replies to your customers, masquerading as a real person, that you're able to speak through when neccersary
- Modify the server to take ansible commands and deploy it on your ansible server. Modify the bot/server to accept a range of commands that will utilize Ansible to execute commands on your remote linux systems on your behalf. Write a bunch of scripts that basically automate your job. Fake an injury and begin "working from home" during your recovery phase, preferably on a beach somewhere. Have the bot look for keywords in emails and execute the apporpriate script in response. Anything that doesn't trigger, have a bot sitting in hipchat so you can just tell it what to do. Now that you have more free time, you can spend your afternoons on more productive pursuits, like training to scull a longneck in a single go or balancing carburetors my ear.
