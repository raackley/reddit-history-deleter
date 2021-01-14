# Reddit history deleter

This script deletes your user's Reddit comments if they are older than a certain number of days.  If you do not specify an age threshold, then the default value is set to 365 days.

## Configuration

To configure the script, you must set your Reddit user's credentials as environment variables.  Set the following values.

```
export RHD_USERNAME=<Reddit username>
export RHD_PASSWORD=<Reddit password>
export RHD_CLIENT_ID=<Reddit app ID>
export RHD_CLIENT_SECRET=<Reddit app secret>
```

The username and password should be self explanatory.  The client ID and secret must be configured as a new application in your Reddit account first, then the values for that app can be used here.

To do that, log into your Reddit account, and go to User Settings.  Then go to `Safety & Privacy`, and then at the bottom, click on `Manage third-party app authorization`.

Click the "Create another app..." button.  Enter a name, like `reddit-history-deleter`.  Click the button next to `script`.  Enter a `redirect uri` value of `http://localhost:8080`.  The other fields you can leave blank if you want.

Click `create app`.  After the app has been created, use the value under `personal use script` for the app ID in the configuration, and use the value for `secret` for the app secret value.

## Run

You will need Python 3 to run the app after configuring it.  If you have Python 3 installed, you can run it like so:

```
$ python reddit-history-deleter.py
```