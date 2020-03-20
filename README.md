# Slack Converstation History Export

## Description

This repo includes script for exporting conversation history from Slack.
Please see Slack’s various export tools here: https://slack.com/help/articles/204897248-Guide-to-Slack-import-and-export-tools
If your workspace is on Slack’s Standard plan, you can use Slack API to export message history. With your user token, you can fetch direct messages, group direct messages, private and public channels that the user participates in.

## Dependencies

1. Script runs on python(specifically python 3).
2. You need to get your user token with below scope and update token.txt with your token.
![picture alt] (https://github.com/aaskan/Slack-Export/blob/master/ReadMeAsset/userscope.png)

## Usage

Exporting all direct messages, group direct messages, private and public channels that the user participates in: 
``` 
python slack_export.py all 
```

You can also export
- only direct messages by running ``` python slack_export.py im ```
- only group direct messages by running ``` python slack_export.py mpim ```
- only private channels by running ``` python slack_export.py private_channel ```
- only public channels by running ``` python slack_export.py public_channel ```

