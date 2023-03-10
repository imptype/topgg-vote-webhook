# UPDATE
Use the website https://webhook-topgg.com/ (by top.gg staff member) instead, it has everything already. 

# FEB 14 2023 UPDATE: Deta Cloud moved to Deta Space
This guide is partially broken. The code still works but the steps for deploying/hosting is different. Use https://github.com/imptype/deta-space-fastapi-example for the updated steps, and you'll need to modify the `Spacefile` to include the environment variables (check the [docs](https://deta.space/docs/en/reference/spacefile)).
But you can use the website above anyway.

## Information

This is a relay server that posts [Top.gg](https://top.gg) vote events as a basic Discord message through a Discord webhook. 

It's great if you don't have a server or you don't want to give your IP to Top.gg.

## Running
1. Make a new project on [Deta](https://web.deta.sh/home).
2. Click the 'Deploy to Deta' button on this repo.
3. Select your project and enter the environment variables.
   - `DISCORD_WEBHOOK_URL` is https://discord.com/api/webhooks/{id}/{token}
      - Edit Discord channel -> Integrations -> New webhook -> Copy webhook URL
   - `TOPGG_AUTH_TOKEN` is your authorization text in https://top.gg/bot/{id}/webhooks
4. Once deployed, set Top.gg's webhook to point to this page of the Micro's URL: [https://{id}.deta.dev/github](https://deta.sh)

## Deploy
Click the following button to deploy this Micro in your own Deta project:

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy)
