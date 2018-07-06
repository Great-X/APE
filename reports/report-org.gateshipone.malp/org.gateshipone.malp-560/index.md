title: org.gateshipone.malp

# org.gateshipone.malp

[Google Play Store](https://play.google.com/store/apps/details?id=org.gateshipone.malp)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.String.replaceAll(java.lang.String, java.lang.String)' on a null object reference
// 	at org.gateshipone.malp.mpdservice.mpdprotocol.MPDCommands.escapeString(MPDCommands.java:327)
// 	at org.gateshipone.malp.mpdservice.mpdprotocol.MPDCommands.MPD_COMMAND_SEARCH_FILES(MPDCommands.java:283)
// 	at org.gateshipone.malp.mpdservice.mpdprotocol.MPDInterface.getSearchedFiles(MPDInterface.java:530)
// 	at org.gateshipone.malp.mpdservice.handlers.serverhandler.MPDQueryHandler.handleMessage(MPDQueryHandler.java:517)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.os.HandlerThread.run(HandlerThread.java:61)

```



