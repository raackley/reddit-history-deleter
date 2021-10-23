# Reddit history deleter

This script deletes or overwrites your user's Reddit comments and submissions if they are older than a certain number of days.  If you do not specify an age threshold, then the default value is set to 365 days.  The default mode is "delete".

## Configuration

To configure the script, you must set your Reddit user's credentials as environment variables.  Set the following values.

```
export RHD_USERNAME=<Reddit username>
export RHD_PASSWORD=<Reddit password>
export RHD_CLIENT_ID=<Reddit app ID>
export RHD_CLIENT_SECRET=<Reddit app secret>
```
Optional, set the number of days old a Reddit post should be to delete.  Not setting this value will default to 365 days.

```
export RHD_EXPIRATION_DAYS=<number of days>
```

Optional, set the mode.  For overwrite mode, set the variable to "overwrite".  For delete mode, set it to "delete", or do not set it.

```
export RHD_MODE="overwrite"
```

Optional, when using overwrite mode, you can customize the overwritten message.  The default is "DLETED".

```
export RHD_OVERWRITE_MESSAGE="<your overwrite message>"
```

The username and password should be self explanatory.  The client ID and secret must be configured as a new application in your Reddit account first, then the values for that app can be used here.

To do that, log into your Reddit account, and go to User Settings.  Then go to `Safety & Privacy`, and then at the bottom, click on `Manage third-party app authorization`.

Click the "Create another app..." button.  Enter a name, like `reddit-history-deleter`.  Click the button next to `script`.  Enter a `redirect uri` value of `http://localhost:8080`.  The other fields you can leave blank if you want.

Click `create app`.  After the app has been created, use the value under `personal use script` for the app ID in the configuration, and use the value for `secret` for the app secret value.

## Run Standalone

You will need Python 3 to run the app after configuring it.  You will also need to install the PRAW library via pip.

```
$ cd src
```

```
$ python -m pip install -r requirements.txt
```

```
$ python reddit-history-deleter.py
```

## Run with Docker

```
docker run --rm -e RHD_USERNAME=$RHD_USERNAME \
-e RHD_PASSWORD=$RHD_PASSWORD \
-e RHD_CLIENT_ID=$RHD_CLIENT_ID \
-e RHD_CLIENT_SECRET=$RHD_CLIENT_SECRET \
-e RHD_EXPIRATION_DAYS=$RHD_EXPIRATION_DAYS raackley/reddit-history-deleter:latest
```