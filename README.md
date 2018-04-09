# IRC Bots

This is a different take on IRC Bots. This could be utilized for a bot net or something similar. It's not asynchronus like the Wifi(now|zone|here) botnet-style command push feature we developed back in '09 as it requires IRC connectivity, however it's enough for you to have a central place to accept commands, then push them out to the relevant nodes. 

I haven't finished this and probably never will, but I guess it would be a good stub to get some fun things happening in the future. 

I've built this because I want to build a jarvis but haven't worked out how yet. One day... one day I'll learn some nlp.

# Intended Use

You'll run your server. This badboy is responsible for processing commands.
You'll run your client. These badboys are responsible for interacting with hoomans.

The server sits in the background, listening to an ip/port. The clients run where-ever you want, and they'll perform tasks such as: 
- Sitting in an IRC chatroom
- Sitting in a Hipchat rom
- Posting to your Facebook
- Interacting with your monitoring or CI
- Anything else your mind imagines


This stems from the idea that I would like to have my phone connected to a bot in a chat program. Let's use Hipchat as an example, even though I'm pretty sure it blocks this.

I would be connected to my companies Hipchat room, with all my fellow coworkers. We sit in the chatroom all day instead of sitting in an office. Our bot sits in there with us, and whenever a key event happens that has our backs.

You might work in a 24/7 support team, manned by a handful of engineers who run a rotating on-call roster to respond to out-of-hours emergencies. Whenever a server goes down, a website doesn't fully load, or whatever metrics you might monitor fails, your bot would be alerted to the issue and would post in your Support Chat in-kind. You could then say "Thanks Bot" to acknowledge the alert and silence it.

Alternatively, your bot could create a ticket in salesforce and post the ticket into the chat along with the alert notification. You could then reply "thanks bot", and the bot would assign that ticket to your queue. You could then say "Let the customer know I'm looking into it and will call in five minutes." Your bot would then submit an entry into your ticket system, masquerading as yourself, saying "I'm looking into it and will call in five minutes", or could potentially pull the customers mobile phone numbers from your CRM (remember your customers received the same alert via sms/email), then SMS them through an sms gateway.

The possibilities are endless with your automation. You could say "Hey bot! Run jenkins job build-project" then "Hey bot! Run jenkins job test-project", and the bot would do so in kind, later replying "Hey <user>! Job failed, here's the build link: <link>".

Bots are highly disregarded in business because we don't run our businesses properly. We still insist on people doing certain tasks manually, or it might be easier to do it manually because noone cared to properly build your systems.

No matter your inspiration, I hope this at least inspires you to do something with irc-bot. Even if it's to centralize your messaging programs in a hacky kind of way.
