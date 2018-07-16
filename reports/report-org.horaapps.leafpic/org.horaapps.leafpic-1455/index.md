title: org.horaapps.leafpic

# org.horaapps.leafpic

```
// java.lang.RuntimeException: An error occurred while executing doInBackground()
// 	at android.os.AsyncTask$3.done(AsyncTask.java:309)
// 	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:354)
// 	at java.util.concurrent.FutureTask.setException(FutureTask.java:223)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:242)
// 	at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:234)
// 	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
// 	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
// 	at java.lang.Thread.run(Thread.java:818)
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'char[] java.lang.String.toCharArray()' on a null object reference
// 	at java.io.File.fixSlashes(File.java:183)
// 	at java.io.File.<init>(File.java:130)
// 	at org.horaapps.leafpic.data.HandlingAlbums.deleteAlbum(HandlingAlbums.java:335)
// 	at org.horaapps.leafpic.activities.MainActivity$1DeletePhotos.doInBackground(MainActivity.java:836)
// 	at org.horaapps.leafpic.activities.MainActivity$1DeletePhotos.doInBackground(MainActivity.java:821)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more

```



