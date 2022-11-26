import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1046108463304028232/AWucOz4jfF3lBLg_mkqXMMfJgJAwjA_hhMEO2Mubp3vxi63QLpQmRFzPNnytaTqjuqcs', username="pica", content="lorem ipsum dolor sit amet")
    
response = webhook.execute()