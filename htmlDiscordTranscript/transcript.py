import discord
import os

class Transcript():
    def __init__(self):
        self.out_dir = os.path.join(os.path.dirname(__file__), 'out')

    def escape_html(self, text):
        return discord.utils.escape_markdown(discord.utils.escape_mentions(text))

    def escape_attachments(self, attachments):
        if not attachments:
            return ""

        attachment_list = []
        for attachment in attachments:
            attachment_list.append(f'<img src="{discord.utils.escape_markdown(attachment.url)}" style="max-width: 800px; max-height: 600px; margin: 5px" alt="Attachment">')

        return " ".join(attachment_list)

    async def get_all_threads(self, channel):
        archived_threads = [thread async for thread in channel.archived_threads()]
        active_threads = channel.threads
        # Convert active threads to a list if needed
        active_threads = list(active_threads)

        all_threads = archived_threads + active_threads
        return all_threads

    async def removeHTML(self, user: discord.User):
        # Get a list of HTML files in the 'out' directory
        html_files = [file for file in os.listdir(self.out_dir) if file.endswith('.html')]

        # Check if there are HTML files in the 'out' directory
        if not html_files:
            raise "Error: No HTML files found in 'out' directory."

        try:
            # Send each HTML file
            for html_file in html_files:
                html_file_path = os.path.join(self.out_dir, html_file)
                await user.send(file=discord.File(html_file_path))

            print(f"Transcripts sent to {user.name}")
        except discord.errors.Forbidden:
            print("Error: Unable to send files to the specified user. Make sure the user allows direct messages.")
            
        for file_name in html_files:
            try:
                os.remove(os.path.join(self.out_dir, file_name))
                print(f"File {file_name} removed successfully.")
            except FileNotFoundError:
                print(f"File {file_name} not found.")
            except Exception as e:
                print(f"Error removing file {file_name}: {e}")

    async def transcriptChannel(self, user: discord.User, channel: discord.TextChannel):
        
        with open(os.path.join(self.out_dir, f"{channel.name}.html"), "w", encoding="utf-8") as file:
            file.write(
                    '''<head> 
                    <meta charset="UTF-8"> 
                    <meta name="viewport" 
                    content="width=device-width, 
                    initial-scale=1.0"> 
                    <title>Transcript</title> 
                    <link rel="stylesheet" 
                    href="style.css"> 
                    <script src="script.js" 
                    defer></script> 
                    </head>'''
                )
            async for message in channel.history(limit=None):
                
                content = self.escape_html(message.content)
                attachments = self.escape_attachments(message.attachments)
                
                pfp = message.author.display_avatar
                color = message.author.color
                
                file.write(f'<div><img src="{pfp}" style="max-width: 40px; max-height: 40px; border-radius: 50%;"> <strong><a style="color: {color}">{message.author.name}</a>:</strong> {content}</div>')
                file.write(f'<div>{attachments}</div>')
        await self.removeHTML(user)

    async def transcriptThread(self, user: discord.User, thread: discord.Thread):
        with open(os.path.join(self.out_dir, f"{thread.name}.html"), "w", encoding="utf-8") as file:
            # Creating head tag
            file.write(
                f'''<head> 
                <meta charset="UTF-8"> 
                <meta name="viewport" 
                content="width=device-width, 
                initial-scale=1.0"> 
                <title>Transcript</title> 
                <link rel="stylesheet" 
                href="style.css"> 
                <script src="script.js" 
                defer></script> 
                </head>'''
            )
            # Thread ID and Name
            file.write(f"Thread ID: {thread.id}, Name: {thread.name}")
            async for message in thread.history(limit=None):
                content = self.escape_html(message.content)
                attachments = self.escape_attachments(message.attachments)
                pfp = message.author.display_avatar
                color = message.author.color
                file.write(f'<div><img src="{pfp}" style="max-width: 40px; max-height: 40px; border-radius: 50%;"> <strong><a style="color: {color}">{message.author.name}</a>:</strong> {content}</div>')
                file.write(f'<div>{attachments}</div>')
                    
        await self.removeHTML(user)

    async def transcriptAllThreads(self, user: discord.User, channel: discord.TextChannel):
        threads = await self.get_all_threads(channel)
        
        for thread in threads:
            with open(os.path.join(self.out_dir, f"{thread.name}.html"), "w", encoding="utf-8") as file:
                # Creating head tag
                file.write(
                    f'''<head> 
                    <meta charset="UTF-8"> 
                    <meta name="viewport" 
                    content="width=device-width, 
                    initial-scale=1.0"> 
                    <title>Transcript</title> 
                    <link rel="stylesheet" 
                    href="style.css"> 
                    <script src="script.js" 
                    defer></script> 
                    </head>'''
                )
                # Thread ID and Name
                file.write(f"Thread ID: {thread.id}, Name: {thread.name}")
                async for message in thread.history(limit=None):
                    content = self.escape_html(message.content)
                    attachments = self.escape_attachments(message.attachments)
                    pfp = message.author.display_avatar
                    color = message.author.color
                    file.write(f'<div><img src="{pfp}" style="max-width: 40px; max-height: 40px; border-radius: 50%;"> <strong><a style="color: {color}">{message.author.name}</a>:</strong> {content}</div>')
                    file.write(f'<div>{attachments}</div>')
                    
        await self.removeHTML(user)